#!/usr/bin/env python3
"""
Quota pre-flight check for daily trading-scan routine.

Anthropic does not expose Max-plan remaining quota via API, so this estimates it.

PRIMARY metric = MODEL-WEIGHTED units derived from the repo's own scan output
(daily/<date>/<ticker>/). Two reasons it is not the session transcripts:

  1. The scans run on CCR cloud containers whose ~/.claude/projects transcripts
     never reach this disk. Measured 2026-08-27: this repo's local sessions hold
     1 Agent call while ~/.claude/projects holds 1349 — i.e. the transcript count
     was reporting OTHER projects' usage, so gating on it would have throttled
     the trading scan based on unrelated work.
  2. A transcript count treats every subagent call the same. A Haiku Phase-1
     analyst and an Opus portfolio-manager are not the same spend.

Weights (haiku=1, sonnet=3.5, opus=18) match .claude/agents/trading/*.md model
frontmatter. Per ticker: 4 haiku Phase-1, and if it went through Phase 2-4,
7 sonnet + 1 opus. Per sector: 1 sonnet comparator.

Reading the repo also makes the number identical locally and in the cloud, since
both have the same git checkout.

Exits:
  0  → under threshold, OK to run
  1  → over threshold, alert + abort
  2  → cannot determine (treat as caution → abort)

Outputs JSON summary to stdout for the wrapper script to log.
"""
import argparse
import json
import os
import sys
import time
from pathlib import Path
from datetime import datetime, timedelta

PROJECTS = Path.home() / ".claude" / "projects"
SCANS_ROOT = Path(os.environ.get("TRADING_SCANS_ROOT", Path(__file__).resolve().parents[2]))

# Weighted cost per subagent call, by the model in .claude/agents/trading/*.md.
W_HAIKU, W_SONNET, W_OPUS = 1.0, 3.5, 18.0
# Per ticker: Phase 1 = 4 haiku. Full Phase 2-4 = 2 debate + 1 research-manager
# + 1 trader + 3 risk = 7 sonnet, then 1 opus portfolio-manager.
FULL_PIPELINE_UNITS = 7 * W_SONNET + W_OPUS      # 42.5


def count_repo_usage(lookback_days: int) -> dict:
    """Weighted units actually produced by scans in the last N days.

    Counts what landed on disk, so a sector that died before Phase 2 costs what
    it really cost. A ticker that reached trade_proposal.md went through the full
    Sonnet+Opus path; one with only Phase-1 reports did not.
    """
    import datetime
    daily = SCANS_ROOT / "daily"
    if not daily.is_dir():
        return {"error": f"no daily/ under {SCANS_ROOT}"}

    today = datetime.date.today()
    window = {(today - datetime.timedelta(days=i)).isoformat()
              for i in range(lookback_days)}

    units = 0.0
    tickers_full = tickers_p1 = sectors = 0
    for d in window:
        ddir = daily / d
        if not ddir.is_dir():
            continue
        for t in ddir.iterdir():
            if not t.is_dir():
                continue
            if (t / "sector_report.md").exists():
                units += W_SONNET
                sectors += 1
                continue
            p1 = sum((t / f"{n}.md").exists()
                     for n in ("fundamentals", "market", "news", "sentiment"))
            if not p1:
                continue
            units += p1 * W_HAIKU
            if (t / "trade_proposal.md").exists():
                units += FULL_PIPELINE_UNITS
                tickers_full += 1
            else:
                tickers_p1 += 1

    return {
        "lookback_days": lookback_days,
        "weighted_units": round(units, 1),
        "tickers_full_pipeline": tickers_full,
        "tickers_phase1_only": tickers_p1,
        "sector_reports": sectors,
    }

# Defaults tuned for Max $100 plan ("Max 5x"):
# - Per past 7 days, full weekly budget ≈ 600 subagent (Task) calls.
# - Auto-skip threshold = 50% of budget = 300 calls used in last 7d.
# - 1 power-sector scan ≈ 100 subagent calls, so we want headroom for ad-hoc
#   manual usage on top of routine scans.
# Override via env or CLI.
# Calibrated 2026-08-27 from 78 scan dates of real output: the 7-day rolling
# weighted total ran median 3324, max 5465. 9000 keeps a median week in the
# top-10 tier (37%) and only throttles genuine spikes (5465 -> 61% -> top 5),
# so wiring the gate on does not silently halve normal throughput.
DEFAULT_WEEKLY_BUDGET = 9000          # weekly MODEL-WEIGHTED unit budget
DEFAULT_ALERT_PCT = 50                # alert + halt when used >= this % of budget
DEFAULT_LOOKBACK_DAYS = 7


