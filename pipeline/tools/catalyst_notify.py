#!/usr/bin/env python3
"""
Catalyst notifier v3 — single consolidated briefing.

Behaviour:
1. Reads /Users/yht/Study/scans/_catalysts.json (refreshed by extract_catalysts.py).
2. Filters: only actionable categories (earnings / regulatory / corporate / macro).
   Skips category=='other' (mostly false positives).
3. Dedupes per (ticker, date) → 1 record (keeps longest description).
4. Renders ONE briefing HTML at /Users/yht/Study/scans/daily_briefing.html
   — fixed path, updated in-place on every run.
   — shows rolling window: past --lookback days + upcoming --lookahead days.
   — dates grouped descending (upcoming first, then today, then history).
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


def render_briefing(
    upcoming: list[dict],
    history: list[dict],
    today: date,
    lookback: int,
    lookahead: int,
    out_path: Path,
) -> None:
    """Write consolidated briefing HTML.

    Layout (date descending — most actionable at top):
      Upcoming (today → lookahead) — highlighted
      History (yesterday → lookback) — muted
    """
    all_events = upcoming + history
    by_date: dict[str, list] = defaultdict(list)
    for e in all_events:
        by_date[e["date"]].append(e)

    # Sort dates: upcoming first (ascending), then past (descending)
    upcoming_dates = sorted(
        [d for d in by_date if d >= today.isoformat()],
    )
    past_dates = sorted(
        [d for d in by_date if d < today.isoformat()],
        reverse=True,
    )
    ordered_dates = upcoming_dates + past_dates

    sections = []
    for dt in ordered_dates:
        is_future = dt >= today.isoformat()
        d = date.fromisoformat(dt)
        delta = (d - today).days
        label = date_label(dt, today)

        # Section header style
        if delta == 0:
            header_extra = "border-blue-400"
            icon = "📅"
        elif delta > 0:
            header_extra = "border-emerald-400"
            icon = "🔜"
        else:
            header_extra = "border-slate-300"
            icon = "🗓️"

        cards = []
        for e in by_date[dt]:
            cat = e.get("category", "other")
            emoji = CATEGORY_EMOJI.get(cat, "📌")
            label_cat = CATEGORY_LABEL.get(cat, cat)
            verdict = e.get("verdict", "UNKNOWN")

            # Mute past events slightly
            opacity = "" if is_future else "opacity-75"
            cards.append(f"""
            <div class="event {opacity}">
              <div class="event-header">
                <span class="emoji">{emoji}</span>
                <span class="ticker v-{verdict}">{html.escape(e['ticker'])}</span>
                <span class="cat">{label_cat}</span>
                <span class="verdict v-{verdict}">{verdict}</span>
              </div>
              <p class="desc">{html.escape(shorten(e['description'], 400))}</p>
              <p class="source">📁 {html.escape(e.get('source', ''))}</p>
            </div>
            """)

        sections.append(f"""
        <section>
          <h2 class="date-h {header_extra}">{icon} {label} · {len(by_date[dt])} 個事件</h2>
          {''.join(cards)}
        </section>
        """)

    window_start = (today - timedelta(days=lookback)).isoformat()
    window_end = (today + timedelta(days=lookahead)).isoformat()
    total = len(all_events)

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
</style>
</head>
<body class="text-slate-900">

<header class="bg-slate-900 text-white p-6">
  <div class="max-w-4xl mx-auto">
    <h1>📊 Trading Daily Briefing</h1>
    <p class="text-slate-300 text-sm mt-1">
      今日: {today} ·
      顯示 {window_start} → {window_end} ·
      共 {total} 事件 ({len(upcoming)} 即將 / {len(history)} 歷史)
    </p>
    <div class="text-xs text-slate-400 mt-2 flex gap-3">
      <a href="./dashboard.html" class="hover:underline text-blue-300">📊 Dashboard</a>
      <a href="./SECTOR_OVERVIEWS.html" class="hover:underline text-blue-300">📖 Sector overviews</a>
      <a href="./HOWTO_READ.html" class="hover:underline text-blue-300">📘 閱讀指南</a>
    </div>
  </div>
</header>

<main class="max-w-4xl mx-auto p-6">
  {''.join(sections) if sections else '<p class="text-slate-500 text-center py-12">無 actionable 事件 (window 內)。</p>'}
</main>

<footer class="text-center text-xs text-slate-500 p-6">
  更新於 {datetime.now().strftime('%Y-%m-%d %H:%M')} · 自動產生, 純研究用途
</footer>

</body>
</html>
"""
    out_path.write_text(body, encoding="utf-8")


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
    args = p.parse_args()

    if args.refresh or not CAT.exists():
        if EXTRACTOR.exists() and PY.exists():
            subprocess.run([str(PY), str(EXTRACTOR)], check=True)

    if not CAT.exists():
        print(f"no catalyst file at {CAT}", file=sys.stderr)
        sys.exit(2)

    data = json.loads(CAT.read_text(encoding="utf-8"))
    today = date.today()
    horizon = today + timedelta(days=args.lookahead)
    lookback_start = today - timedelta(days=args.lookback)

    def keep(c: dict) -> bool:
        if c.get("category") not in ACTIONABLE_CATEGORIES:
            return False
        if is_meta_line(c.get("description", "")):
            return False
        return True

    def dedup(events: list[dict]) -> list[dict]:
        grouped: dict[tuple, dict] = {}
        for c in events:
            key = (c["ticker"], c["date"])
            if key not in grouped or len(c["description"]) > len(grouped[key]["description"]):
                grouped[key] = c
        return sorted(grouped.values(), key=lambda c: (c["date"], c["ticker"]))

    # Upcoming: today → lookahead
    upcoming_raw = [
        c for c in data["all"]
        if today.isoformat() <= c["date"] <= horizon.isoformat() and keep(c)
    ]
    upcoming = dedup(upcoming_raw)

    # History: lookback_start → yesterday
    hist_raw = [
        c for c in data["all"]
        if lookback_start.isoformat() <= c["date"] < today.isoformat() and keep(c)
    ]
    history = dedup(hist_raw)

    # Always re-render — single fixed file, updated in-place
    render_briefing(upcoming, history, today, args.lookback, args.lookahead, BRIEFING_PATH)

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
