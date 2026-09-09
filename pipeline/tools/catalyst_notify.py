#!/usr/bin/env python3
"""
Catalyst notifier v3 — single consolidated briefing.

Behaviour:
1. Reads /Users/yht/Study/scans/_catalysts.json (refreshed by extract_catalysts.py).
2. Filters: only actionable categories (earnings / regulatory / corporate / macro).
   Skips category=='other' (mostly false positives).
3. Dedupes per event_key (ticker + date + type + normalised title), so two
   real events on one day both survive and a long analyst paragraph never
   outranks a short factual line.
4. Renders ONE briefing HTML at /Users/yht/Study/scans/daily_briefing.html:
     TODAY → NEXT N DAYS (exact-day events only) → LATER WATCH (quarter-precision)
     → RECENTLY PASSED (collapsed; last 3 days open, --lookback days inside).
   Verdicts are shown as "Current: BUY (scan …)" — the latest scan's view, not
   the view on the event date. Header states the calendar's source scan time;
   a calendar older than --max-stale-days is flagged and never notified as normal.
5. Auto-opens the briefing HTML in browser (once per day unless --no-open).
6. Sends ONE macOS notification summarising new upcoming events.
7. seen.json prevents repeat notifications for the same (day, event-count) combo.

Usage:
  catalyst_notify.py                        # lookback 14d, lookahead 3d
  catalyst_notify.py --lookahead 5
  catalyst_notify.py --lookback 7
  catalyst_notify.py --refresh              # re-run extractor first
  catalyst_notify.py --silent               # skip notification, still open
  catalyst_notify.py --no-open              # skip auto-open

Schedule via ~/Library/LaunchAgents/com.yht.trading-catalyst-notify.plist
"""
import argparse
import html
import json
import re
import subprocess
import sys
from collections import defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

TPE = ZoneInfo("Asia/Taipei")

SCANS = Path("/Users/yht/Study/scans")
CAT = SCANS / "_catalysts.json"
SEEN = SCANS / "_catalysts_seen.json"
BRIEFING_PATH = SCANS / "daily_briefing.html"   # fixed path, updated in-place
EXTRACTOR = Path.home() / ".claude/tools/trading/extract_catalysts.py"
PY = Path.home() / ".claude/tools/trading/venv/bin/python"

ACTIONABLE_CATEGORIES = {"earnings", "regulatory", "corporate", "macro"}

CATEGORY_EMOJI = {
    "earnings":   "💰",
    "regulatory": "⚖️",
    "corporate":  "🏢",
    "macro":      "🌐",
    "other":      "📌",
}

CATEGORY_LABEL = {
    "earnings":   "財報",
    "regulatory": "監管",
    "corporate":  "公司事件",
    "macro":      "總體",
    "other":      "其他",
}


def notify(title: str, msg: str, subtitle: str = "", sound: str = "Glass") -> None:
    args = [f'display notification "{msg}" with title "{title}"']
    if subtitle:
        args.append(f'subtitle "{subtitle}"')
    args.append(f'sound name "{sound}"')
    script = " ".join(args)
    try:
        subprocess.run(["osascript", "-e", script], check=False, timeout=10)
    except Exception as e:
        print(f"notify failed: {e}", file=sys.stderr)


def open_file(path: Path) -> None:
    try:
        subprocess.run(["open", str(path)], check=False, timeout=10)
    except Exception:
        pass


def shorten(text: str, n: int = 200) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    return text if len(text) <= n else text[:n - 1] + "…"


def is_meta_line(desc: str) -> bool:
    """Filter out lines that are clearly template metadata / table headers."""
    s = desc.strip().lower()
    junk_markers = [
        "investment plan", "research manager", "trade card", "trade proposal",
        "final decision", "risk debate", "phase 1", "phase 2", "phase 3", "phase 4",
        "ranking table", "verdict",
        "投資計劃", "投資計畫", "交易計劃", "交易提案", "最終決議", "風險辯論",
        "排名表", "判決",
    ]
    return any(m in s for m in junk_markers)


def date_label(dt_iso: str, today: date) -> str:
    """Human-readable date label relative to today."""
    d = date.fromisoformat(dt_iso)
    delta = (d - today).days
    if delta == 0:
        return f"今日 · {dt_iso}"
    elif delta == 1:
        return f"明日 · {dt_iso}"
    elif delta == -1:
        return f"昨日 · {dt_iso}"
    elif delta > 1:
        return f"{delta} 天後 · {dt_iso}"
    else:
        return f"{abs(delta)} 天前 · {dt_iso}"


