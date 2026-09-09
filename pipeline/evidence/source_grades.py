#!/usr/bin/env python3
"""Deterministic source grading for evidence_shadow.json — the LLM extracts
claims and names sources; THIS file decides the grade, so TrendForce is "B"
on every ticker on every day, and a policy change re-grades without an LLM.

  A  official: regulators / government statistics / exchanges / company IR & filings
  B  specialist industry research, primary research publications
  C  broker notes, mainstream financial media, secondary reporting, data vendors
  D  social, forums, anonymous channel checks, reposts
  UNKNOWN  no URL and no recognisable source name

    python3 pipeline/evidence/source_grades.py daily/2026-09-10/NVDA/evidence_shadow.json   # grade in place
    python3 pipeline/evidence/source_grades.py --domain trendforce.com                      # -> B
"""
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

GRADES = ("A", "B", "C", "D", "UNKNOWN")

# domain suffix -> grade. Longest matching suffix wins ("ir.example.com" matches "example.com").
DOMAINS = {
    # A — official
    "sec.gov": "A", "edgar-online.com": "A", "federalreserve.gov": "A", "bls.gov": "A", "census.gov": "A",
    "energy.gov": "A", "ferc.gov": "A", "bis.doc.gov": "A", "commerce.gov": "A", "whitehouse.gov": "A",
    "twse.com.tw": "A", "tpex.org.tw": "A", "mops.twse.com.tw": "A", "cbc.gov.tw": "A", "moea.gov.tw": "A",
    "dart.fss.or.kr": "A", "krx.co.kr": "A", "ecb.europa.eu": "A", "europa.eu": "A",
    "nvidia.com": "A", "amd.com": "A", "broadcom.com": "A", "marvell.com": "A", "tsmc.com": "A", "asml.com": "A",
    "micron.com": "A", "arm.com": "A", "intel.com": "A", "samsung.com": "A", "skhynix.com": "A",
    "apple.com": "A", "microsoft.com": "A", "google.com": "A", "abc.xyz": "A", "amazon.com": "A", "meta.com": "A",
    "businesswire.com": "A", "prnewswire.com": "A", "globenewswire.com": "A",   # company-issued releases
    # B — specialist research
    "trendforce.com": "B", "idc.com": "B", "gartner.com": "B", "semianalysis.com": "B",
    "counterpointresearch.com": "B", "canalys.com": "B", "omdia.com": "B", "techinsights.com": "B",
    "digitimes.com": "B", "semi.org": "B", "ieee.org": "B", "arxiv.org": "B", "yole.fr": "B",
    "yolegroup.com": "B", "isemi.com": "B", "spglobal.com": "B", "moodys.com": "B", "fitchratings.com": "B",
    "eia.gov": "A", "iea.org": "B", "nerc.com": "B", "pjm.com": "A", "ercot.com": "A",
    # C — media / brokers / data vendors
    "reuters.com": "C", "bloomberg.com": "C", "wsj.com": "C", "ft.com": "C", "cnbc.com": "C",
    "marketwatch.com": "C", "barrons.com": "C", "seekingalpha.com": "C", "fool.com": "C", "investing.com": "C",
    "finance.yahoo.com": "C", "yahoo.com": "C", "benzinga.com": "C", "tipranks.com": "C", "zacks.com": "C",
    "morningstar.com": "C", "investopedia.com": "C", "nikkei.com": "C", "asia.nikkei.com": "C",
    "cnyes.com": "C", "udn.com": "C", "ltn.com.tw": "C", "ctee.com.tw": "C", "technews.tw": "C",
    "cna.com.tw": "C", "chinatimes.com": "C", "storm.mg": "C", "bnext.com.tw": "C", "wealth.com.tw": "C",
    "tomshardware.com": "C", "theverge.com": "C", "techcrunch.com": "C", "theinformation.com": "C",
    "wccftech.com": "C", "electrek.co": "C", "koreaherald.com": "C", "businesskorea.co.kr": "C",
    # D — social
    "reddit.com": "D", "x.com": "D", "twitter.com": "D", "stocktwits.com": "D", "youtube.com": "D",
    "ptt.cc": "D", "dcard.tw": "D", "trackserenity.com": "D", "medium.com": "D", "substack.com": "D",
    "threads.net": "D", "facebook.com": "D", "tiktok.com": "D", "discord.com": "D", "telegram.org": "D",
}

