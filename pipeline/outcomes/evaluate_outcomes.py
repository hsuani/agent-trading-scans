#!/usr/bin/env python3
"""0.1 + 0.2 — long_trade_plan_outcome: replay every long-shaped decision card
(stop < entry < T1) against daily OHLC and report. Short/invalid shapes are out
of scope (36 cards), so every number here is about LONG trade plans only.

Outcome enum (daily bars, no intrabar order assumed):
  T1_FIRST / STOP_FIRST            resolved
  NOT_TRIGGERED                    entry zone never touched inside the horizon
  TIMEOUT                          entered, horizon elapsed, neither level hit
  OPEN                             horizon not yet elapsed (entered or not)
  AMBIGUOUS_ENTRY_BAR              entry bar also touched T1 or stop
  AMBIGUOUS_SAME_BAR               one bar touched both T1 and stop
  INVALID_LEVELS                   entry >40% away from the signal-date close, or stop <1% from entry
  CORPORATE_ACTION                 split inside the window (levels no longer comparable)
  MARKET_DATA_UNAVAILABLE          no bars after the signal date

Horizon runs from the DECISION date, not the entry date. MFE/MAE are PRE-EXIT:
the exit bar is excluded because its high/low order vs the exit is unknown.
Primary KPI cohort = t1_source == "stated" (the analyst's own target); derived
T1s are dashboard placeholders and are reported separately.

    python3 pipeline/outcomes/evaluate_outcomes.py
      -> pipeline/outcomes/outcomes.json + pipeline/outcomes/REPORT.md
"""
import json
import random
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path
from statistics import mean, median

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cards import ROOT, collect, priced  # noqa: E402
import prices  # noqa: E402

SANITY_PCT = 40          # same tolerance as validate.py
MIN_RISK_PCT = 1.0       # stop closer than this to entry = degenerate (DBC card: 0.3% -> 44R target)
RESOLVED = ("T1_FIRST", "STOP_FIRST")
ENTERED = RESOLVED + ("TIMEOUT", "AMBIGUOUS_SAME_BAR", "AMBIGUOUS_ENTRY_BAR")
EXCLUDED = ("INVALID_LEVELS", "CORPORATE_ACTION", "MARKET_DATA_UNAVAILABLE")


