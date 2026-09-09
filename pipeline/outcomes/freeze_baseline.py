#!/usr/bin/env python3
"""0.0 — freeze the pre-v2 decision distribution + the configuration that
produced it. Immutable: refuses to overwrite an existing file (use --force).

    python3 pipeline/outcomes/freeze_baseline.py
"""
import hashlib
import json
import subprocess
import sys
from collections import Counter
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cards import ROOT, PROMPT_CUTOFF, collect, priced, held_set  # noqa: E402

VERDICTS = ("BUY", "HOLD", "SELL", "UNKNOWN")


def _git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True).stdout.strip()


def verdict_stats(cards):
    n = len(cards)
    cnt = Counter(c["verdict"] for c in cards)
    return {"n": n, **{v: cnt.get(v, 0) for v in VERDICTS},
            **{f"{v}_rate": round(cnt.get(v, 0) / n, 4) if n else None for v in VERDICTS}}


def agent_models():
    out = {}
    for f in sorted((ROOT / ".claude" / "agents" / "trading").glob("*.md")):
        for line in f.read_text().splitlines()[:8]:
            if line.startswith("model:"):
                out[f.stem] = line.split(":", 1)[1].strip()
    return out


def main(force=False):
    out = ROOT / "pipeline" / "baselines" / f"pre_v2_{date.today().isoformat()}.json"
    if out.exists() and not force:
        sys.exit(f"{out} exists — baseline is immutable (pass --force to overwrite)")
    cards = list(collect())
    full = [c for c in cards if not c["stub"]]
    groups = {
        "all": cards, "full_run": full, "stub": [c for c in cards if c["stub"]],
        "cur_held_full": [c for c in full if c["currently_held_ticker"]],
        "cur_nonheld_full": [c for c in full if not c["currently_held_ticker"]],
        "post_held_at_decision": [c for c in cards if c["held_at_decision"] is True],
        "post_new_at_decision": [c for c in cards if c["held_at_decision"] is False],
        "pre": [c for c in cards if c["era"] == "pre"],
        "post": [c for c in cards if c["era"] == "post"],
    }
    # EXPLORATORY cells: currently-held ticker (today's list) x pre/post prompt cutoff.
    # Not a treatment/control split — the held list is not point-in-time.
    did = {f"cur_{h}_{e}": verdict_stats([c for c in full if c["currently_held_ticker"] == (h == "held")
                                           and c["era"] == e])
           for h in ("held", "nonheld") for e in ("pre", "post")}
    code = [ROOT / "pipeline" / "tools" / "build_dashboard.py",
            *sorted((ROOT / "pipeline" / "outcomes").glob("*.py"))]
    diff = _git("diff", "HEAD")
    pm = ROOT / ".claude" / "agents" / "trading" / "portfolio-manager.md"
    skill = ROOT / ".claude" / "skills" / "trading-scan" / "SKILL.md"
    doc = {
        "frozen_at": date.today().isoformat(),
        "git_head_sha": _git("rev-parse", "HEAD"),
        "git_dirty": bool(_git("status", "--porcelain", "--untracked-files=no")),
        "git_diff_sha256": hashlib.sha256(diff.encode()).hexdigest() if diff else None,
        "code_sha256": {f.name: hashlib.sha256(f.read_bytes()).hexdigest() for f in code},
        "scan_date_range": [min(c["scan_date"] for c in cards), max(c["scan_date"] for c in cards)],
        "prompt_cutoff": PROMPT_CUTOFF,
        "pm_prompt_commits": _git("log", "--format=%h %ad %s", "--date=short", "--", str(pm)).splitlines(),
        "pm_prompt_blob": _git("hash-object", str(pm)),
        "positive_gate_blob": _git("hash-object", str(skill)),
        "agent_models": agent_models(),
        "risk_agents": sorted(k for k in agent_models() if k.startswith("risk-")),
        "held_tickers": sorted(held_set()),
        "held_list_note": "held_tickers.txt has a single commit (2026-06-23). currently_held_ticker = today's list, "
                          "NOT point-in-time; held_at_decision = PM's own framing, post-08-27 cards only",
        "counts": {"final_decisions": len(cards), "entry_and_stop": sum(1 for c in cards if c["entry_mid"] and c["stop"]),
                   "full_price_cards": len(priced(cards)),
                   "full_price_cards_note": "entry+stop+T1 derivable via build_dashboard.derive_targets (long-shaped: stop < entry)"},
        "verdicts": {k: verdict_stats(v) for k, v in groups.items()},
        "exploratory_cur_held_x_era_sell_rate": did,
        "sectors": dict(Counter(c["sector_v1"] for c in cards).most_common()),
        "modify": dict(Counter(c["modify"] or "-" for c in cards).most_common()),
    }
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"wrote {out.relative_to(ROOT)}")
    for k, v in doc["verdicts"].items():
        print(f"  {k:14} n={v['n']:5}  SELL {v['SELL_rate']}  BUY {v['BUY_rate']}  UNKNOWN {v['UNKNOWN_rate']}")
    print("  exploratory cur_held x era SELL:", {k: (v["SELL"], v["n"], v["SELL_rate"]) for k, v in did.items()})


if __name__ == "__main__":
    main(force="--force" in sys.argv)
