#!/usr/bin/env python3
"""
Pure-regex catalyst extractor. No LLM. Cheap real-time.

Walks /Users/yht/Study/scans/{DATE}/{TICKER}/*.md and pulls out dated
trigger / catalyst / event mentions. Writes to
/Users/yht/Study/scans/_catalysts.json (consolidated calendar).

Triggers a desktop notification only via the separate notifier script;
this extractor is silent and idempotent.

Date forms handled:
  - 2026-05-28
  - 5/28           → resolved to current year, current/next occurrence
  - 5/28/2026
  - Q2'26          → resolved to mid-quarter date (2026-05-15)
  - "next earnings" without date → skipped

Each catalyst record:
  {
    "ticker":      "OKTA",
    "sector":      "security",
    "date":        "2026-05-28",
    "category":    "earnings | regulatory | corporate | macro | technical",
    "description": "5/28 Q1 FY2027 earnings binary",
    "verdict":     "BUY" / "HOLD" / "SELL" (from final_decision)
    "trigger_kind": "event" (date) / "level" (price)
    "source":      "VST/final_decision.md:42"
  }
"""
import argparse
import json
import re
import sys
from collections import defaultdict
from datetime import datetime, date
from pathlib import Path

import os as _os
# Portable root: env override, else repo root (this file lives at
# <repo>/pipeline/tools/, so parents[2] == repo root). Works bundled locally
# and cloned anywhere in the cloud.
SCANS_ROOT = Path(_os.environ.get("TRADING_SCANS_ROOT") or Path(__file__).resolve().parents[2])
# Per-day scan output lives under daily/<date>/. OUT stays at the root.
DAILY = SCANS_ROOT / "daily"
_DBASE = DAILY if DAILY.is_dir() else SCANS_ROOT   # tolerate pre-migration root
OUT = SCANS_ROOT / "_catalysts.json"

SECTORS = {
    "semi":      ["NVDA", "AMD", "AVGO", "MRVL", "TSM", "ASML", "MU", "ARM", "CBRS"],
    "power":     ["VST", "CEG", "TLN", "GEV", "ETN", "PWR", "NEE", "SO"],
    "cooling":   ["VRT", "MOD", "ANET", "COHR", "LITE", "FN", "AAOI", "IPGP", "GLW"],
    "reit":      ["EQIX", "DLR", "IRM", "AMT"],
    "oem":       ["SMCI", "DELL", "HPE", "2317.TW", "2382.TW"],
    "security":  ["CRWD", "PANW", "ZS", "S", "OKTA"],
    "robotics":  ["TSLA", "ISRG", "ABBNY", "FANUY", "SYM"],
    "materials": ["FCX", "MP", "LIN", "APD", "ALB"],
    "quantum":   ["IONQ", "RGTI", "QBTS", "QUBT", "ARQQ", "LAES", "HON", "IBM"],
    "photonics": ["POET", "CRDO", "ALAB", "GFS", "INTC"],
    "hedge":     ["GLD", "GDX", "TLT", "MUB", "UUP", "DBC", "BTAL", "SH"],
    "tw_photonics": ["3081.TWO", "2455.TW", "4908.TWO"],
}
TICKER_TO_SECTOR = {t: s for s, ts in SECTORS.items() for t in ts}

# Quarter midpoints (mid-month of the middle month of each quarter)
QUARTER_MIDPOINT = {1: (2, 15), 2: (5, 15), 3: (8, 15), 4: (11, 15)}

CATEGORY_KEYWORDS = {
    "earnings":   ["earnings", "EPS", "財報", "Q1", "Q2", "Q3", "Q4", "pre-announce", "guide", "guidance"],
    "regulatory": ["FERC", "DOE", "SEC", "FDA", "EU", "EUR", "regulatory", "ruling", "rule",
                   "OBBBA", "IRA", "ITC", "PTC", "tariff", "PJM", "BYOG"],
    "corporate":  ["M&A", "acquisition", "merger", "spinoff", "buyback", "dividend",
                   "PPA", "split", "insider", "Form 4", "10-K", "10-Q", "Investor Day"],
    "macro":      ["Fed", "FOMC", "CPI", "PCE", "jobs", "NFP", "rate cut", "rate hike", "ECB",
                   "BoJ", "BoE"],
}


def classify(text_window: str) -> str:
    lower = text_window.lower()
    for cat, kws in CATEGORY_KEYWORDS.items():
        for kw in kws:
            if kw.lower() in lower:
                return cat
    return "other"


