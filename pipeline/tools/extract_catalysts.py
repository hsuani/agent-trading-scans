#!/usr/bin/env python3
"""
Pure-regex catalyst extractor. No LLM. Cheap real-time.

For EVERY ticker in the static universe, reads that ticker's LATEST available
scan (sectors scan on different weekdays, so a single global date would drop
most of the universe) and pulls dated events out of the FACT sources only:

  FACT     news.md, fundamentals.md, and the "Catalyst calendar" section of
           final_decision.md (Monitoring trigger is a conditional decision rule,
           not an event — excluded)
  excluded debate/, risk_debate/, investment_plan.md, trade_proposal.md,
           market.md, sentiment.md — analyst reasoning, not events

Writes _catalysts.json (consolidated calendar). Each record:
  {
    "ticker": "OKTA", "sector": "security",
    "date": "2026-05-28",            # quarter tokens still map to the mid-quarter day
    "date_precision": "exact_day" | "quarter",   # ...but say so; briefing only trusts exact_day
    "category": "earnings | regulatory | corporate | macro | other",
    "description": "...", "source": "OKTA/news.md:42", "source_role": "fact",
    "event_key": "OKTA|2026-05-28|earnings|earnings",   # ticker|day|type|event word
    "scan_date": "2026-09-07",        # the scan the record came from
    "current_verdict": "BUY", "current_verdict_scan_date": "2026-09-07",
    "verdict": "BUY",                 # alias of current_verdict (older consumers)
    "trigger_kind": "event"
  }
Same event mentioned by several files collapses to one record: source priority
news > fundamentals > final_decision, then the more complete description.
"""
import argparse
import json
import re
import sys
from collections import OrderedDict, defaultdict
from datetime import datetime, date
from pathlib import Path
from zoneinfo import ZoneInfo

import os as _os
SCANS_ROOT = Path(_os.environ.get("TRADING_SCANS_ROOT") or Path(__file__).resolve().parents[2])
DAILY = SCANS_ROOT / "daily"
_DBASE = DAILY if DAILY.is_dir() else SCANS_ROOT
OUT = SCANS_ROOT / "_catalysts.json"
TPE = ZoneInfo("Asia/Taipei")

sys.path.insert(0, str(Path(__file__).resolve().parent))
import universe as _u  # noqa: E402
SECTORS = OrderedDict(_u.PEER_GROUPS); SECTORS[_u.UNASSIGNED_KEY] = list(_u.UNASSIGNED)   # static universe only
TICKER_TO_SECTOR = {t: s for s, ts in SECTORS.items() for t in ts}

QUARTER_MIDPOINT = {1: (2, 15), 2: (5, 15), 3: (8, 15), 4: (11, 15)}

# Source roles. Only "fact" files feed the calendar.
FACT_FILES = {"news.md": 0, "fundamentals.md": 1, "final_decision.md": 2}   # value = priority
# Inside final_decision.md only these sections are event lists, not reasoning.
FD_SECTION_RE = re.compile(r"catalyst|催化|事件日曆|calendar", re.I)

# Event words — a date next to a bare "Q3" or "SEC" is not an event.
CATEGORY_RULES = {
    "earnings":   r"\b(earnings|results|quarterly report)\b|reports? q[1-4]|財報|法說|季報|營收公布|revenue (release|report)|月營收",
    "regulatory": r"\b(ruling|decision|hearing|approval|approved?|deadline|effective|vote|ban|banned)\b|裁決|裁定|審查|批准|生效|判決|聽證|投票|禁令|關稅生效|tariff (deadline|decision|takes effect)",
    "corporate":  r"m&a|acquisition|merger|spin-?off|buyback|ex-?dividend|dividend|除息|除權|ppa|stock split|investor day|analyst day|shareholder meeting|股東會|法人說明會|form 4|10-k|10-q|8-k|product launch|發表會|上市",
    "macro":      r"\bfed\b|fomc|\bcpi\b|\bpce\b|\bnfp\b|jobs report|rate (decision|cut|hike)|\becb\b|\bboj\b|\bboe\b|央行|利率決議",
}


