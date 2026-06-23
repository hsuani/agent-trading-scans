#!/usr/bin/env python3
"""
L0 price monitor — ZERO LLM. Tracks already-locked trade levels against live
price so positions/setups can be followed daily without re-running the
expensive multi-agent scan (that stays weekly).

Watchlist = union of:
  - held positions           (pipeline/tools/held_tickers.txt)
  - actionable BUYs          (latest verdict BUY and R:R(T2) > RR_MIN)
  - catalyst-soon            (any ticker with a catalyst within CATALYST_DAYS)

For each, pulls live price (yfinance fast_info — free) and compares to the
entry zone / stop / T1 / T2 parsed from its most recent final_decision.md.
Emits alerts.json + alerts.html at the repo root. Designed to run as a GitHub
Action (no Claude usage, Mac need not be on).

Run: TRADING_SCANS_ROOT=<repo> python3 pipeline/tools/monitor.py
Env: RR_MIN (default 2.0), CATALYST_DAYS (5), NEAR_PCT (3.0)
"""
import json
import os
import re
import sys
from datetime import date, datetime, timezone
from pathlib import Path

import yfinance as yf

# Reuse the battle-tested parsers from the dashboard builder (same dir).
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_dashboard import parse_final_decision, collect_ticker_history  # noqa: E402

ROOT = Path(os.environ.get("TRADING_SCANS_ROOT") or Path(__file__).resolve().parents[2])
# Per-day scan output under daily/<date>/ (tolerate pre-migration root).
DAILY = ROOT / "daily"
_DBASE = DAILY if DAILY.is_dir() else ROOT
HELD_FILE = Path(__file__).resolve().parent / "held_tickers.txt"
CATALYSTS = ROOT / "_catalysts.json"

RR_MIN = float(os.environ.get("RR_MIN", "2.0"))
CATALYST_DAYS = int(os.environ.get("CATALYST_DAYS", "5"))
NEAR_PCT = float(os.environ.get("NEAR_PCT", "3.0"))

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def first_num(s: str):
    """First numeric value in a level string like '$220.00（MA50…）' -> 220.0."""
    if not s:
        return None
    m = re.search(r"-?\d+(?:\.\d+)?", s.replace(",", ""))
    return float(m.group()) if m else None


def zone(s: str):
    """Entry zone '$226.00 – $230.00（…）' -> (226.0, 230.0); single -> (x,x)."""
    if not s:
        return (None, None)
    nums = [float(x) for x in re.findall(r"-?\d+(?:\.\d+)?", s.replace(",", ""))]
    if not nums:
        return (None, None)
    return (nums[0], nums[1] if len(nums) > 1 else nums[0])


def all_tickers():
    """Every ticker that has at least one final_decision.md under a date dir."""
    seen = set()
    for d in _DBASE.iterdir():
        if not (d.is_dir() and DATE_RE.match(d.name)):
            continue
        for t in d.iterdir():
            if t.is_dir() and (t / "final_decision.md").exists():
                seen.add(t.name)
    return sorted(seen)


def latest_card(ticker):
    """Most recent parsed final_decision card for a ticker, or None."""
    hist = collect_ticker_history(ticker)
    if not hist:
        return None
    d = sorted(hist)[-1]
    card = dict(hist[d])
    card["scan_date"] = d
    return card


def rr_t2(card):
    """R:R to T2 for a long: (t2-entry_mid)/(entry_mid-stop). None if invalid."""
    lo, hi = zone(card.get("entry", ""))
    stop = first_num(card.get("stop", ""))
    t2 = first_num(card.get("t2", ""))
    if None in (lo, hi, stop, t2):
        return None
    entry = (lo + hi) / 2
    risk = entry - stop
    if risk <= 0:
        return None
    return (t2 - entry) / risk


def upcoming_catalysts():
    """{ticker: (date, desc)} nearest upcoming catalyst within CATALYST_DAYS."""
    out = {}
    if not CATALYSTS.exists():
        return out
    try:
        data = json.loads(CATALYSTS.read_text(encoding="utf-8"))
    except Exception:
        return out
    today = date.today().isoformat()
    horizon = (date.today().toordinal() + CATALYST_DAYS)
    for c in data.get("all", []):
        cd = c.get("date", "")
        if not DATE_RE.match(cd) or cd < today:
            continue
        try:
            if date.fromisoformat(cd).toordinal() > horizon:
                continue
        except ValueError:
            continue
        t = c.get("ticker")
        if t and (t not in out or cd < out[t][0]):
            out[t] = (cd, (c.get("description") or "")[:120])
    return out


def price(ticker):
    """Live last price via fast_info (free). None on failure."""
    try:
        fi = yf.Ticker(ticker).fast_info
        p = fi.get("last_price") or fi.get("lastPrice")
        return float(p) if p else None
    except Exception:
        return None


def status(card, px):
    """Classify live price vs locked levels. Returns (urgency, flag list)."""
    if px is None:
        return (5, ["no price"])
    lo, hi = zone(card.get("entry", ""))
    stop = first_num(card.get("stop", ""))
    t1 = first_num(card.get("t1", ""))
    t2 = first_num(card.get("t2", ""))
    flags, urg = [], 9
    if stop is not None:
        dpct = (px - stop) / stop * 100
        if px <= stop:
            flags.append("🔴 STOP BREACHED"); urg = min(urg, 0)
        elif 0 < dpct <= NEAR_PCT:
            flags.append(f"⚠ near stop ({dpct:+.1f}%)"); urg = min(urg, 1)
    if t2 is not None and px >= t2:
        flags.append("🎯 T2 HIT"); urg = min(urg, 1)
    elif t1 is not None and px >= t1:
        flags.append("🎯 T1 HIT"); urg = min(urg, 2)
    if lo is not None and hi is not None:
        if lo <= px <= hi:
            flags.append("🟢 IN ENTRY ZONE"); urg = min(urg, 1)
        elif px < lo:
            flags.append(f"⬇ below entry ({(px-lo)/lo*100:+.1f}%)"); urg = min(urg, 3)
    return (urg, flags or ["— in range"])