def count_recent_usage(lookback_days: int) -> dict:
    if not PROJECTS.exists():
        return {"error": f"no projects dir at {PROJECTS}"}

    cutoff = time.time() - lookback_days * 86400
    total_sessions = 0
    total_assistant_msgs = 0
    total_subagent_calls = 0
    total_bytes = 0

    for jsonl in PROJECTS.rglob("*.jsonl"):
        try:
            st = jsonl.stat()
        except OSError:
            continue
        if st.st_mtime < cutoff:
            continue
        total_sessions += 1
        total_bytes += st.st_size
        try:
            with jsonl.open("r", encoding="utf-8", errors="ignore") as f:
                for line in f:
                    if '"type":"assistant"' in line:
                        total_assistant_msgs += 1
                        # crude: any line containing "Task" tool_use is a subagent call
                        if '"name":"Task"' in line or '"name":"Agent"' in line:
                            total_subagent_calls += 1
        except Exception:
            continue

    return {
        "lookback_days": lookback_days,
        "sessions": total_sessions,
        "assistant_msgs": total_assistant_msgs,
        "subagent_calls": total_subagent_calls,
        "bytes_mb": round(total_bytes / 1024 / 1024, 1),
    }


def notify_macos(title: str, message: str) -> None:
    """Show macOS desktop notification via osascript."""
    try:
        import subprocess
        script = (f'display notification "{message}" '
                  f'with title "{title}" sound name "Submarine"')
        subprocess.run(["osascript", "-e", script], check=False, timeout=10)
    except Exception:
        pass


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--budget", type=int,
                   default=int(os.getenv("TRADING_SCAN_BUDGET",
                                         DEFAULT_WEEKLY_BUDGET)),
                   help=f"Weekly model-weighted unit budget "
                        f"(default {DEFAULT_WEEKLY_BUDGET})")
    p.add_argument("--alert-pct", type=int,
                   default=int(os.getenv("TRADING_SCAN_ALERT_PCT",
                                         DEFAULT_ALERT_PCT)),
                   help="Alert threshold as %% of budget (default 50)")
    p.add_argument("--lookback", type=int,
                   default=int(os.getenv("TRADING_SCAN_LOOKBACK",
                                         DEFAULT_LOOKBACK_DAYS)),
                   help="Days to look back (default 7)")
    p.add_argument("--quiet", action="store_true", help="suppress alert")
    p.add_argument("--pct", action="store_true",
                   help="print only the raw integer pct_of_budget and exit 0 (no alert)")
    args = p.parse_args()

    usage = count_repo_usage(args.lookback)
    if "error" in usage:
        if args.pct:
            print("0")
            sys.exit(0)
        print(json.dumps(usage, indent=2))
        sys.exit(2)

    # Transcript count kept as a secondary, local-only signal. It sees ad-hoc
    # interactive usage that never writes to daily/, but misses everything the
    # cloud routine does — never gate on it.
    usage["local_transcript_subagent_calls"] = (
        count_recent_usage(args.lookback).get("subagent_calls"))

    calls = usage["weighted_units"]
    threshold_calls = args.budget * args.alert_pct / 100
    pct_of_budget = round(100 * calls / args.budget, 1) if args.budget else 0

    # --pct: just print the number, always exit 0 (caller decides what to do)
    if args.pct:
        print(int(pct_of_budget))
        sys.exit(0)

    usage.update({
        "budget": args.budget,
        "alert_pct": args.alert_pct,
        "alert_at_calls": threshold_calls,
        "pct_of_budget": pct_of_budget,
        "status": "over" if calls >= threshold_calls else "under",
    })

    print(json.dumps(usage, indent=2))

    if calls >= threshold_calls:
        if not args.quiet:
            notify_macos(
                "Trading scan paused",
                f"Usage {pct_of_budget}% of weekly budget "
                f"({calls}/{args.budget}). Alert threshold {args.alert_pct}%. "
                f"Run /trading-scan manually if you want to proceed."
            )
        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()