def evaluate(card, bars, delay=0, ambig=None):
    """Outcome fields for one card. `delay` = trading days after the decision
    before the entry is allowed (horizon still runs from the decision date).
    `ambig` resolves every ambiguous bar along one path: "lo" = the stop wins
    whenever touched, "hi" = T1 wins whenever touched and a stop-only touch on
    the entry bar is ignored. Used only for the expectancy bounds."""
    sd = card["scan_date"]
    past = [b for b in bars if b["date"] <= sd]
    after = [b for b in bars if b["date"] > sd]
    fut, complete = after[: card["horizon_days"]], len(after) >= card["horizon_days"]
    r = {"outcome": None, "signal_close": past[-1]["close"] if past else None,
         "entry_date": None, "fill": None, "exit_date": None, "days_to_entry": None,
         "days_to_exit": None, "pre_exit_mfe": None, "pre_exit_mae": None,
         "ret_pct": None, "ret_R": None, "post_stop_reentry": None, "post_stop_hit_t1": None}
    if not fut:
        r["outcome"] = "MARKET_DATA_UNAVAILABLE"; return r
    ref = r["signal_close"] or fut[0]["open"]
    risk = card["entry_mid"] - card["stop"]                # planned 1R
    if abs(card["entry_mid"] / ref - 1) * 100 > SANITY_PCT or risk / card["entry_mid"] < MIN_RISK_PCT / 100:
        r["outcome"] = "INVALID_LEVELS"; return r          # hallucinated entry, or a stop so close it is a parse artifact
    if any(b["split"] for b in fut):
        r["outcome"] = "CORPORATE_ACTION"; return r
    lo, hi, stop, t1 = card["entry_lo"], card["entry_hi"], card["stop"], card["t1"]
    for i, b in enumerate(fut):
        if i >= delay and b["low"] <= hi and b["high"] >= lo:
            break
    else:
        r["outcome"] = "NOT_TRIGGERED" if complete else "OPEN"; return r
    r["entry_date"], r["days_to_entry"] = b["date"], i + 1
    r["fill"] = fill = min(max(card["entry_mid"], b["low"]), b["high"])
    hit_t, hit_s = b["high"] >= t1, b["low"] <= stop
    if ambig == "lo" and hit_s or ambig == "hi" and hit_t:
        r["outcome"], r["exit_date"], r["days_to_exit"] = ("STOP_FIRST" if ambig == "lo" else "T1_FIRST"), b["date"], 0
        px = stop if ambig == "lo" else t1
        r["ret_pct"], r["ret_R"] = round(px / fill - 1, 4), round((px - fill) / risk, 3)
        return r
    if ambig is None and (hit_t or hit_s):
        r["outcome"] = "AMBIGUOUS_ENTRY_BAR"; return r
    mfe = mae = 0.0
    for j, b in enumerate(fut[i + 1:], 1):
        hit_t, hit_s = b["high"] >= t1, b["low"] <= stop
        if hit_t and hit_s and ambig:
            hit_t, hit_s = ambig == "hi", ambig == "lo"
        if hit_t or hit_s:
            r["outcome"] = ("AMBIGUOUS_SAME_BAR" if hit_t and hit_s
                            else "T1_FIRST" if hit_t else "STOP_FIRST")
            r["exit_date"], r["days_to_exit"] = b["date"], j
            if r["outcome"] in RESOLVED:
                px = t1 if hit_t else stop
                r["ret_pct"], r["ret_R"] = round(px / fill - 1, 4), round((px - fill) / risk, 3)
            if r["outcome"] == "STOP_FIRST":       # what the rest of the horizon did
                rest = fut[i + 1 + j:]
                r["post_stop_reentry"] = any(x["low"] <= hi and x["high"] >= lo for x in rest)
                r["post_stop_hit_t1"] = any(x["high"] >= t1 for x in rest)
            break
        mfe, mae = max(mfe, b["high"] / fill - 1), min(mae, b["low"] / fill - 1)
    else:
        r["outcome"] = "TIMEOUT" if complete else "OPEN"
    r["pre_exit_mfe"], r["pre_exit_mae"] = round(mfe, 4), round(mae, 4)
    return r


# ---------- report ----------
def pct(a, b):
    return round(a / b, 3) if b else None


