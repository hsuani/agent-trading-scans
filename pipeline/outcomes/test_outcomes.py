#!/usr/bin/env python3
"""Self-check for the outcome evaluator. Run: python3 pipeline/outcomes/test_outcomes.py"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cards import parse_horizon
from evaluate_outcomes import evaluate
from political import eligible, evaluate as pol_eval

# horizon: upper bound of the range, in trading days
for s, want in (("1–3 個月", 63), ("3m+", 63), ("6–10 週", 50), ("2–3 季", 189), ("", 60),
                ("2026-08 底 – 2026-10 底", 60), ("10 個交易日", 10), ("1–4 週（事件交易）", 20)):
    assert parse_horizon(s) == want, (s, parse_horizon(s), want)


def bar(d, o, h, l, c, split=0.0):
    return {"date": "2026-" + d if len(d) == 5 else d, "open": o, "high": h, "low": l, "close": c, "split": split}


CARD = {"scan_date": "2026-06-01", "horizon_days": 5, "entry_lo": 100, "entry_hi": 105,
        "entry_mid": 102.5, "stop": 95, "t1": 110}
SIG = [bar("2026-06-01", 108, 109, 107, 108)]


def run(*fut):
    return evaluate(CARD, SIG + list(fut))


# T1 before stop, MFE/MAE measured from the fill (102.5)
r = run(bar("06-02", 104, 106, 101, 103), bar("06-03", 103, 108, 102, 107), bar("06-04", 107, 111, 106, 110))
assert r["outcome"] == "T1_FIRST" and r["days_to_entry"] == 1 and r["days_to_exit"] == 2, r
assert r["fill"] == 102.5 and r["pre_exit_mae"] == round(102 / 102.5 - 1, 4), r
assert r["ret_R"] == round((110 - 102.5) / 7.5, 3) and r["ret_pct"] == round(110 / 102.5 - 1, 4), r
# pre-exit: the exit bar's high must NOT leak into MFE (exit bar high 108 > prior 106 here)
r = run(bar("06-02", 104, 106, 101, 103), bar("06-03", 103, 108, 102, 107), bar("06-04", 107, 112, 94, 95))
assert r["outcome"] == "AMBIGUOUS_SAME_BAR" and r["pre_exit_mfe"] == round(108 / 102.5 - 1, 4), r
same = SIG + [bar("06-02", 104, 106, 101, 103), bar("06-03", 103, 108, 102, 107), bar("06-04", 107, 112, 94, 95)]
assert evaluate(CARD, same, ambig="lo")["ret_R"] == -1.0 and evaluate(CARD, same, ambig="hi")["ret_R"] == 1.0
# stop before T1
r = run(bar("06-02", 104, 106, 101, 103), bar("06-03", 100, 101, 94, 95),
        bar("06-04", 96, 103, 95, 102), bar("06-05", 103, 111, 102, 110))
assert r["outcome"] == "STOP_FIRST" and r["ret_R"] == -1.0 and r["pre_exit_mfe"] == 0.0, r  # entry + exit bars excluded
assert r["post_stop_reentry"] is True and r["post_stop_hit_t1"] is True, r
# entry delay: same bars, entry withheld 1 day -> fills on 06-03 instead
r = evaluate(CARD, SIG + [bar("06-02", 104, 106, 101, 103), bar("06-03", 103, 105, 101, 104),
                          bar("06-04", 104, 111, 103, 110)], delay=1)
assert r["outcome"] == "T1_FIRST" and r["days_to_entry"] == 2, r
# same bar touches both -> never a win
r = run(bar("06-02", 104, 106, 101, 103), bar("06-03", 101, 112, 94, 105))
assert r["outcome"] == "AMBIGUOUS_SAME_BAR", r
# entry bar itself touches T1 -> not a win either
r = run(bar("06-02", 101, 112, 98, 110))
assert r["outcome"] == "AMBIGUOUS_ENTRY_BAR", r
# entry bar touched the stop only: lower path = stopped at once, upper path = ignore it and keep going
sb = SIG + [bar("06-02", 101, 104, 94, 103), bar("06-03", 103, 111, 102, 110)]
assert evaluate(CARD, sb)["outcome"] == "AMBIGUOUS_ENTRY_BAR"
assert evaluate(CARD, sb, ambig="lo")["ret_R"] == -1.0 and evaluate(CARD, sb, ambig="hi")["outcome"] == "T1_FIRST"
# zone never touched within horizon (5 bars), horizon complete
flat = [bar(f"06-{d:02d}", 120, 122, 118, 121) for d in range(2, 8)]
assert run(*flat)["outcome"] == "NOT_TRIGGERED"
# same, horizon not elapsed yet
assert run(*flat[:2])["outcome"] == "OPEN"
# entered, drifted, horizon elapsed
r = run(bar("06-02", 104, 106, 101, 103), *[bar(f"06-{d:02d}", 103, 105, 101, 104) for d in range(3, 8)])
assert r["outcome"] == "TIMEOUT" and r["pre_exit_mfe"] == round(105 / 102.5 - 1, 4), r
# entered late: horizon counts from the DECISION date, not the entry
r = run(*flat[:3], bar("06-05", 104, 106, 101, 103), bar("06-06", 103, 105, 101, 104), bar("06-07", 103, 105, 101, 104))
assert r["outcome"] == "TIMEOUT" and r["days_to_entry"] == 4, r
# split inside the window / no data / hallucinated level
assert run(bar("06-02", 104, 106, 101, 103), bar("06-03", 50, 52, 49, 51, split=2.0))["outcome"] == "CORPORATE_ACTION"
assert evaluate(CARD, SIG)["outcome"] == "MARKET_DATA_UNAVAILABLE"
assert evaluate({**CARD, "entry_mid": 300}, SIG + flat)["outcome"] == "INVALID_LEVELS"
assert evaluate({**CARD, "stop": 102.0}, SIG + flat)["outcome"] == "INVALID_LEVELS"   # degenerate 0.5% stop

# political: only confident individual equities pass; excess return is vs benchmark, sign by tx_type
ev = {"event_id": "x", "asset_type": "equity", "ticker": "T", "ticker_confidence": 0.9,
      "tx_type": "sale_full", "public_available_date": "2026-06-01"}
assert eligible(ev) and not eligible({**ev, "asset_type": "etf"}) and not eligible({**ev, "ticker_confidence": 0.5})
bars = [bar(f"06-{d:02d}", 0, 0, 0, px) for d, px in zip(range(1, 9), (100, 100, 101, 102, 103, 104, 105, 106))]
bench = [bar(f"06-{d:02d}", 0, 0, 0, 100) for d in range(1, 9)]
r = pol_eval(ev, bars, bench)
assert r["excess_5d"] == round(-(105 / 100 - 1), 4) and r["excess_20d"] is None, r
print("ok")