def classify(text_window: str, with_subtype: bool = False):
    """Category, or (category, subtype) — subtype = the event word that matched,
    so two corporate events on one day (dividend vs investor day) stay distinct."""
    low = text_window.lower()
    for cat, pat in CATEGORY_RULES.items():
        m = re.search(pat, low)
        if m:
            sub = re.sub(r"\s+", "_", m.group(0).strip())
            return (cat, sub) if with_subtype else cat
    return ("other", "") if with_subtype else "other"


def parse_date(token: str, scan_date: date):
    """(YYYY-MM-DD, precision) or (None, None)."""
    token = token.strip()
    m = re.fullmatch(r"(\d{4})[-/](\d{1,2})[-/](\d{1,2})", token)     # 2026-09-17 / 2026/09/17 (TW style)
    if m:
        y, mo, d = map(int, m.groups())
        try:
            return date(y, mo, d).isoformat(), "exact_day"
        except ValueError:
            return None, None
    m = re.fullmatch(r"(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})", token)
    if m:
        mo, d, y = (int(x) for x in m.groups())
        y += 2000 if y < 100 else 0
        try:
            return date(y, mo, d).isoformat(), "exact_day"
        except ValueError:
            return None, None
    m = re.fullmatch(r"(\d{1,2})/(\d{1,2})", token)
    if m:
        mo, d = int(m.group(1)), int(m.group(2))
        if not (1 <= mo <= 12 and 1 <= d <= 31):
            return None, None
        for y in (scan_date.year, scan_date.year + 1):
            try:
                dt = date(y, mo, d)
            except ValueError:
                continue
            if -45 <= (dt - scan_date).days <= 270:
                return dt.isoformat(), "exact_day"
        return None, None
    m = re.fullmatch(r"Q([1-4])\s*['’]?\s*(\d{2}|\d{4})", token)
    if m:
        q, y = int(m.group(1)), int(m.group(2))
        y += 2000 if y < 100 else 0
        mo, d = QUARTER_MIDPOINT[q]
        try:
            return date(y, mo, d).isoformat(), "quarter"
        except ValueError:
            return None, None
    return None, None


DATE_PATTERNS = [
    re.compile(r"\b(\d{4}[-/]\d{1,2}[-/]\d{1,2})\b"),
    re.compile(r"\b(\d{1,2}/\d{1,2}/\d{2,4})\b"),
    re.compile(r"\b(\d{1,2}/\d{1,2})(?:[^\d/]|$)"),
    re.compile(r"\b(Q[1-4]\s*['’]?\s*\d{2,4})\b"),
]


def parse_verdict(final_md: str) -> str:
    m = re.search(r"FINAL TRANSACTION PROPOSAL:\s*\*?\*?\s*(BUY|HOLD|SELL)", final_md or "", re.I)
    return m.group(1).upper() if m else "UNKNOWN"


def latest_scan_for_ticker(ticker: str, as_of: date):
    """Newest daily/<date>/<ticker>/ (<= as_of) holding at least one fact file."""
    best = None
    for d in _DBASE.iterdir():
        if not (d.is_dir() and re.fullmatch(r"\d{4}-\d{2}-\d{2}", d.name)) or d.name > as_of.isoformat():
            continue
        t = d / ticker
        if t.is_dir() and any((t / f).exists() for f in FACT_FILES) and (best is None or d.name > best):
            best = d.name
    return best


def fd_fact_lines(text: str):
    """Line numbers (1-based) of final_decision.md that sit inside an event section."""
    keep, inside = set(), False
    for i, line in enumerate(text.splitlines(), 1):
        if line.startswith("#"):
            inside = bool(FD_SECTION_RE.search(line))
            continue
        if inside:
            keep.add(i)
    return keep