def funnel(recs):
    c = Counter(r["outcome"] for r in recs)
    open_in = sum(1 for r in recs if r["outcome"] == "OPEN" and r["entry_date"])
    open_out = c["OPEN"] - open_in
    entered = sum(c[k] for k in ENTERED) + open_in
    resolved = [r for r in recs if r["outcome"] in RESOLVED]
    closed = sum(c[k] for k in ENTERED)
    stops = [r for r in recs if r["outcome"] == "STOP_FIRST"]
    dte = [r["days_to_entry"] for r in recs if r["days_to_entry"]]
    dtx = [r["days_to_exit"] for r in resolved]
    return {"n": len(recs), "outcomes": dict(c), "open_entered": open_in, "open_not_entered": open_out,
            "matured_trigger_rate": pct(entered, entered + c["NOT_TRIGGERED"]),
            "asof_trigger_rate": pct(entered, entered + c["NOT_TRIGGERED"] + open_out),
            "resolved_n": len(resolved),
            "resolved_win_rate": pct(c["T1_FIRST"], len(resolved)),
            "expectancy_R": round(mean(r["ret_R"] for r in resolved), 3) if resolved else None,
            "expectancy_pct": round(mean(r["ret_pct"] for r in resolved), 4) if resolved else None,
            # ambiguity-adjusted bounds: the whole cohort replayed with every ambiguous
            # bar resolved along the stop path (lo) or the T1 path (hi); see evaluate(ambig=).
            "expectancy_R_bounds": [round(mean(v), 3) if v else None for v in
                                    ([r[k] for r in recs if r[k] is not None] for k in ("ret_R_lo", "ret_R_hi"))],
            "timeout_rate": pct(c["TIMEOUT"], closed),
            "ambiguous_rate": pct(c["AMBIGUOUS_SAME_BAR"] + c["AMBIGUOUS_ENTRY_BAR"], closed),
            "excluded_rate": pct(sum(c[k] for k in EXCLUDED), len(recs)),
            "post_stop_reentry_rate": pct(sum(bool(r["post_stop_reentry"]) for r in stops), len(stops)),
            "post_stop_hit_t1_rate": pct(sum(bool(r["post_stop_hit_t1"]) for r in stops), len(stops)),
            "median_days_to_entry": median(dte) if dte else None,
            "median_days_to_exit": median(dtx) if dtx else None,
            "median_pre_exit_mfe": {k: round(median([r["pre_exit_mfe"] for r in recs if r["outcome"] == k]), 4)
                                    for k in ("STOP_FIRST", "TIMEOUT") if c[k]},
            "median_pre_exit_mae": {k: round(median([r["pre_exit_mae"] for r in recs if r["outcome"] == k]), 4)
                                    for k in ("T1_FIRST", "TIMEOUT") if c[k]}}


def cluster_ci(recs, key="ret_R", n_boot=1000, seed=0):
    """Ticker-clustered bootstrap 95% CI of the mean of `key` over resolved
    trades (key="win" -> win rate). Tickers, not cards, are resampled."""
    by = defaultdict(list)
    for r in recs:
        if r["outcome"] in RESOLVED:
            by[r["ticker"]].append(1.0 if key == "win" and r["outcome"] == "T1_FIRST"
                                   else 0.0 if key == "win" else r[key])
    tick = list(by.values())
    if len(tick) < 3:
        return None
    rng, means = random.Random(seed), []
    for _ in range(n_boot):
        s = [x for _ in tick for x in rng.choice(tick)]
        means.append(sum(s) / len(s))
    means.sort()
    return [round(means[int(.025 * len(means))], 3), round(means[int(.975 * len(means)) - 1], 3)]