def parse_date(token: str, scan_date: date) -> str | None:
    """Return YYYY-MM-DD or None."""
    token = token.strip()

    # 2026-05-28
    m = re.fullmatch(r"(\d{4})-(\d{1,2})-(\d{1,2})", token)
    if m:
        y, mo, d = map(int, m.groups())
        try:
            return date(y, mo, d).isoformat()
        except ValueError:
            return None

    # 5/28/2026 or 5/28/26
    m = re.fullmatch(r"(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})", token)
    if m:
        mo, d, y = m.groups()
        mo, d, y = int(mo), int(d), int(y)
        if y < 100:
            y += 2000
        try:
            return date(y, mo, d).isoformat()
        except ValueError:
            return None

    # 5/28 (no year — assume scan year, but only if >= scan_date - 30 days)
    m = re.fullmatch(r"(\d{1,2})/(\d{1,2})", token)
    if m:
        mo, d = int(m.group(1)), int(m.group(2))
        if not (1 <= mo <= 12 and 1 <= d <= 31):
            return None
        for y in (scan_date.year, scan_date.year + 1):
            try:
                dt = date(y, mo, d)
            except ValueError:
                continue
            # accept if within +/- 6 months of scan
            delta = (dt - scan_date).days
            if -45 <= delta <= 270:
                return dt.isoformat()
        return None

    # Q1'26, Q2'26, Q3'26, Q4'26 (and Q1 2026)
    m = re.fullmatch(r"Q([1-4])\s*['’]?\s*(\d{2}|\d{4})", token)
    if m:
        q = int(m.group(1))
        y = int(m.group(2))
        if y < 100: y += 2000
        mo, d = QUARTER_MIDPOINT[q]
        try:
            return date(y, mo, d).isoformat()
        except ValueError:
            return None

    return None


# Regex patterns to find candidate date tokens in text
DATE_PATTERNS = [
    re.compile(r"\b(\d{4}-\d{1,2}-\d{1,2})\b"),
    re.compile(r"\b(\d{1,2}/\d{1,2}/\d{2,4})\b"),
    re.compile(r"\b(\d{1,2}/\d{1,2})(?:[^\d/]|$)"),
    re.compile(r"\b(Q[1-4]\s*['’]?\s*\d{2,4})\b"),
]


def parse_verdict(final_md: str) -> str:
    m = re.search(r"FINAL TRANSACTION PROPOSAL:\s*\*?\*?\s*(BUY|HOLD|SELL)", final_md or "", re.I)
    return m.group(1).upper() if m else "UNKNOWN"


def extract_for_ticker(ticker: str, scan_date: date) -> list[dict]:
    base = _DBASE / scan_date.isoformat() / ticker
    if not base.exists():
        return []

    final_md = ""
    fd_path = base / "final_decision.md"
    if fd_path.exists():
        final_md = fd_path.read_text(encoding="utf-8", errors="ignore")
    verdict = parse_verdict(final_md)

    catalysts = []
    seen = set()  # de-dup by (date, description)

    for md in sorted(base.rglob("*.md")):
        if md.name.endswith(".en.md"):
            continue
        text = md.read_text(encoding="utf-8", errors="ignore")
        lines = text.splitlines()
        for lineno, line in enumerate(lines, 1):
            for pat in DATE_PATTERNS:
                for m in pat.finditer(line):
                    token = m.group(1)
                    iso = parse_date(token, scan_date)
                    if not iso:
                        continue
                    # capture 1 line of context (this line, trimmed)
                    desc = line.strip()
                    # trim very long lines
                    if len(desc) > 300:
                        idx = m.start()
                        desc = line[max(0, idx-80):idx+220].strip()
                    key = (iso, desc[:120])
                    if key in seen:
                        continue
                    seen.add(key)
                    catalysts.append({
                        "ticker":       ticker,
                        "sector":       TICKER_TO_SECTOR.get(ticker, "unknown"),
                        "date":         iso,
                        "category":     classify(desc),
                        "description":  desc,
                        "verdict":      verdict,
                        "trigger_kind": "event",
                        "source":       f"{ticker}/{md.relative_to(base)}:{lineno}",
                    })
    return catalysts


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--scan-date", default=None, help="YYYY-MM-DD (default: latest scan dir)")
    p.add_argument("--out", default=str(OUT), type=Path)
    args = p.parse_args()

    if args.scan_date:
        scan_date = date.fromisoformat(args.scan_date)
    else:
        # pick the latest YYYY-MM-DD dir under scans/
        dirs = sorted(d for d in _DBASE.iterdir() if d.is_dir() and re.fullmatch(r"\d{4}-\d{2}-\d{2}", d.name))
        if not dirs:
            print("no scan dirs found", file=sys.stderr)
            sys.exit(1)
        scan_date = date.fromisoformat(dirs[-1].name)

    all_cats: list[dict] = []
    for sector, tickers in SECTORS.items():
        for tk in tickers:
            all_cats.extend(extract_for_ticker(tk, scan_date))

    # sort by date asc, then ticker
    all_cats.sort(key=lambda c: (c["date"], c["ticker"]))

    by_date = defaultdict(list)
    for c in all_cats:
        by_date[c["date"]].append(c)

    out = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "scan_date":    scan_date.isoformat(),
        "total":        len(all_cats),
        "by_date":      dict(by_date),
        "all":          all_cats,
    }
    args.out.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"extracted {len(all_cats)} catalysts across {len(by_date)} dates → {args.out}")


if __name__ == "__main__":
    main()