def main():
    held = set()
    if HELD_FILE.exists():
        for line in HELD_FILE.read_text(encoding="utf-8").splitlines():
            s = line.split("#", 1)[0].strip()
            if s:
                held.add(s)

    cats = upcoming_catalysts()
    cards = {}
    watch = {}  # ticker -> set of reasons

    for t in all_tickers():
        card = latest_card(t)
        if not card:
            continue
        cards[t] = card
        reasons = set()
        if t in held:
            reasons.add("held")
        rr = rr_t2(card)
        if card.get("verdict") == "BUY" and rr is not None and rr > RR_MIN:
            reasons.add(f"R:R {rr:.1f}")
        if t in cats:
            reasons.add(f"catalyst {cats[t][0]}")
        if reasons:
            watch[t] = (reasons, rr)

    # held tickers may lack a final_decision (e.g. ETF) — still watch by price
    for t in held - set(cards):
        watch[t] = ({"held"}, None)
        cards[t] = {"verdict": "?", "entry": "", "stop": "", "t1": "", "t2": "",
                    "scan_date": "—"}

    rows = []
    for t, (reasons, rr) in watch.items():
        card = cards[t]
        px = price(t)
        urg, flags = status(card, px)
        cat = cats.get(t)
        rows.append({
            "ticker": t, "verdict": card.get("verdict", "?"),
            "scan_date": card.get("scan_date", "—"),
            "price": px,
            "entry": card.get("entry", ""), "stop": card.get("stop", ""),
            "t1": card.get("t1", ""), "t2": card.get("t2", ""),
            "rr_t2": round(rr, 2) if rr else None,
            "reasons": sorted(reasons), "flags": flags, "urgency": urg,
            "catalyst": {"date": cat[0], "desc": cat[1]} if cat else None,
        })

    rows.sort(key=lambda r: (r["urgency"], r["ticker"]))
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "rr_min": RR_MIN, "catalyst_days": CATALYST_DAYS,
        "count": len(rows), "alerts": rows,
    }
    (ROOT / "alerts.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2),
                                      encoding="utf-8")
    (ROOT / "alerts.html").write_text(render(payload), encoding="utf-8")

    actionable = [r for r in rows if r["urgency"] <= 3]
    print(f"monitor: {len(rows)} watched, {len(actionable)} actionable "
          f"-> {ROOT/'alerts.html'}")
    for r in actionable:
        cs = f"  📅 {r['catalyst']['date']}" if r["catalyst"] else ""
        pxs = f"${r['price']:.2f}" if r["price"] else "n/a"
        print(f"  [{r['urgency']}] {r['ticker']:7} {pxs:>9}  "
              f"{' | '.join(r['flags'])}{cs}")


def render(p):
    head = (
        "<!DOCTYPE html><html lang='zh-Hant'><head><meta charset='utf-8'>"
        "<title>L0 Monitor — Alerts</title>"
        "<style>body{font-family:-apple-system,'PingFang TC',sans-serif;margin:24px;"
        "background:#0b0f17;color:#e5e7eb}table{border-collapse:collapse;width:100%}"
        "th,td{padding:6px 10px;border-bottom:1px solid #1f2937;text-align:left;font-size:13px}"
        "th{color:#9ca3af;font-weight:600}.u0{background:#3f1d1d}.u1{background:#3a2a14}"
        ".u2{background:#13324a}.u3{background:#14322a}.tk{font-weight:700}"
        "a{color:#60a5fa}</style></head><body>"
    )
    rows = []
    for r in p["alerts"]:
        cls = f"u{r['urgency']}" if r["urgency"] <= 3 else ""
        px = f"${r['price']:.2f}" if r["price"] else "—"
        cat = (f"{r['catalyst']['date']} {r['catalyst']['desc']}"
               if r["catalyst"] else "")
        rr = r["rr_t2"] if r["rr_t2"] is not None else ""
        rows.append(
            f"<tr class='{cls}'><td class='tk'>{r['ticker']}</td>"
            f"<td>{r['verdict']}</td><td>{px}</td>"
            f"<td>{' | '.join(r['flags'])}</td>"
            f"<td>{r['entry']}</td><td>{r['stop']}</td>"
            f"<td>{r['t1']}</td><td>{r['t2']}</td><td>{rr}</td>"
            f"<td>{', '.join(r['reasons'])}</td><td>{cat}</td></tr>"
        )
    return (
        head
        + f"<h2>L0 Monitor — {p['count']} watched "
          f"<small style='color:#9ca3af'>(R:R&gt;{p['rr_min']}, "
          f"catalyst&le;{p['catalyst_days']}d · {p['generated_at']} UTC)</small></h2>"
        + "<table><tr><th>Ticker</th><th>Verdict</th><th>Price</th><th>Status</th>"
          "<th>Entry</th><th>Stop</th><th>T1</th><th>T2</th><th>R:R(T2)</th>"
          "<th>Why</th><th>Catalyst</th></tr>"
        + "".join(rows) + "</table></body></html>"
    )


if __name__ == "__main__":
    main()
