#!/usr/bin/env python3
"""0.3 — political-trade signal schema + outcome evaluator. Framework only:
no scrapers (Phase 3). Fixtures are mock; nothing here is a real filing.

The signal date is ALWAYS public_available_date. Measuring from
transaction_date is look-ahead bias (disclosure lags up to 45 days).

    python3 pipeline/outcomes/political.py [events.json]   # default: fixtures/political_mock.json
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import prices  # noqa: E402

HORIZONS = (5, 20, 60)          # trading days after public_available_date
BENCHMARK = "SPY"
MIN_TICKER_CONFIDENCE = 0.8     # below: stays in raw, never becomes a signal

# One PoliticalTradeEvent. Amount fields are the statutory bracket edges
# ($1,001–$15,000 …), not a point estimate — never treat them as continuous.
SCHEMA = {
    "event_id": "str  stable hash of (source, filer, ticker, transaction_date, tx_type, amount_low)",
    "source": "house_clerk | senate_efd | oge_278t",
    "filer": "str", "office": "str", "party": "str | null",
    "owner": "SELF | SPOUSE | DEPENDENT | JOINT",
    "asset_name": "str  free text as filed",
    "asset_type": "equity | option | etf | fund | bond | other",
    "ticker": "str | null", "ticker_confidence": "0..1",
    "tx_type": "purchase | sale_full | sale_partial | exchange",
    "amount_low": "int USD bracket floor", "amount_high": "int USD bracket ceiling",
    "transaction_date": "YYYY-MM-DD", "filing_date": "YYYY-MM-DD",
    "public_available_date": "YYYY-MM-DD  <- the ONLY signal date",
    "in_universe": "bool  already covered by a sector scan (flag only, no re-run)",
    "raw_ref": "str  URL / PDF page for audit",
}


def eligible(ev, min_conf=MIN_TICKER_CONFIDENCE):
    """v0 hard gate only: individual equity with a confident ticker. Amount and
    party thresholds wait for an outcome distribution — no invented weights."""
    return ev.get("asset_type") == "equity" and bool(ev.get("ticker")) \
        and float(ev.get("ticker_confidence") or 0) >= min_conf \
        and bool(ev.get("public_available_date"))


def dedupe(events):
    seen, out = set(), []
    for ev in events:
        k = (ev["source"], ev["filer"], ev.get("ticker"), ev["transaction_date"], ev["tx_type"], ev["amount_low"])
        if k not in seen:
            seen.add(k); out.append(ev)
    return out


def _fwd_close(bars, signal_date, n):
    """Close n bars after the first bar strictly after signal_date (that bar is
    the earliest a follower can act); None if not enough history yet."""
    fut = [b for b in bars if b["date"] > signal_date]
    if len(fut) <= n:
        return None, None
    return fut[0]["close"], fut[n]["close"]


def evaluate(ev, bars, bench):
    """Excess return of following the disclosure at each horizon (sign follows
    tx_type: a sale is measured as a short)."""
    sign = 1 if ev["tx_type"] == "purchase" else -1
    out = {"event_id": ev["event_id"], "ticker": ev["ticker"], "signal_date": ev["public_available_date"]}
    for n in HORIZONS:
        e0, e1 = _fwd_close(bars, ev["public_available_date"], n)
        b0, b1 = _fwd_close(bench, ev["public_available_date"], n)
        out[f"excess_{n}d"] = (round(sign * ((e1 / e0 - 1) - (b1 / b0 - 1)), 4)
                               if e0 and b0 else None)
    return out


def main(path):
    events = dedupe(json.loads(Path(path).read_text()))
    bench = prices.load(BENCHMARK)
    for ev in events:
        if not eligible(ev):
            print(f"skip {ev['event_id']}: not eligible"); continue
        print(json.dumps(evaluate(ev, prices.load(ev["ticker"]), bench)))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).parent / "fixtures" / "political_mock.json")
