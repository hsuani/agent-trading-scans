#!/usr/bin/env python3
"""1B calibration helpers — zero LLM.

  regression  compare the current evidence_shadow.json set against a git ref
              (claims / unique keys / unique sources / UNSUPPORTED per ticker)
  sample      build a labelling sheet of ~N claims for manual VALID / INVALID and
              UNSUPPORTED correctness judgement, stratified so the challenge
              cases are in: every UNSUPPORTED claim (cap 30), every claim whose
              wording looks like an estimate but is NOT labelled UNSUPPORTED
              (recall candidates, cap 20), the rest random. Each row carries
              the closest line of the source report so the judge does not have
              to open four files.
  determinism run source_grades + evidence_report twice, assert identical.

    python3 pipeline/evidence/calibration.py regression 040c3be8a
    python3 pipeline/evidence/calibration.py sample --n 100 --seed 7  -> pipeline/evidence/CALIBRATION_SHEET.md
    python3 pipeline/evidence/calibration.py determinism
"""
import difflib
import hashlib
import json
import random
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from evidence_report import ROOT, load, kpis, source_id  # noqa: E402

ESTIMATE_RE = re.compile(r"預估|估計|推估|估值|合理|可能|應該|預期|我們認為|我們預|likely|we (estimate|expect|believe|think)|"
                         r"implied|fair value|could|should|upside|downside|assum", re.I)


def per_ticker(docs):
    out = {}
    for d in docs:
        cl = d.get("claims", [])
        out[f"{d['_ticker']}@{d['_date']}"] = {
            "claims": len(cl), "keys": len({c.get("evidence_key") for c in cl}),
            "sources": len({source_id(c) for c in cl if source_id(c)}),
            "unsupported": sum(c.get("claim_status") == "UNSUPPORTED" for c in cl),
            "unknown": sum(c.get("source_grade", "UNKNOWN") == "UNKNOWN" for c in cl),
        }
    return out


def load_ref(ref):
    """evidence_shadow.json docs as they were at a git ref."""
    files = subprocess.run(["git", "ls-tree", "-r", "--name-only", ref, "daily"], cwd=ROOT,
                           capture_output=True, text=True).stdout.split()
    docs = []
    for f in files:
        if f.endswith("evidence_shadow.json"):
            txt = subprocess.run(["git", "show", f"{ref}:{f}"], cwd=ROOT, capture_output=True, text=True).stdout
            d = json.loads(txt)
            d["_ticker"], d["_date"] = f.split("/")[2], f.split("/")[1]
            docs.append(d)
    return docs


def regression(ref):
    now, old = per_ticker(load()), per_ticker(load_ref(ref))
    rows = ["| ticker | claims r1→r2 | keys r1→r2 | claims/keys r2 | sources r2 | UNSUPPORTED r1→r2 | UNKNOWN r1→r2 |", "|---|---|---|---|---|---|---|"]
    for k in sorted(now):
        n, o = now[k], old.get(k, {})
        g = lambda d, f: d.get(f, "—")  # noqa: E731
        ratio = round(n["claims"] / n["keys"], 2) if n["keys"] else "—"
        rows.append(f"| {k} | {g(o,'claims')}→{n['claims']} | {g(o,'keys')}→{n['keys']} | {ratio} | {n['sources']} | "
                    f"{g(o,'unsupported')}→{n['unsupported']} | {g(o,'unknown')}→{n['unknown']} |")
    return "\n".join(rows)


def closest_line(claim, ticker, date, origin):
    f = ROOT / "daily" / date / ticker / f"{origin}.md"
    if not f.exists():
        return ""
    lines = [l.strip() for l in f.read_text(encoding="utf-8", errors="ignore").splitlines() if l.strip()]
    best = max(lines, key=lambda l: difflib.SequenceMatcher(None, claim[:120], l[:200]).ratio(), default="")
    return best[:220]


