#!/usr/bin/env python3
"""Self-check for monitor.status() level parsing. Run: python3 test_monitor.py

Regression guard for the 2026-08-18 outage: a card whose stop text was
"N/A（無倉位，停損觸發損失 = $0）" made first_num() return 0.0, which passed the
old `if stop is not None` guard and hit `(px - stop) / stop` -> ZeroDivisionError,
killing the 正2 intraday workflow for a whole session.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("TRADING_SCANS_ROOT", os.getcwd())

from monitor import first_num, status, zone  # noqa: E402


def card(entry="", stop="", t1="", t2=""):
    return {"entry": entry, "stop": stop, "t1": t1, "t2": t2}


# first_num grabs the first number in the string — this is why "$0" bit us.
assert first_num("$220.00（MA50…）") == 220.0
assert first_num("") is None
assert first_num("N/A（無倉位）") is None
assert first_num("N/A（無倉位，停損觸發損失 = $0）") == 0.0

# The exact card that took down the workflow: must not raise.
urg, flags = status(card(stop="N/A（無倉位，停損觸發損失 = $0）"), 12.5)
assert flags == ["— in range"], flags

# A zero / negative stop is not a tradeable level — treat it as "no stop",
# same path the 591 unparseable-stop cards already take.
for bad in ("0", "$0.00", "-5"):
    urg, flags = status(card(stop=bad), 12.5)
    assert not any("stop" in f for f in flags), (bad, flags)

# A real stop still flags normally.
_, flags = status(card(stop="$100.00"), 99.0)
assert "🔴 STOP BREACHED" in flags, flags
_, flags = status(card(stop="$100.00"), 102.0)
assert any("near stop" in f for f in flags), flags
_, flags = status(card(stop="$100.00"), 500.0)
assert not any("stop" in f for f in flags), flags

# zone() can also yield 0.0 (e.g. entry "當前市價 ±0%"); the entry branch must
# not divide by it either. Unreachable today (needs px < 0) but cheap to pin.
assert zone("待觸發 — 催化劑確認當日收盤，當前市價 ±0%") == (0.0, 0.0)
status(card(entry="待觸發 — 催化劑確認當日收盤，當前市價 ±0%"), 12.5)

# No price at all -> the early-return path, never touches the levels.
assert status(card(stop="$100.00"), None) == (5, ["no price"])

print("ok")
