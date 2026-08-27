#!/usr/bin/env python3
"""Self-check for entry/stop level parsing. Run: python3 test_levels.py

Regression guard for the fake-price class of bug. _first_nums used to take the
first two numbers out of whatever the entry field said. When a scan hit
PRICE_DATA_UNAVAILABLE the analyst correctly refused to quote levels and wrote a
condition instead — "2026 年 9 月上旬 8 月月營收公布…" — and the parser averaged
the YEAR and the MONTH into an entry price of (2026+9)/2 = 1017.5. Both 3017.TW
and 6805.TW landed on that same number, it was shown on the dashboard as a real
entry, and validate.py then reported it as 疑似幻想價 — blaming the analyst for a
number the parser invented.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("TRADING_SCANS_ROOT", os.getcwd())

from build_dashboard import _first_nums, derive_targets  # noqa: E402

# 1. A card that refuses to quote a level yields NO number, whatever digits the
#    sentence happens to contain. This is the rule that matters: the downstream
#    treats a missing level as 價格待補, which is the truth.
for txt in (
    "2026 年 9 月上旬 8 月月營收公布，達 Q2 單月均值（≈ NT$16.4 億）以上，以市價執行首批",
    "PRICE_DATA_UNAVAILABLE — 待 2026-08-26 財報後即時報價恢復",
    "無即時價格，暫不給進出場價位（財報後不晚於 2026-08-06 開盤）",
    "不設價位（PRICE_DATA_UNAVAILABLE）。進場條件＝2026-08-27 Q2 報告消化完畢（發布後 24–48 小時）",
    "無即時價格；三項條件同夜同時成立才進場：Q2 non-GAAP EPS ≥$0.80",
):
    assert _first_nums(txt) == [], (txt, _first_nums(txt))

# The exact pair that produced 1017.5.
assert derive_targets("2026 年 9 月上旬 8 月月營收公布，達 Q2 單月均值以上", "", None) \
    == (None, None, None, None)

# 2. Real levels still parse, including ranges where only the low end carries the
#    currency marker — taking just the low end would shift every derived target.
for txt, want in (
    ("$270.00 – $275.00",                      [270.0, 275.0]),
    ("NT$2,050 – NT$2,100",                    [2050.0, 2100.0]),
    ("NT$390–401（首選）/ NT$497（次選）",        [390.0, 401.0]),
    ("NT$6,000 – 6,300（分兩批各 0.20% NAV）",   [6000.0, 6300.0]),
    ("** TWD 775–795（目標均價 ≤ NT$785）",      [775.0, 795.0]),
    ("$310 / $360 call spread（現價 $303.58）",  [310.0, 360.0]),
    ("$226.00 – $230.00（R:R 3.9x, 上檔 12%）",  [226.0, 230.0]),
    ("1,017.5 – 1,050.0",                      [1017.5, 1050.0]),
):
    assert _first_nums(txt) == want, (txt, _first_nums(txt), want)

# 3. Units that are not prices never become one, even with no currency marker.
for txt in (
    "Q2 財報後 1–3 個交易日以市價分批",     # trading days
    "到期 2026-09/10 涵蓋財報後 4-6 週",   # weeks
    "H2 EPS 達標後進場，Q3 毛利率 ≥ 32%",  # halves / quarters / percent
    "2026Q3 財報後再評估",
):
    assert _first_nums(txt) == [], (txt, _first_nums(txt))

# 4. A normal long card still derives a full ladder.
emid, stop, t1, t2 = derive_targets("$270.00 – $275.00", "$256.10", 3.4)
assert emid == 272.5 and stop == 256.1 and t1 and t2 and t1 < t2, (emid, stop, t1, t2)

print("ok")