def event_card(e: dict, muted: bool = False) -> str:
    cat = e.get("category", "other")
    verdict = e.get("current_verdict") or e.get("verdict", "UNKNOWN")
    vscan = e.get("current_verdict_scan_date") or e.get("scan_date") or ""
    prec = "" if e.get("date_precision", "exact_day") == "exact_day" else \
        ' <span class="prec">≈ 季度推估日期</span>'
    return f"""
            <div class="event {'opacity-75' if muted else ''}">
              <div class="event-header">
                <span class="emoji">{CATEGORY_EMOJI.get(cat, "📌")}</span>
                <span class="ticker">{html.escape(e['ticker'])}</span>
                <span class="cat">{CATEGORY_LABEL.get(cat, cat)}</span>
                <span class="verdict v-{verdict}" title="最新 scan 的看法,不是事件當日的看法">Current: {verdict}{(' · scan ' + vscan) if vscan else ''}</span>{prec}
              </div>
              <p class="desc">{html.escape(shorten(e['description'], 400))}</p>
              <p class="source">📁 {html.escape(e.get('source', ''))}</p>
            </div>"""


def date_section(dt: str, events: list[dict], today: date) -> str:
    delta = (date.fromisoformat(dt) - today).days
    style, icon = (("border-blue-400", "📅") if delta == 0 else
                   ("border-emerald-400", "🔜") if delta > 0 else ("border-slate-300", "🗓️"))
    return f"""
        <section>
          <h2 class="date-h {style}">{icon} {date_label(dt, today)} · {len(events)} 個事件</h2>
          {''.join(event_card(e, muted=delta < 0) for e in events)}
        </section>"""


def render_briefing(upcoming, history, later, today, lookback, lookahead, out_path,
                    calendar_generated_at="", freshness_ok=True, coverage=""):
    """TODAY → NEXT N DAYS → LATER WATCH → RECENTLY PASSED (collapsed beyond 3 days)."""
    def grouped(events):
        by = defaultdict(list)
        for e in events:
            by[e["date"]].append(e)
        return by

    up_by, hist_by = grouped(upcoming), grouped(history)
    today_iso = today.isoformat()
    today_html = date_section(today_iso, up_by[today_iso], today) if up_by.get(today_iso) else \
        '<p class="text-slate-500 py-4">今日無精確日期事件。</p>'
    next_html = "".join(date_section(d, up_by[d], today) for d in sorted(up_by) if d > today_iso) or \
        '<p class="text-slate-500 py-4">未來 %d 天無精確日期事件。</p>' % lookahead
    later_html = "".join(f"""
            <div class="event"><div class="event-header"><span class="emoji">🗓️</span>
              <span class="ticker">{html.escape(e['ticker'])}</span>
              <span class="cat">{CATEGORY_LABEL.get(e.get('category'), '')}</span>
              <span class="prec">Q{(int(e['date'][5:7]) + 2) // 3} {e['date'][:4]} (日期未定)</span></div>
              <p class="desc">{html.escape(shorten(e['description'], 300))}</p>
              <p class="source">📁 {html.escape(e.get('source', ''))}</p></div>""" for e in later) or \
        '<p class="text-slate-500 py-4">無季度級事件。</p>'
    recent_dates = sorted(hist_by, reverse=True)
    open_dates, folded_dates = recent_dates[:3], recent_dates[3:]
    hist_html = "".join(date_section(d, hist_by[d], today) for d in open_dates)
    if folded_dates:
        hist_html += f"""
        <details class="mt-4"><summary class="cursor-pointer text-slate-600">
          再往前 {len(folded_dates)} 天 · {sum(len(hist_by[d]) for d in folded_dates)} 個事件(至 {lookback} 天前)</summary>
          {''.join(date_section(d, hist_by[d], today) for d in folded_dates)}
        </details>"""
    if not history:
        hist_html = '<p class="text-slate-500 py-4">近 %d 天無已過事件。</p>' % lookback

    fresh_html = (f'<span class="text-emerald-300">✅ current</span>' if freshness_ok else
                  f'<span class="bg-rose-600 text-white px-2 py-0.5 rounded font-bold">⚠️ CATALYST DATA STALE — last refresh {html.escape(calendar_generated_at[:16])}</span>')
    sections = [
        f'<h2 class="part">TODAY · {today_iso}</h2>{today_html}',
        f'<h2 class="part">NEXT {lookahead} DAYS</h2>{next_html}',
        f'<h2 class="part">LATER WATCH · 季度級,日期未定</h2>{later_html}',
        f'<h2 class="part">RECENTLY PASSED</h2>{hist_html}',
    ]
    window_start = (today - timedelta(days=lookback)).isoformat()
    window_end = (today + timedelta(days=lookahead)).isoformat()
    total = len(upcoming) + len(history)

    body = f"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<title>Trading Daily Briefing</title>
