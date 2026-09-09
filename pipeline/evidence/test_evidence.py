#!/usr/bin/env python3
"""Self-check for the deterministic grader + KPI math. Run: python3 pipeline/evidence/test_evidence.py"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from source_grades import grade, grade_domain, domain_of
from evidence_report import kpis

# domain resolution: longest suffix wins, ir./gov fallbacks, unknown stays unknown
assert grade_domain("trendforce.com") == "B" and grade_domain("www.trendforce.com") == "B"
assert grade_domain("press.trendforce.com") == "B" and grade_domain("sec.gov") == "A"
assert grade_domain("ir.someco.com") == "A" and grade_domain("data.moea.gov.tw") == "A"
assert grade_domain("reddit.com") == "D" and grade_domain("randomblog.io") == "UNKNOWN"
assert domain_of("https://www.reuters.com/x?y=1") == "reuters.com"
# URL beats name; name only when there is no usable URL; grade never implies status
assert grade("https://www.reddit.com/r/x", "Reuters") == ("D", "domain")
assert grade("", "TrendForce 2026-09 HBM report") == ("B", "name")
assert grade("", "Q2 FY27 earnings release") == ("A", "name")
assert grade("", "") == ("UNKNOWN", "none")
assert grade("https://unknown.example", "Bloomberg") == ("C", "name")
assert grade("", "Market data as of 2026-09-07") == ("C", "name") and grade("", "豐雲學堂") == ("C", "name")
assert grade("", "NVIDIA announcement") == ("A", "name") and grade("", "Vocus") == ("D", "name")
assert grade("", "analyst") == ("UNKNOWN", "name")   # the analyst's own estimate is not a source

docs = [{"_ticker": "T", "_date": "2026-09-10", "claims": [
    {"origin_agent": "news", "evidence_key": "E1", "source_url": "https://sec.gov/a", "source_name": "", "source_grade": "A", "grade_basis": "domain", "claim_status": "EXPECTED"},
    {"origin_agent": "fundamentals", "evidence_key": "E1", "source_url": "", "source_name": "10-Q", "source_grade": "A", "grade_basis": "name", "claim_status": "CONFIRMED"},
    {"origin_agent": "sentiment", "evidence_key": "E2", "source_url": "", "source_name": "", "source_grade": "UNKNOWN", "grade_basis": "none", "claim_status": "RUMOR"},
    {"origin_agent": "market", "evidence_key": "E3", "source_url": "", "source_name": "yfinance", "source_grade": "C", "grade_basis": "name", "claim_status": "CONFIRMED"},
]}]
k = kpis(docs)
assert k["claims"] == 4 and k["source_coverage"] == 0.75 and k["url_coverage"] == 0.25, k
assert k["unknown_grade_rate"] == 0.25 and k["unsupported_claim_rate"] == 0.25, k
assert k["duplicate_claim_rate"] == 0.25 and k["independent_evidence"]["T@2026-09-10"] == {"claims": 4, "unique_keys": 3, "unique_sources": 2}, k
assert k["duplicate_by_source"] == 0.5, k
assert k["grade_x_status"]["A/EXPECTED"] == 1   # an A source with a forward-looking claim stays EXPECTED
print("ok")
