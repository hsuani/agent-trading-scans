#!/usr/bin/env python3
"""1B KPIs over every daily/<date>/<ticker>/evidence_shadow.json.

  claims_per_ticker       is the grader missing most of the report?
  source_coverage         share of claims with a URL or a named source
  unknown_grade_rate      resolver too weak / analysts don't cite
  unsupported_claim_rate  claims with no source at all (RUMOR/UNKNOWN or nothing named)
  status_distribution     CONFIRMED / EXPECTED / RUMOR … sanity
  duplicate_claim_rate    1 - unique(evidence_key) / claims: same event counted as several signals (LLM keys)
  duplicate_by_source     same but grouped by normalised (source_name, source_date) — deterministic cross-check
  independent_evidence    per ticker: unique evidence keys / unique sources vs reported claims

    python3 pipeline/evidence/evidence_report.py [--since YYYY-MM-DD]  -> pipeline/evidence/EVIDENCE_REPORT.md
"""
import json
import sys
from collections import Counter
from datetime import date
from pathlib import Path
from statistics import median

ROOT = Path(__file__).resolve().parents[2]
STATUSES = ("CONFIRMED", "QUALIFIED", "SAMPLING", "EXPECTED", "RUMOR", "UNSUPPORTED", "UNKNOWN")


def source_id(c):
    """Deterministic document identity: normalised source name + date."""
    name = " ".join((c.get("source_name") or "").lower().split())
    return (name, c.get("source_date") or "") if name else None


def load(since=""):
    docs = []
    for f in sorted((ROOT / "daily").glob("*/*/evidence_shadow.json")):
        if f.parts[-3] >= since:
            try:
                d = json.loads(f.read_text(encoding="utf-8"))
            except json.JSONDecodeError as e:
                print(f"bad json {f}: {e}", file=sys.stderr); continue
            d["_ticker"], d["_date"] = f.parts[-2], f.parts[-3]
            docs.append(d)
    return docs


def kpis(docs):
    claims = [c for d in docs for c in d.get("claims", [])]
    n = len(claims)
    pct = lambda a: round(a / n, 3) if n else None  # noqa: E731
    per = [len(d.get("claims", [])) for d in docs]
    keys_per = [(len(d.get("claims", [])), len({c.get("evidence_key") for c in d.get("claims", [])}),
                 len({source_id(c) for c in d.get("claims", []) if source_id(c)}))
                for d in docs]
    return {
        "tickers": len(docs), "claims": n,
        "claims_per_ticker": {"median": median(per) if per else None, "min": min(per, default=None), "max": max(per, default=None)},
        "source_coverage": pct(sum(1 for c in claims if c.get("source_url") or c.get("source_name"))),
        "url_coverage": pct(sum(1 for c in claims if c.get("source_url"))),
        "unknown_grade_rate": pct(sum(1 for c in claims if c.get("source_grade", "UNKNOWN") == "UNKNOWN")),
        "unsupported_claim_rate": pct(sum(1 for c in claims if not (c.get("source_url") or c.get("source_name"))
                                          or c.get("claim_status") in ("RUMOR", "UNSUPPORTED", "UNKNOWN"))),
        "grade_distribution": dict(Counter(c.get("source_grade", "UNKNOWN") for c in claims)),
        "grade_basis": dict(Counter(c.get("grade_basis", "none") for c in claims)),
        "status_distribution": dict(Counter(c.get("claim_status", "UNKNOWN") for c in claims)),
        "duplicate_claim_rate": pct(n - sum(u for _, u, _ in keys_per)),
        "duplicate_by_source": pct(n - sum(s for _, _, s in keys_per)),
        "independent_evidence": {f"{d['_ticker']}@{d['_date']}": {"claims": c, "unique_keys": u, "unique_sources": s}
                                 for d, (c, u, s) in zip(docs, keys_per)},
        "by_origin_agent": dict(Counter(c.get("origin_agent") for c in claims)),
        "grade_x_status": dict(Counter(f"{c.get('source_grade', '?')}/{c.get('claim_status', '?')}" for c in claims)),
    }


def main():
    since = sys.argv[sys.argv.index("--since") + 1] if "--since" in sys.argv else ""
    docs = load(since)
    k = kpis(docs)
    lines = [f"# Evidence shadow report — {date.today().isoformat()}", "",
             f"{k['tickers']} tickers · {k['claims']} claims" + (f" · since {since}" if since else ""), "",
             "| KPI | value |", "|---|---|"]
    for key in ("claims_per_ticker", "source_coverage", "url_coverage", "unknown_grade_rate",
                "unsupported_claim_rate", "duplicate_claim_rate", "duplicate_by_source", "grade_distribution", "grade_basis",
                "status_distribution", "by_origin_agent"):
        lines.append(f"| {key} | {json.dumps(k[key], ensure_ascii=False)} |")
    lines += ["", "## grade × status (should NOT collapse to A→CONFIRMED)", "",
              "| cell | n |", "|---|---|"] + [f"| {c} | {v} |" for c, v in sorted(k["grade_x_status"].items())]
    lines += ["", "## independent evidence per ticker", "", "| ticker | claims | unique evidence keys (LLM) | unique sources (name+date) |", "|---|---|---|---|"]
    lines += [f"| {t} | {v['claims']} | {v['unique_keys']} | {v['unique_sources']} |" for t, v in k["independent_evidence"].items()]
    out = ROOT / "pipeline" / "evidence" / "EVIDENCE_REPORT.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
