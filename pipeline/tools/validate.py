#!/usr/bin/env python3
"""
Post-scan validator — run after every scan/build to confirm the output is in the
correct shape. Checks:

  1. Top-20 LEVELS: for each Top-20 ticker, Entry/Stop/T1/T2 must all derive to
     numbers (from entry+stop+R:R). Flags empty / non-derivable / 'x'-ratio rows.
  2. PRICE SANITY: parsed entry midpoint vs live price (cnyes/yf). If the entry
     is >SANITY_PCT off the real price, flag as likely hallucinated (the FN 7/8
     case: $685 entry while the stock was ~$470 — Yahoo 403 → made-up levels).
  3. VERDICT shape: verdict ∈ {BUY,HOLD,SELL,UNKNOWN}.

Writes validation.json at the repo root and prints a report. Exit code = number
of ERROR-level issues (0 = clean) so the scan routine can react.

Run: TRADING_SCANS_ROOT=<repo> python3 pipeline/tools/validate.py [--date DATE]
Env: SANITY_PCT (default 40 — entry within ±40% of live price)
"""
import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_dashboard as bd  # reuse collect_payload/compute_top20/derive_targets

ROOT = Path(os.environ.get("TRADING_SCANS_ROOT") or Path(__file__).resolve().parents[2])
TOOLS = Path(__file__).resolve().parent
SANITY_PCT = float(os.environ.get("SANITY_PCT", "40"))


# "無即時" stem covers 無即時報價 / 無即時價格 / 無即時行情 (all = no real-time price).
_PP_PHRASES = ("PRICE_DATA_UNAVAILABLE", "無即時", "暫不給進出場", "無法計算", "不設固定價位")


def _price_pending(scan_date, ticker):
    """True if the ticker's final_decision.md declined to give levels for lack of a
    real-time price (guarded behaviour), rather than genuinely missing levels."""
    if not scan_date:
        return False
    fd = ROOT / "daily" / scan_date / ticker / "final_decision.md"
    try:
        txt = fd.read_text(encoding="utf-8")
    except Exception:
        return False
    return any(s in txt for s in _PP_PHRASES)


def live_price(ticker):
    """Live price via the yf.py CLI (cnyes-primary). None on failure."""
    try:
        out = subprocess.run(
            [sys.executable, str(TOOLS / "yf.py"), ticker, "fast_info"],
            capture_output=True, text=True, timeout=30)
        d = json.loads(out.stdout or "{}")
        p = d.get("last_price")
        return float(p) if p else None
    except Exception:
        return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default=None, help="only validate this scan date (else all in Top 20)")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    payload = bd.collect_payload()
    top = bd.compute_top20(payload["sectors"])
    if args.date:
        top = [t for t in top if t.get("scan_date") == args.date]

    issues = []   # {level, ticker, msg}
    checked = 0
    for t in top:
        tk = t["ticker"]; v = t.get("verdict", "?"); p1 = t.get("phase1_only")
        sec = t.get("sector", "")
        checked += 1
        # 3. verdict shape
        if v not in ("BUY", "HOLD", "SELL", "UNKNOWN"):
            issues.append({"level": "WARN", "ticker": tk, "sector": sec, "msg": f"verdict 異常 '{v}'"})

        emid, snum, ct1, ct2 = bd.derive_targets(t.get("entry"), t.get("stop"), t.get("rr_t2"))
        # 1. levels — only demand full levels for actionable (non-Phase1) BUY/SELL
        actionable = (not p1) and v in ("BUY", "SELL")
        missing = [n for n, x in (("entry", emid), ("stop", snum),
                                  ("T1", ct1), ("T2", ct2)) if x is None]
        # PRICE_PENDING: the analyst correctly DECLINED to invent levels because no
        # real-time price was available at scan time (transient source outage). This
        # is the intended guarded behaviour, NOT a defect — flag WARN (價格待補) not
        # ERROR, and queue the sector for a re-scan once the price source is back up.
        # The parsed entry/stop fields come back empty in this case, so read the
        # source final_decision.md directly for the guard phrases (authoritative).
        price_pending = _price_pending(t.get("scan_date"), tk)
        if missing:
            if price_pending:
                issues.append({"level": "WARN", "ticker": tk, "sector": sec,
                               "price_pending": True,
                               "msg": f"價格待補（掃描時無報價，待重掃補值）rr={t.get('rr_t2')}"})
            elif actionable:
                issues.append({"level": "ERROR", "ticker": tk, "sector": sec,
                               "msg": f"缺 {'/'.join(missing)} (rr={t.get('rr_t2')})"})
            else:
                issues.append({"level": "INFO", "ticker": tk, "sector": sec,
                               "msg": f"缺 {'/'.join(missing)} (rr={t.get('rr_t2')})"})

        # 2. price sanity
        if emid is not None:
            lp = live_price(tk)
            if lp:
                off = abs(emid / lp - 1) * 100
                if off > SANITY_PCT:
                    issues.append({"level": "ERROR", "ticker": tk, "sector": sec,
                                   "msg": f"進場價 {emid:g} 與現價 {lp:g} 差 {off:.0f}% "
                                          f"(疑似幻想價/403)"})

    # 4. Serenity digest freshness — flag if newest strategy_*.md older than today
    from datetime import date as _date
    sdir = ROOT / "serenity"
    sfiles = sorted(sdir.glob("strategy_*.md")) if sdir.is_dir() else []
    ser_date = sfiles[-1].stem.replace("strategy_", "") if sfiles else ""
    if not ser_date:
        issues.append({"level": "WARN", "ticker": "SERENITY", "sector": "serenity",
                       "msg": "無每日觀點摘要"})
    elif ser_date < _date.today().isoformat():
        issues.append({"level": "WARN", "ticker": "SERENITY", "sector": "serenity",
                       "msg": f"每日觀點摘要過期 (最新 {ser_date})"})

    errors = [i for i in issues if i["level"] == "ERROR"]
    warns = [i for i in issues if i["level"] == "WARN"]

    # Queue for re-scan the SECTORS of (a) ERROR tickers (real defect: missing levels
    # while price WAS available / hallucinated price) AND (b) price_pending tickers
    # (no price at scan time — re-scan once the source is back up fills real levels).
    # Both self-heal via the next backfill; price_pending is WARN, not an alarm.
    pending_issues = errors + [i for i in warns if i.get("price_pending")]
    bad_secs = sorted({i["sector"] for i in pending_issues if i.get("sector")})
    if bad_secs:
        try:
            subprocess.run([sys.executable, str(TOOLS / "pending.py"), "add", *bad_secs],
                           capture_output=True, text=True, timeout=15)
        except Exception:
            pass
    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "date_filter": args.date, "checked": checked,
        "errors": len(errors), "warnings": len(warns),
        "price_pending": len([i for i in warns if i.get("price_pending")]),
        "issues": issues,
    }
    (ROOT / "validation.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    if not args.quiet:
        print(f"validate: {checked} Top-20 tickers · {len(errors)} ERROR · {len(warns)} WARN")
        for i in issues:
            mark = {"ERROR": "❌", "WARN": "⚠️", "INFO": "·"}.get(i["level"], " ")
            print(f"  {mark} {i['ticker']:8} {i['msg']}")
    sys.exit(len(errors))


if __name__ == "__main__":
    main()
