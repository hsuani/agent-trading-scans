#!/usr/bin/env python3
"""Offline checks for the price chain (no network). Run: python3 pipeline/tools/test_pricefeed.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pricefeed as pf

assert pf.cnyes_symbol("2330.TW") == "TWS:2330:STOCK" and pf.cnyes_symbol("6510.TWO") == "TWS:6510:STOCK"
assert pf.cnyes_symbol("nvda") == "USS:NVDA:STOCK" and pf.cnyes_symbol("000660.KS") is None

# history() walks the chain in order and stops at the first feed with bars
calls = []
def mk(name, rows):
    def f(t, d):
        calls.append(name)
        if isinstance(rows, Exception):
            raise rows
        return rows
    return f
import datetime as dt
bars = [(dt.date(2026, 9, 8), 1, 2, 0.5, 1.5, 10), (dt.date(2026, 9, 9), 1.5, 2.5, 1, 2, 11)]
pf._cnyes_history, pf._yahoo_v8_history = mk("cnyes", RuntimeError("blocked")), mk("yahoo_v8", None)
pf._yfinance_history, pf._twse_history = mk("yfinance", bars), mk("twse", bars)
df = pf.history("X", 30)
assert calls == ["cnyes", "yahoo_v8", "yfinance"] and df.attrs["source"] == "yfinance", (calls, df.attrs)
assert list(df.columns) == ["open", "high", "low", "close", "volume"] and df.index[0] < df.index[1]
pf._yfinance_history, pf._twse_history = mk("yfinance", None), mk("twse", None)
try:
    pf.history("X", 30); raise AssertionError("expected failure")
except RuntimeError as e:
    assert "no history" in str(e)
print("ok")