def event_title(desc: str) -> str:
    """Identity stem for uncategorised lines: first normalised words, no dates/numbers."""
    s = re.sub(r"\d[\d/\-.,:%$']*", " ", desc.lower())
    s = re.sub(r"[^\w一-鿿]+", " ", s)
    return " ".join(s.split()[:4])


def extract_for_ticker(ticker: str, scan_date: date) -> list[dict]:
    base = _DBASE / scan_date.isoformat() / ticker
    if not base.exists():
        return []
    fd_text = (base / "final_decision.md").read_text(encoding="utf-8", errors="ignore") \
        if (base / "final_decision.md").exists() else ""
    verdict = parse_verdict(fd_text)
    fd_lines = fd_fact_lines(fd_text)

    found = {}   # event_key -> record
    for fname, prio in FACT_FILES.items():
        f = base / fname
        if not f.exists():
            continue
        for lineno, line in enumerate(f.read_text(encoding="utf-8", errors="ignore").splitlines(), 1):
            if fname == "final_decision.md" and lineno not in fd_lines:
                continue
            for pat in DATE_PATTERNS:
                for m in pat.finditer(line):
                    iso, prec = parse_date(m.group(1), scan_date)
                    if not iso:
                        continue
                    desc = line.strip()
                    if len(desc) > 300:
                        desc = line[max(0, m.start() - 80):m.start() + 220].strip()
                    cat, sub = classify(desc, with_subtype=True)
                    # identity: ticker + day + type + event word; free-text stem only for "other"
                    key = f"{ticker}|{iso}|{cat}|{sub or event_title(desc)}"
                    rec = {
                        "ticker": ticker, "sector": TICKER_TO_SECTOR.get(ticker, "unknown"),
                        "date": iso, "date_precision": prec, "category": cat,
                        "description": desc, "source": f"{ticker}/{fname}:{lineno}",
                        "source_role": "fact", "event_key": key,
                        "scan_date": scan_date.isoformat(),
                        "current_verdict": verdict, "current_verdict_scan_date": scan_date.isoformat(),
                        "verdict": verdict, "trigger_kind": "event", "_prio": prio,
                    }
                    old = found.get(key)
                    # canonical = higher-priority source, then the fuller description
                    if old is None or (rec["_prio"], -len(desc)) < (old["_prio"], -len(old["description"])):
                        found[key] = rec
    out = []
    for r in found.values():
        r.pop("_prio", None)
        out.append(r)
    return out


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--as-of", default=None, help="YYYY-MM-DD: use each ticker's latest scan on/before this day")
    p.add_argument("--out", default=str(OUT), type=Path)
    args = p.parse_args()
    as_of = date.fromisoformat(args.as_of) if args.as_of else datetime.now(TPE).date()

    all_cats, scan_dates = [], {}
    for tk in TICKER_TO_SECTOR:
        sd = latest_scan_for_ticker(tk, as_of)
        if not sd:
            continue
        scan_dates[tk] = sd
        all_cats.extend(extract_for_ticker(tk, date.fromisoformat(sd)))
    all_cats.sort(key=lambda c: (c["date"], c["ticker"]))

    by_date = defaultdict(list)
    for c in all_cats:
        by_date[c["date"]].append(c)
    out = {
        "generated_at": datetime.now(TPE).isoformat(timespec="seconds"),
        "as_of": as_of.isoformat(),
        "scan_date": max(scan_dates.values()) if scan_dates else None,   # newest scan used (compat)
        "scan_dates": scan_dates,                                        # per ticker
        "tickers_covered": len(scan_dates),
        "total": len(all_cats),
        "by_date": dict(by_date),
        "all": all_cats,
    }
    args.out.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"extracted {len(all_cats)} catalysts for {len(scan_dates)} tickers across {len(by_date)} dates → {args.out}")


if __name__ == "__main__":
    main()
