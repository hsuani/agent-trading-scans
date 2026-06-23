#!/usr/bin/env python3
"""
Quota pre-flight check for daily trading-scan routine.

Anthropic does not expose Max-plan remaining quota via API, so this script
estimates weekly usage by walking ~/.claude/projects/**/*.jsonl session
transcripts from the past 7 days and counting:

  - assistant message events (proxy for output tokens)
  - tool_use blocks of type Agent (= subagent invocations, the biggest spend)

Compares to a configurable weekly budget. Exits:
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

# Defaults tuned for Max $100 plan ("Max 5x"):
# - Per past 7 days, full weekly budget ≈ 600 subagent (Task) calls.
# - Auto-skip threshold = 50% of budget = 300 calls used in last 7d.
# - 1 power-sector scan ≈ 100 subagent calls, so we want headroom for ad-hoc
#   manual usage on top of routine scans.
# Override via env or CLI.
DEFAULT_WEEKLY_BUDGET = 600           # full weekly subagent-call budget
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
                   help="Full weekly subagent-call budget (default 600)")
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

    usage = count_recent_usage(args.lookback)
    if "error" in usage:
        if args.pct:
            print("0")
            sys.exit(0)
        print(json.dumps(usage, indent=2))
        sys.exit(2)

    calls = usage["subagent_calls"]
    threshold_calls = args.budget * args.alert_pct // 100
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