def md_table(rows, cols):
    out = ["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
    out += ["| " + " | ".join("" if v is None else str(v) for v in r) + " |" for r in rows]
    return "\n".join(out)


COLS = ["group", "n", "resolved", "win", "exp_R", "exp_R CI95", "exp_R bounds", "trig(matured)", "trig(asof)",
        "timeout", "ambig", "excl", "T1", "STOP", "reentry|stop", "T1|stop"]


def row(name, sub):
    s = funnel(sub)
    return [name, s["n"], s["resolved_n"], s["resolved_win_rate"], s["expectancy_R"], cluster_ci(sub),
            s["expectancy_R_bounds"], s["matured_trigger_rate"], s["asof_trigger_rate"], s["timeout_rate"], s["ambiguous_rate"],
            s["excluded_rate"], s["outcomes"].get("T1_FIRST", 0), s["outcomes"].get("STOP_FIRST", 0),
            s["post_stop_reentry_rate"], s["post_stop_hit_t1_rate"]]


def breakdown(recs, key):
    return [row(g, [r for r in recs if r[key] == g]) for g in sorted({r[key] for r in recs}, key=str)]


def report(recs):
    prim = [r for r in recs if r["t1_source"] == "stated"]
    f = funnel(prim)
    lines = [f"# long_trade_plan_outcome — {date.today().isoformat()}", "",
             f"{len(recs)} long-shaped cards replayed (daily OHLC, horizon from decision date, "
             f"MFE/MAE exclude the exit bar). **Primary cohort = stated T1 ({len(prim)} cards)**; "
             "derived T1s are dashboard placeholders (rr default 1.5 -> 0.75R) and sit below for reference.", "",
             "## Primary KPI (stated T1)", "",
             md_table([[k, f[k]] for k in ("resolved_n", "resolved_win_rate", "expectancy_R", "expectancy_pct",
                                          "expectancy_R_bounds",
                                          "matured_trigger_rate", "asof_trigger_rate", "open_entered",
                                          "open_not_entered", "timeout_rate", "ambiguous_rate", "excluded_rate",
                                          "post_stop_reentry_rate", "post_stop_hit_t1_rate",
                                          "median_days_to_entry", "median_days_to_exit")], ["metric", "value"]), "",
             f"expectancy_R 95% CI (ticker-clustered bootstrap): {cluster_ci(prim)}  ·  "
             f"win-rate CI: {cluster_ci(prim, 'win')}", "",
             f"**Ambiguity-adjusted expectancy bounds: {f['expectancy_R_bounds']}** — the cohort replayed with every "
             "ambiguous bar resolved along its stop path (lower) or its T1 path (upper); a stop-only touch on the "
             "entry bar is ignored on the upper path. No intraday order assumed.", "",
             f"pre-exit MFE median (STOP_FIRST/TIMEOUT): {f['median_pre_exit_mfe']}  ·  "
             f"pre-exit MAE median (T1_FIRST/TIMEOUT): {f['median_pre_exit_mae']}", "",
             "Outcomes: " + json.dumps(f["outcomes"], ensure_ascii=False), "",
             "## By t1_source (all cards)", "", md_table(breakdown(recs, "t1_source"), COLS), ""]
    for name, key in (("era", "era"), ("verdict", "verdict"), ("sector_v1 (scanned under)", "sector_v1"),
                      ("primary_group_v2 (1A mapping, same outcomes)", "primary_group_v2")):
        lines += [f"## Primary cohort by {name}", "", md_table(breakdown(prim, key), COLS), ""]
    lines += ["## Held — EXPLORATORY, not a treatment/control split", "",
              "`currently_held_ticker` = in today's held_tickers.txt (one commit, 2026-06-23), not the "
              "holding state on the decision date. `held_at_decision` = the PM's own framing, written only "
              "since the 08-27 prompt, so it exists for the post era only. No causal reading of either.", "",
              md_table(breakdown(prim, "currently_held_ticker"), ["currently_held_ticker"] + COLS[1:]), "",
              md_table(breakdown([r for r in prim if r["held_at_decision"] is not None], "held_at_decision"),
                       ["held_at_decision (post only)"] + COLS[1:]), ""]
    rows = [row(f"{'cur_held' if h else 'cur_nonheld'}_{e}",
                [r for r in prim if r["currently_held_ticker"] == h and r["era"] == e])
            for h in (True, False) for e in ("pre", "post")]
    lines += ["### DiD cells (currently_held_ticker × era) — exploratory", "", md_table(rows, COLS), ""]
    return "\n".join(lines)


def main():
    recs, cache = [], {}
    for c in priced(collect()):
        bars = cache.setdefault(c["ticker"], prices.load(c["ticker"]))
        recs.append({**c, **evaluate(c, bars),
                     "ret_R_lo": evaluate(c, bars, ambig="lo")["ret_R"],
                     "ret_R_hi": evaluate(c, bars, ambig="hi")["ret_R"]})
    out = ROOT / "pipeline" / "outcomes"
    (out / "outcomes.json").write_text(json.dumps(recs, ensure_ascii=False, indent=1), encoding="utf-8")
    (out / "REPORT.md").write_text(report(recs), encoding="utf-8")
    print(f"{len(recs)} cards -> outcomes.json, REPORT.md")
    print(json.dumps(funnel([r for r in recs if r["t1_source"] == "stated"]), ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
