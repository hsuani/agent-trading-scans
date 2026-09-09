#!/usr/bin/env python3
"""Phase 0.5 — counterfactual surface on the stated-T1 cohort: stop width x T1
distance x entry delay. Pure replay of the same daily bars; nothing else moves.

Expectancy is in ORIGINAL R (the card's planned entry-stop distance), so a wider
stop is charged its larger loss instead of redefining the unit.

    python3 pipeline/outcomes/sensitivity.py   -> pipeline/outcomes/SENSITIVITY.md
"""
import sys
from collections import Counter
from datetime import date
from pathlib import Path
from statistics import mean, median

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cards import ROOT, collect, priced  # noqa: E402
from evaluate_outcomes import RESOLVED, evaluate, md_table  # noqa: E402
import prices  # noqa: E402

STOP_X = (1.0, 1.25, 1.5, 2.0)      # x original risk
T1_X = (0.8, 1.0, 1.2)              # x original T1 distance
DELAY = (0, 1, 3)                   # trading days entry is withheld after the decision


def variant(card, sx, tx):
    risk, up = card["entry_mid"] - card["stop"], card["t1"] - card["entry_mid"]
    return {**card, "stop": card["entry_mid"] - sx * risk, "t1": card["entry_mid"] + tx * up}


def cell(cards, bars, sx, tx, delay):
    recs, orig_R = [], {}
    for c in cards:
        v = variant(c, sx, tx)
        r = evaluate(v, bars[c["ticker"]], delay)
        if r["outcome"] in RESOLVED:        # re-express in the card's ORIGINAL R
            r["ret_R"] = round((v["t1"] if r["outcome"] == "T1_FIRST" else v["stop"]) - r["fill"], 6) \
                / (c["entry_mid"] - c["stop"])
        recs.append(r)
    c = Counter(r["outcome"] for r in recs)
    res = [r for r in recs if r["outcome"] in RESOLVED]
    stops = [r for r in recs if r["outcome"] == "STOP_FIRST"]
    entered = sum(c[k] for k in RESOLVED + ("TIMEOUT", "AMBIGUOUS_SAME_BAR", "AMBIGUOUS_ENTRY_BAR"))
    p = lambda a, b: round(a / b, 3) if b else None  # noqa: E731
    return [f"stop {sx}R", f"T1 {tx}x", f"+{delay}d", len(res), p(c["T1_FIRST"], len(res)),
            round(mean(r["ret_R"] for r in res), 3) if res else None,
            p(c["STOP_FIRST"], entered), p(c["TIMEOUT"], entered),
            p(c["AMBIGUOUS_SAME_BAR"] + c["AMBIGUOUS_ENTRY_BAR"], entered),
            median(r["days_to_exit"] for r in res) if res else None,
            p(sum(bool(r["post_stop_hit_t1"]) for r in stops), len(stops))]


COLS = ["stop", "T1", "entry", "resolved", "win", "exp_R(orig)", "stop_rate", "timeout", "ambig",
        "med_days", "T1|stop"]


def main():
    cards = [c for c in priced(collect()) if c["t1_source"] == "stated"]
    bars = {t: prices.load(t) for t in {c["ticker"] for c in cards}}
    rows = [cell(cards, bars, sx, tx, d) for d in DELAY for tx in T1_X for sx in STOP_X]
    base = next(r for r in rows if r[:3] == ["stop 1.0R", "T1 1.0x", "+0d"])
    lines = [f"# Sensitivity — stated-T1 cohort ({len(cards)} cards) — {date.today().isoformat()}", "",
             "Same bars, same horizon (from decision date). exp_R is in each card's ORIGINAL R so a wider "
             "stop pays its larger loss. Baseline row = stop 1.0R / T1 1.0x / +0d.", "",
             f"Baseline: resolved {base[3]}, win {base[4]}, exp_R {base[5]}", "",
             "## Stop x T1 (entry +0d)", "", md_table([r for r in rows if r[2] == "+0d"], COLS), "",
             "## Entry delay (original stop & T1)", "",
             md_table([r for r in rows if r[0] == "stop 1.0R" and r[1] == "T1 1.0x"], COLS), "",
             "## Full grid", "", md_table(rows, COLS), "",
             "Reading: stop-width column improving exp_R -> stop placement; delay row improving -> "
             "timing/chase; neither -> direction / selection. Max drawdown of a sequential equity curve is "
             "not computed (cards overlap in time, so there is no single position sequence to draw down)."]
    (ROOT / "pipeline" / "outcomes" / "SENSITIVITY.md").write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines[:6]))
    print(md_table([r for r in rows if r[2] == "+0d"], COLS))
    print(md_table([r for r in rows if r[0] == "stop 1.0R" and r[1] == "T1 1.0x"], COLS))


if __name__ == "__main__":
    main()