# source_name (as the analyst wrote it) -> grade, used only when there is no URL.
# Matched case-insensitively as a substring; first hit in this order wins.
NAMES = [
    # the analyst's own estimate is not a source
    (r"^analyst$|analyst('s)? (own )?(estimate|inference|calculation)|分析師(自行)?(預估|推估)", "UNKNOWN"),
    (r"10-[kq]|8-k|form 4|form 13|13f|s-1|def 14a|20-f|6-k|proxy", "A"),
    (r"sec\b|edgar|regulator|fed\b|federal reserve|bls|census|ferc|doe\b|eia\b|央行|central bank|金管會|經濟部|財政部|ministry", "A"),
    (r"earnings (release|call|report)|法說|財報|earnings|guidance|investor (day|relations)|\bir\b|press release|announcement|newsroom|news room|(company|corporate|official) (release|disclosure|filing)|annual report|quarterly report|shareholder letter|公告|公開(揭露|資訊|財務)|disclosure|月營收|monthly revenue|twse|tpex|mops|年報|季報", "A"),
    (r"trendforce|idc|gartner|semianalysis|counterpoint|canalys|omdia|techinsights|digitimes|yole|s&p global|moody|fitch|iea\b|nerc|pjm|ercot|futurum|fusion worldwide|naddod|industry (research|statistics|association)|產業(研究|統計|協會)|tpca|semi\b|dell'oro|lightcounting|jpr\b", "B"),
    (r"reuters|bloomberg|wsj|wall street journal|financial times|\bft\b|cnbc|marketwatch|barron|seeking ?alpha|motley|yahoo|benzinga|tipranks|zacks|morningstar|nikkei|鉅亨|cnyes|經濟日報|工商時報|自由時報|中央社|科技新報|technews|newtalk|udn|ettoday|now ?news|digitimes|analyst|broker|券商|外資|大行|美系|goldman|morgan stanley|jpmorgan|jp morgan|bofa|美銀|bank of america|citi|ubs|barclays|jefferies|bernstein|wedbush|kgi|凱基|元大|富邦|永豐|豐雲|國泰|統一|群益|wall street|華爾街|consensus|共識|yfinance|stockstats|refinitiv|factset|lseg|"
     r"market data|市場數據|financial (statements?|data|metrics)|balance sheet|cash ?flow statement|income statement|technical (analysis|indicators|data)|技術(面|指標|分析)|price action|indicators?|fundamentals analysis|ownership|insider (trading|transaction)|institutional|機構持股|持股數據|交易資料|valuation data", "C"),
    (r"reddit|wallstreetbets|twitter|x\.com|\bx\b|stocktwits|youtube|ptt|dcard|serenity|@\w+|forum|論壇|social|retail sentiment|散戶|substack|medium|vocus|方格子|104 職場|threads|telegram|discord|channel check|渠道|傳聞|rumou?r|blog|部落格", "D"),
]


def domain_of(url):
    try:
        host = urlparse(url if "://" in url else "https://" + url).hostname or ""
    except ValueError:
        return ""
    return host.lower().lstrip("www.")


def grade_domain(domain):
    d = domain.lower()
    best = None
    for suffix, g in DOMAINS.items():
        if d == suffix or d.endswith("." + suffix):
            if best is None or len(suffix) > len(best[0]):
                best = (suffix, g)
    if best:
        return best[1]
    if re.match(r"^(ir|investor|investors)\.", d) or d.endswith(".gov") or ".gov." in d:
        return "A"
    return "UNKNOWN"


def grade(source_url="", source_name=""):
    """(grade, basis) — basis is 'domain', 'name' or 'none'."""
    if source_url:
        g = grade_domain(domain_of(source_url))
        if g != "UNKNOWN":
            return g, "domain"
    low = (source_name or "").lower()
    if low:
        for pat, g in NAMES:
            if re.search(pat, low):
                return g, "name"
    return "UNKNOWN", "none"


def grade_file(path):
    p = Path(path)
    doc = json.loads(p.read_text(encoding="utf-8"))
    for c in doc.get("claims", []):
        c["source_domain"] = domain_of(c.get("source_url", "")) if c.get("source_url") else ""
        c["source_grade"], c["grade_basis"] = grade(c.get("source_url", ""), c.get("source_name", ""))
    doc["graded_by"] = "source_grades.py"
    p.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
    return doc


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "--domain":
        print(grade_domain(a[1]))
    elif a and a[0] == "--name":
        print(grade("", a[1])[0])
    else:
        for f in a:
            d = grade_file(f)
            from collections import Counter
            print(f, dict(Counter(c["source_grade"] for c in d["claims"])))
