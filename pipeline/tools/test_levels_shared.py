#!/usr/bin/env python3
"""Regression fixtures for levels.py — every one of these produced a false L0
alert or a false rank on the 2026-09-11 dashboard. Run: python3 pipeline/tools/test_levels_shared.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from levels import parse_price, parse_zone, plan_status, quote_status, trade_ready, validate_long

# R multiples, percentages, valuation multiples and yields are never prices
for s in ("2.1", "2.6", "1.8", "1.2", "3.7", "1.25", "1.5", "1", "1.25x", "2.6×", "2R", "+20%", "entry + 2R",
          "進場價 × 1.2", "10yr 回落至 **4.30%**", "10x", "寬度 7–9%", "FY2027 EPS 中值 × 10x 保守 P/E 之估值地板，寬度 7–9%"):
    assert parse_price(s, ref=1000) is None, s
assert parse_price("2.1") is None                     # bare, small, one decimal: not a price even without a ref
# real prices still parse, with or without currency
assert parse_price("NT$1,250 – NT$1,300（限價）") == 1250.0
assert parse_price("$236.26") == 236.26 and parse_price("236.26", ref=220) == 236.26
assert parse_price("900", ref=760) == 900.0 and parse_price("NT$3,050") == 3050.0
assert parse_zone("$216.00 – $221.00") == (216.0, 221.0)
assert parse_zone("成交日均價 -3% 至 +2%（分批）") == (None, None)
assert parse_price("進場均價 **-20%**") is None
assert parse_price("N/A（無倉位，停損觸發損失 = $0）") is None
assert validate_long(226.0, 230.0, 525.0, 250.0, None) == "stop >= entry"
# ANET: a date window and an index name are not an entry zone; CRDO: "$2.0B" is revenue guidance
assert parse_zone("不新增。減碼執行窗口 2026-09-18 至 09-21（S&P 100 納入被動買盤流動性窗口），分兩筆各半") == (None, None)
assert parse_price("**(1)** FY2027 營收指引 ≥ $2.0B 且毛利率指引 ≥ 66%") is None
assert parse_zone("$21 – $100") == (21.0, 21.0) and parse_zone("$216.00 – $221.00") == (216.0, 221.0)

C = lambda e="", s="", t1="", t2="": {"entry": e, "stop": s, "t1": t1, "t2": t2}  # noqa: E731
# 3163.TWO: DERIVED levels + T2 "1" -> no alert of any kind
p = plan_status(C("$740 – $780（DERIVED，GTC 確認後次一交易日市價）", "$680（DERIVED）", "900", "1"), quote=672)
assert p["plan"] == "UNPRICED" and p["t2"] is None, p
# 3017.TW / 2368.TW / 2376.TW / 3324.TWO / 3653.TW / 8996.TW: "T1 = 2.1" style never a target
p = plan_status(C("NT$3,235 – NT$3,400（僅為回調加碼區）", "NT$3,050", "2.1"), quote=3380)
assert p["plan"] == "PRICED" and p["t1"] is None and p["stop"] == 3050, p
p = plan_status(C("成交日均價 -3% 至 +2%（分批，禁止追漲停後跳空高開）", "進場均價 **-20%**", "2.6"), quote=1025)
assert p["plan"] == "UNPRICED", p
p = plan_status(C("PRICE_DATA_UNAVAILABLE — 執行前以 TWSE 即時報價為錨", "入場價 -10%（收盤價判定）", "1.8"), quote=348.5)
assert p["plan"] == "UNPRICED", p
p = plan_status(C("NT$4,200 – NT$4,500（僅在此區間成交才建倉）", "NT$3,700", "3.7"), quote=5760)
assert p["plan"] == "PRICED" and p["t1"] is None, p
# HPE: valuation-multiple stop text -> UNPRICED, never STOP BREACHED
p = plan_status(C("待即時盤口確認;以財報後回落區間為參考,不得高於財報前收盤",
                  "待盤口確認;錨定 FY2027 EPS 中值 × 10x 保守 P/E 之估值地板,寬度 7–9%"), quote=55.22)
assert p["plan"] == "UNPRICED" and p["stop"] is None, p
# 8996.TW: NT$320–360 card on a NT$1,330 stock -> LEVEL_SCALE_SUSPECT
p = plan_status(C("現價須 < NT$377.5；目標買區 NT$320 – NT$360（NT$377.5 之 -15% ~ -5%）", "進場價 -10%（若於 NT$340 進場約 NT$306）", "1.25"), quote=1330)
assert p["plan"] == "LEVEL_SCALE_SUSPECT", p
# MUB: yield-level card -> UNPRICED (its old "T2 HIT" was 4.10% read as $4.10)
p = plan_status(C("PRICE_DATA_UNAVAILABLE — 無即時價格", "10yr UST 收盤 **≥ 4.90%**", "10yr 回落至 **4.30%**", "10yr 回落至 **4.10%**"), quote=102.72)
assert p["plan"] == "UNPRICED", p
# NVDA: normal card stays PRICED with all four levels
p = plan_status(C("$216.00 – $221.00", "$208.00", "236.26", "250.00"), quote=218.36)
assert p["plan"] == "PRICED" and (p["stop"], p["t1"], p["t2"]) == (208.0, 236.26, 250.0), p
# a real absolute T2 on a priced card still exists for the monitor to hit
p = plan_status(C("$100 – $104", "$95", "$110", "$120"), quote=121)
assert p["plan"] == "PRICED" and p["t2"] == 120.0

assert quote_status("2026-09-11T05:00:00+00:00", now=__import__("datetime").datetime(2026, 9, 11, 6, tzinfo=__import__("datetime").timezone.utc)) == "LIVE"
assert quote_status("2026-09-01T05:00:00+00:00", now=__import__("datetime").datetime(2026, 9, 11, 6, tzinfo=__import__("datetime").timezone.utc)) == "STALE"
assert quote_status(None) == "UNAVAILABLE"
from datetime import date as _date
assert trade_ready("PRICED", "LIVE", "2026-09-10", today=_date(2026, 9, 11)) == "ACTIONABLE"
assert trade_ready("LEVEL_SCALE_SUSPECT", "LIVE", "2026-09-10", today=_date(2026, 9, 11)) == "NEEDS_REPRICE"
assert trade_ready("PRICED", "STALE", "2026-09-10", today=_date(2026, 9, 11)) == "DATA_STALE"
assert trade_ready("PRICED", "UNAVAILABLE", "2026-09-10", today=_date(2026, 9, 11)) == "RESEARCH_ONLY"
print("ok")