def sample(n, seed, tickers=None, unsupported_only=False, out_name="CALIBRATION_SHEET.md"):
    rng = random.Random(seed)
    docs = [d for d in load() if not tickers or d["_ticker"] in tickers]
    allc = [(d, c) for d in docs for c in d.get("claims", [])]
    if unsupported_only:
        allc = [x for x in allc if x[1].get("claim_status") == "UNSUPPORTED"]
        n = len(allc)
    uns = [x for x in allc if x[1].get("claim_status") == "UNSUPPORTED"]
    recall = [x for x in allc if x[1].get("claim_status") != "UNSUPPORTED" and ESTIMATE_RE.search(x[1].get("claim", ""))
              and (x[1].get("source_name", "").lower() in ("", "analyst") or x[1].get("source_grade") == "UNKNOWN")]
    rng.shuffle(uns); rng.shuffle(recall)
    chosen = (uns if unsupported_only else uns[:30]) + ([] if unsupported_only else recall[:20])
    rest = [x for x in allc if x not in chosen]
    rng.shuffle(rest)
    chosen += rest[: max(0, n - len(chosen))]
    lines = [f"# Evidence-shadow calibration sheet — {len(chosen)} claims (seed {seed})", "",
             "Judge each row on TWO questions, write V/I in `extract` (claim faithfully present in the report, meaning not "
             "distorted) and, for the status column, whether `UNSUPPORTED` is right / missing (U-ok / U-miss / U-wrong / n.a.).",
             f"Strata: {min(len(uns),30)} UNSUPPORTED (precision), {min(len(recall),20)} estimate-looking non-UNSUPPORTED "
             f"(recall candidates), {len(chosen) - min(len(uns),30) - min(len(recall),20)} random.", "",
             "| # | ticker | agent | status | grade | source_name | claim | closest report line | extract | status-judge |",
             "|---|---|---|---|---|---|---|---|---|---|"]
    for i, (d, c) in enumerate(chosen, 1):
        esc = lambda s: str(s).replace("|", "\\|").replace("\n", " ")  # noqa: E731
        lines.append(f"| {i} | {d['_ticker']} | {c.get('origin_agent','')} | {c.get('claim_status','')} | {c.get('source_grade','')} | "
                     f"{esc(c.get('source_name',''))[:30]} | {esc(c.get('claim',''))[:160]} | "
                     f"{esc(closest_line(c.get('claim',''), d['_ticker'], d['_date'], c.get('origin_agent','news')))} |  |  |")
    out = ROOT / "pipeline" / "evidence" / out_name
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out, len(chosen), min(len(uns), 30), min(len(recall), 20)


def determinism():
    files = sorted((ROOT / "daily").glob("*/*/evidence_shadow.json"))
    def digest():
        subprocess.run([sys.executable, str(ROOT / "pipeline/evidence/source_grades.py"), *map(str, files)],
                       capture_output=True, check=True)
        h = hashlib.sha256()
        for f in files:
            h.update(f.read_bytes())
        k = json.dumps(kpis(load()), sort_keys=True, ensure_ascii=False)
        return h.hexdigest(), hashlib.sha256(k.encode()).hexdigest()
    a, b = digest(), digest()
    return a == b, a


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "regression":
        print(regression(sys.argv[2]))
    elif cmd == "sample":
        n = int(sys.argv[sys.argv.index("--n") + 1]) if "--n" in sys.argv else 100
        seed = int(sys.argv[sys.argv.index("--seed") + 1]) if "--seed" in sys.argv else 7
        tk = sys.argv[sys.argv.index("--tickers") + 1].split(",") if "--tickers" in sys.argv else None
        name = sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else "CALIBRATION_SHEET.md"
        out, total, u, r = sample(n, seed, tk, "--unsupported-only" in sys.argv, name)
        print(f"{total} rows ({u} UNSUPPORTED, {r} recall candidates) -> {out}")
    elif cmd == "determinism":
        ok, h = determinism()
        print("deterministic" if ok else "NON-DETERMINISTIC", h)
