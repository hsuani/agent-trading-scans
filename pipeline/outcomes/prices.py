#!/usr/bin/env python3
"""Daily OHLC cache for the outcome tracker. Raw (unadjusted) prices + split
events, one CSV per ticker under pipeline/outcomes/prices/ (gitignored).

    python3 pipeline/outcomes/prices.py            # refresh every ticker in _tickers.txt
    python3 pipeline/outcomes/prices.py NVDA SPY   # just these
"""
import csv
import sys
import warnings
from datetime import date
from pathlib import Path

warnings.filterwarnings("ignore")

DIR = Path(__file__).resolve().parent / "prices"
START = "2026-05-01"          # earliest scan is 2026-05-15
COLS = ("date", "open", "high", "low", "close", "split")


def load(ticker):
    """[{date, open, high, low, close, split}] sorted by date, [] if no cache."""
    f = DIR / f"{ticker}.csv"
    if not f.is_file():
        return []
    with f.open() as fh:
        rows = list(csv.DictReader(fh))
    for r in rows:
        for k in COLS[1:]:
            r[k] = float(r[k])
    # yfinance back-adjusts OHLC for splits whatever auto_adjust says; cards quote
    # the price of their day, so undo it: bars before a split x its ratio.
    factor = 1.0
    for r in reversed(rows):
        for k in ("open", "high", "low", "close"):
            r[k] *= factor
        if r["split"]:
            factor *= r["split"]
    return rows


def fetch(ticker):
    import yfinance as yf
    kw = dict(start=START, end=date.today().isoformat(), auto_adjust=False, actions=True)
    df = yf.Ticker(ticker).history(**kw)
    if (df is None or df.empty) and ticker.endswith(".TW"):   # 上櫃 listed under .TWO
        df = yf.Ticker(ticker + "O").history(**kw)
    if df is None or df.empty:
        return 0
    DIR.mkdir(exist_ok=True)
    with (DIR / f"{ticker}.csv").open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(COLS)
        for idx, r in df.iterrows():
            w.writerow([idx.date().isoformat(), r["Open"], r["High"], r["Low"],
                        r["Close"], r.get("Stock Splits", 0.0) or 0.0])
    return len(df)


if __name__ == "__main__":
    tickers = sys.argv[1:] or (DIR / "_tickers.txt").read_text().split()
    bad = []
    for t in tickers:
        try:
            n = fetch(t)
        except Exception as e:      # noqa: BLE001 — keep going, report at end
            n, e_ = 0, e
        if not n:
            bad.append(t)
        print(f"{t:12} {n} bars", flush=True)
    print("FAILED:", bad or "none")
