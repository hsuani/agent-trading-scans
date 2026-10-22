#!/usr/bin/env python3
"""Offline checks for the price chain (no network). Run: python3 pipeline/tools/test_pricefeed.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pricefeed as pf

assert pf.cnyes_symbol("2330.TW") == "TWS:2330:STOCK" and pf.cnyes_symbol("6510.TWO") == "TWS:6510:STOCK"
assert pf.cnyes_symbol("nvda") == "USS:NVDA:STOCK" and pf.cnyes_symbol("000660.KS") is None

# split_adjust: a 4:1 gap back-adjusts every earlier bar; small stock dividends pass through
import datetime as _d
raw = [(_d.date(2025, 6, 10), 188, 190, 186, 188.7, 100), (_d.date(2025, 6, 18), 47.2, 48, 47, 47.6, 400),
       (_d.date(2025, 6, 19), 47.6, 48, 47, 47.9, 410)]
adj = pf.split_adjust(raw)
assert abs(adj[0][4] - 188.7 / (188.7 / 47.2)) < 1e-9 and adj[1][4] == 47.6 and adj[0][5] == 100 * (188.7 / 47.2), adj
small = [(_d.date(2026, 7, 27), 100, 101, 99, 100, 1), (_d.date(2026, 7, 28), 95, 96, 94, 95, 1)]   # 1.05 dividend
assert pf.split_adjust(small)[0][4] == 100

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
pf._cnyes_history, pf._yahoo_v8_history = mk("cnyes", None), mk("yahoo_v8", RuntimeError("blocked"))
pf._yfinance_history, pf._twse_history = mk("yfinance", bars), mk("twse", bars)
df = pf.history("X", 30)
assert calls == ["yahoo_v8", "cnyes", "yfinance"] and df.attrs["source"] == "yfinance", (calls, df.attrs)
assert list(df.columns) == ["open", "high", "low", "close", "volume"] and df.index[0] < df.index[1]
pf._yfinance_history, pf._twse_history = mk("yfinance", None), mk("twse", None)
try:
    pf.history("X", 30); raise AssertionError("expected failure")
except RuntimeError as e:
    assert "no history" in str(e)

# live-bar append: only when the quote carries a post-close trade timestamp for a session
# newer than our last bar AND its previous_close equals our last close (exact, not a guess)
from datetime import date as _d, datetime as _dt, timezone as _tz
rows = [(_d(2026, 10, 20), 1, 1, 1, 430.0, 10), (_d(2026, 10, 21), 1, 1, 1, 436.5, 10)]
ts_close = int(_dt(2026, 10, 22, 5, 30, tzinfo=_tz.utc).timestamp())      # 13:30 Taipei = TW close
ts_open = int(_dt(2026, 10, 22, 2, 0, tzinfo=_tz.utc).timestamp())        # 10:00 Taipei = mid-session
q = {"last_price": 414.0, "previous_close": 436.5, "open": 440.0, "day_high": 442.5, "day_low": 412.0, "source": "cnyes", "trade_ts": ts_close}
r2, ok = pf._append_live_bar("2408.TW", rows, q)
assert ok and r2[-1][0] == _d(2026, 10, 22) and r2[-1][4] == 414.0 and r2[-1][1] == 440.0, r2[-1]
assert not pf._append_live_bar("2408.TW", rows, dict(q, trade_ts=ts_open))[1]          # still trading -> no
assert not pf._append_live_bar("2408.TW", rows, dict(q, previous_close=420.0))[1]      # prev close mismatch -> no
assert not pf._append_live_bar("2408.TW", rows, dict(q, source="cache"))[1]            # cached quote -> no
assert not pf._append_live_bar("2408.TW", rows + [(_d(2026, 10, 22), 1, 1, 1, 414.0, 10)], q)[1]   # already have it
assert not pf._append_live_bar("2408.TW", rows, {k: v for k, v in q.items() if k != "trade_ts"})[1]  # no timestamp -> no
print("ok")