<script src="https://cdn.tailwindcss.com"></script>
<style>
  body {{ font-family: "PingFang TC", -apple-system, sans-serif; background: #f8fafc; }}
  .v-BUY {{ background: #dcfce7; color: #166534; }}
  .v-HOLD {{ background: #fef3c7; color: #92400e; }}
  .v-SELL {{ background: #fee2e2; color: #991b1b; }}
  .v-UNKNOWN {{ background: #f3f4f6; color: #374151; }}
  .event {{ background: white; border-radius: 8px; padding: 16px; margin: 10px 0; box-shadow: 0 1px 3px rgba(0,0,0,0.08); }}
  .event-header {{ display: flex; gap: 10px; align-items: center; margin-bottom: 8px; flex-wrap: wrap; }}
  .ticker {{ font-weight: 700; font-size: 1.2rem; padding: 2px 10px; border-radius: 4px; }}
  .cat {{ background: #e0e7ff; color: #3730a3; padding: 2px 8px; border-radius: 4px; font-size: 0.85rem; }}
  .verdict {{ padding: 2px 8px; border-radius: 4px; font-size: 0.85rem; font-weight: 600; }}
  .emoji {{ font-size: 1.4rem; }}
  .desc {{ color: #1f2937; line-height: 1.6; margin: 6px 0; }}
  .source {{ color: #6b7280; font-size: 0.8rem; }}
  .date-h {{ color: #0f172a; font-size: 1.3rem; font-weight: 700; margin: 24px 0 8px;
             padding-bottom: 6px; border-bottom-width: 2px; border-bottom-style: solid; }}
  .border-blue-400 {{ border-bottom-color: #60a5fa; }}
  .border-emerald-400 {{ border-bottom-color: #34d399; }}
  .border-slate-300 {{ border-bottom-color: #cbd5e1; }}
  h1 {{ font-size: 2rem; font-weight: 700; }}
  .opacity-75 {{ opacity: 0.75; }}
  .part {{ font-size: 1.05rem; font-weight: 800; letter-spacing: .08em; color: #334155; margin: 28px 0 4px; }}
  .prec {{ background: #fef9c3; color: #854d0e; padding: 2px 8px; border-radius: 4px; font-size: 0.8rem; }}
  .ticker {{ background: #e2e8f0; color: #0f172a; }}
</style>
</head>
<body class="text-slate-900">

<header class="bg-slate-900 text-white p-6">
  <div class="max-w-4xl mx-auto">
    <h1>📊 Trading Daily Briefing</h1>
    <p class="text-slate-300 text-sm mt-1">
      今日 (Asia/Taipei): {today} ·
      顯示 {window_start} → {window_end} ·
      共 {total} 事件 ({len(upcoming)} 即將 / {len(history)} 歷史 / {len(later)} 季度級)
    </p>
    <p class="text-slate-300 text-xs mt-1">
      Calendar source: {html.escape(calendar_generated_at[:16])} · {coverage} · Freshness: {fresh_html}
    </p>
    <div class="text-xs text-slate-400 mt-2 flex gap-3">
      <a href="./dashboard.html" class="hover:underline text-blue-300">📊 Dashboard</a>
      <a href="./SECTOR_OVERVIEWS.html" class="hover:underline text-blue-300">📖 Sector overviews</a>
      <a href="./HOWTO_READ.html" class="hover:underline text-blue-300">📘 閱讀指南</a>
    </div>
  </div>
</header>

<main class="max-w-4xl mx-auto p-6">
  {''.join(sections)}
</main>

<footer class="text-center text-xs text-slate-500 p-6">
  更新於 {datetime.now(TPE).strftime('%Y-%m-%d %H:%M')} (台北) · 自動產生, 純研究用途 · verdict 為最新 scan 看法
</footer>

</body>
</html>
"""
    out_path.write_text(body, encoding="utf-8")


def dedup(events: list[dict]) -> list[dict]:
    """One record per event_key. Older calendars (no event_key) fall back to
    ticker+date+category. Never 'longest description wins'."""
    grouped: dict[str, dict] = {}
    for c in events:
        key = c.get("event_key") or f"{c['ticker']}|{c['date']}|{c.get('category')}"
        grouped.setdefault(key, c)
    return sorted(grouped.values(), key=lambda c: (c["date"], c["ticker"]))


def select_events(records, today: date, lookahead: int, lookback: int):
    """(upcoming exact-day, recent-past exact-day, later quarter-precision) — all actionable, deduped."""
    def keep(c):
        return c.get("category") in ACTIONABLE_CATEGORIES and not is_meta_line(c.get("description", ""))
    exact = [c for c in records if keep(c) and c.get("date_precision", "exact_day") == "exact_day"]
    horizon, start = (today + timedelta(days=lookahead)).isoformat(), (today - timedelta(days=lookback)).isoformat()
    upcoming = dedup([c for c in exact if today.isoformat() <= c["date"] <= horizon])
    history = dedup([c for c in exact if start <= c["date"] < today.isoformat()])
    later = dedup([c for c in records if keep(c) and c.get("date_precision") == "quarter"
                   and c["date"] >= today.isoformat()])[:40]
    return upcoming, history, later


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--lookahead", type=int, default=3,
                   help="days ahead to show (default 3)")
    p.add_argument("--lookback", type=int, default=14,
                   help="days back to show as history (default 14)")
    p.add_argument("--refresh", action="store_true",
                   help="re-run extractor first")
    p.add_argument("--silent", action="store_true",
                   help="skip macOS notification but still render + open")
    p.add_argument("--no-open", action="store_true",
                   help="don't auto-open briefing in browser")
    p.add_argument("--max-stale-days", type=int, default=1,
                   help="calendar older than this is flagged STALE and not notified (default 1)")
    p.add_argument("--today", default=None, help="override today (YYYY-MM-DD, tests)")
    args = p.parse_args()

    if args.refresh or not CAT.exists():
        if EXTRACTOR.exists() and PY.exists():
            subprocess.run([str(PY), str(EXTRACTOR)], check=True)

    if not CAT.exists():
        print(f"no catalyst file at {CAT}", file=sys.stderr)
        sys.exit(2)

    data = json.loads(CAT.read_text(encoding="utf-8"))
    today = date.fromisoformat(args.today) if args.today else datetime.now(TPE).date()
    horizon = today + timedelta(days=args.lookahead)
    lookback_start = today - timedelta(days=args.lookback)

    # Freshness: the calendar must have been regenerated within max_stale_days.
    gen = data.get("generated_at", "")
    try:
        gen_date = datetime.fromisoformat(gen).date()
    except ValueError:
        gen_date = None
    freshness_ok = gen_date is not None and (today - gen_date).days <= args.max_stale_days
    coverage = f"{data.get('tickers_covered', '?')} tickers · newest scan {data.get('scan_date', '?')}"

    upcoming, history, later = select_events(data["all"], today, args.lookahead, args.lookback)
    render_briefing(upcoming, history, later, today, args.lookback, args.lookahead, BRIEFING_PATH,
                    calendar_generated_at=gen, freshness_ok=freshness_ok, coverage=coverage)
    if not freshness_ok:
        print(f"WARNING: catalyst calendar stale (generated {gen or 'unknown'}); briefing flagged, no notification",
              file=sys.stderr)
        args.silent = True

    # Notification: once per (today, upcoming event count) to avoid spam
    # Only notify for upcoming events, not history
    seen: dict = {}
    if SEEN.exists():
        try:
            seen = json.loads(SEEN.read_text(encoding="utf-8"))
        except Exception:
            seen = {}

    notify_key = f"briefing|{today.isoformat()}|n={len(upcoming)}"
    already_notified = seen.get(notify_key) is not None

    if upcoming and not args.silent and not already_notified:
        tickers = sorted({c["ticker"] for c in upcoming})
        ticker_preview = ", ".join(tickers[:5])
        if len(tickers) > 5:
            ticker_preview += f" +{len(tickers) - 5}"
        title = f"📊 {len(upcoming)} 即將事件"
        subtitle = f"{today} → {horizon}"
        msg = f"{ticker_preview}. 已更新 briefing."
        notify(title, msg, subtitle=subtitle)
        seen[notify_key] = datetime.now().isoformat(timespec="seconds")
        SEEN.write_text(json.dumps(seen, ensure_ascii=False, indent=2), encoding="utf-8")

    # Auto-open: once per day regardless of event count
    open_key = f"opened|{today.isoformat()}"
    already_opened = seen.get(open_key) is not None
    if not args.no_open and not already_opened:
        open_file(BRIEFING_PATH)
        seen[open_key] = datetime.now().isoformat(timespec="seconds")
        SEEN.write_text(json.dumps(seen, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"briefing → {BRIEFING_PATH}")
    print(f"  upcoming: {len(upcoming)} events | history: {len(history)} events")
    if upcoming:
        print("  --- upcoming ---")
        for c in upcoming:
            print(f"  {c['date']} | {c['ticker']:7s} | {c['category']:10s} | {shorten(c['description'], 80)}")
    if history:
        print(f"  --- history (last {args.lookback}d) ---")
        for c in history[:10]:   # cap console output
            print(f"  {c['date']} | {c['ticker']:7s} | {c['category']:10s} | {shorten(c['description'], 80)}")
        if len(history) > 10:
            print(f"  ... +{len(history) - 10} more")


if __name__ == "__main__":
    main()
