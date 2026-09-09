#!/usr/bin/env python3
"""Deterministic checks for the catalyst extractor + briefing selection.
Run: python3 pipeline/tools/test_catalysts.py"""
import os
import sys
import tempfile
from datetime import date
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("TRADING_SCANS_ROOT", os.getcwd())
import extract_catalysts as ex  # noqa: E402
from catalyst_notify import select_events, dedup  # noqa: E402

SD = date(2026, 9, 9)
# dates: precision is explicit; quarter tokens are never "exact"
assert ex.parse_date("2026-09-17", SD) == ("2026-09-17", "exact_day")
assert ex.parse_date("2026/09/17", SD) == ("2026-09-17", "exact_day")
assert ex.parse_date("9/17", SD) == ("2026-09-17", "exact_day")
assert ex.parse_date("Q4'26", SD) == ("2026-11-15", "quarter")
assert ex.parse_date("13/40", SD) == (None, None)

# category needs an EVENT word; a bare quarter / agency name is not an event
assert ex.classify("2026-10-29 Q3 財報") == "earnings"
assert ex.classify("Q3 estimate implies 12% growth") == "other"
assert ex.classify("資料來源包含 S&P、Reddit、SEC、13F") == "other"          # the HPE false positive
assert ex.classify("FERC ruling expected 2026-09-20") == "regulatory"
assert ex.classify("Deutsche Bank 首次覆蓋 COHR 2026-08-31") == "other"   # "Bank" is not "ban"
assert ex.classify("2026-09-15/16 FOMC 利率決議") == "macro"
assert ex.classify("除息日 2026-09-18") == "corporate"

# source roles: debate / plan / proposal never feed the calendar; final_decision only its catalyst section
with tempfile.TemporaryDirectory() as tmp:
    base = Path(tmp) / "2026-09-09" / "TST"
    base.mkdir(parents=True)
    (base / "news.md").write_text("- 2026-09-20 Q3 財報 earnings call\n- 2026-09-20 Q3 財報（法說會）\n", encoding="utf-8")
    (base / "fundamentals.md").write_text("Q3 財報 2026-09-20 預期 EPS 1.2\n", encoding="utf-8")
    (base / "final_decision.md").write_text(
        "FINAL TRANSACTION PROPOSAL: **HOLD**\n## Monitoring trigger\n- 若 2026-09-25 前跌破 $100 則減碼\n"
        "## Catalyst calendar\n- 2026-09-25 除息日\n", encoding="utf-8")
    (base / "risk_debate").mkdir()
    (base / "risk_debate" / "neutral.md").write_text("- 2026-09-05 財報前買 $390 put hedge\n", encoding="utf-8")
    (base / "investment_plan.md").write_text("- 2026-09-30 財報後加碼\n", encoding="utf-8")
    ex._DBASE = Path(tmp)
    recs = ex.extract_for_ticker("TST", SD)
    srcs = {r["source"].split("/")[1].split(":")[0] for r in recs}
    assert srcs == {"news.md", "final_decision.md"}, srcs      # fundamentals' earnings line merged into news' record
    dates = sorted(r["date"] for r in recs)
    assert "2026-09-05" not in dates and "2026-09-30" not in dates, dates      # debate / plan excluded
    assert all(r["source_role"] == "fact" and r["current_verdict"] == "HOLD" for r in recs)
    ev = [r for r in recs if r["date"] == "2026-09-20"]
    assert len(ev) == 1 and ev[0]["source"] == "TST/news.md:1", ev   # one event; news beats fundamentals, fuller line wins
    assert ex.classify("2026-09-18 除息日 + investor day", with_subtype=True) == ("corporate", "除息")
    assert [r for r in recs if r["date"] == "2026-09-25"][0]["category"] == "corporate"   # catalyst section kept
    assert not any("跌破" in r["description"] for r in recs)                               # monitoring rule dropped
    # per-ticker latest scan: an older date dir with the fact files is found; a newer one without them is not
    (Path(tmp) / "2026-09-10" / "TST").mkdir(parents=True)
    assert ex.latest_scan_for_ticker("TST", date(2026, 9, 10)) == "2026-09-09"
    assert ex.latest_scan_for_ticker("TST", date(2026, 9, 8)) is None

# briefing selection: exact-day only in TODAY/NEXT, quarter goes to LATER, event_key dedupe keeps two events on one day
today = date(2026, 9, 10)
recs = [
    {"ticker": "A", "date": "2026-09-10", "date_precision": "exact_day", "category": "earnings", "description": "Q3 財報", "event_key": "A|2026-09-10|earnings|q3 財報"},
    {"ticker": "A", "date": "2026-09-10", "date_precision": "exact_day", "category": "corporate", "description": "除息", "event_key": "A|2026-09-10|corporate|除息"},
    {"ticker": "A", "date": "2026-09-10", "date_precision": "exact_day", "category": "earnings", "description": "Q3 財報 longer longer longer text", "event_key": "A|2026-09-10|earnings|q3 財報"},
    {"ticker": "B", "date": "2026-11-15", "date_precision": "quarter", "category": "earnings", "description": "Q4 財報", "event_key": "B|2026-11-15|earnings|q4 財報"},
    {"ticker": "C", "date": "2026-09-01", "date_precision": "exact_day", "category": "other", "description": "x", "event_key": "C|x"},
    {"ticker": "D", "date": "2026-09-08", "date_precision": "exact_day", "category": "macro", "description": "CPI", "event_key": "D|cpi"},
]
up, hist, later = select_events(recs, today, 3, 14)
assert [e["description"] for e in up] == ["Q3 財報", "除息"], up        # first record wins, both events kept
assert [e["ticker"] for e in later] == ["B"] and [e["ticker"] for e in hist] == ["D"]
assert len(dedup(recs[:3])) == 2
print("ok")
