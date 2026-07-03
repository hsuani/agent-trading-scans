#!/usr/bin/env python3
"""
Serenity tracker ingest — ZERO LLM. Pulls the public feed from trackserenity.com
(mirrors the X account @aleabitoreddit / 白毛股神) and distils it into:

  serenity/signals.json   raw upstream cache (audit / reproducibility)
  serenity/serenity.json  parsed: ranked tickers by mention count + recency,
                          latest tweets, and his "new picks" (mentioned tickers
                          not already in our scan universe)
  serenity/universe.txt   top-N new picks — the dynamic ticker list the weekly
                          `serenity` sector scan reads (his most-discussed calls
                          that we don't already cover)

The upstream /data/signals.json is a public static JSON (no auth), so this runs
fine as a GitHub Action with zero Claude usage. Designed to be idempotent.

Run: TRADING_SCANS_ROOT=<repo> python3 pipeline/tools/serenity.py
Env: SERENITY_TOP_N (default 8), SERENITY_MIN_MENTIONS (default 2)
"""
import json
import os
import re
import sys
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(os.environ.get("TRADING_SCANS_ROOT") or Path(__file__).resolve().parents[2])
OUT_DIR = ROOT / "serenity"
FEED_URL = "https://trackserenity.com/data/signals.json"

TOP_N = int(os.environ.get("SERENITY_TOP_N", "8"))
MIN_MENTIONS = int(os.environ.get("SERENITY_MIN_MENTIONS", "2"))
# His high-conviction picks (mentioned this often) force FULL Phase 2-4 in the
# serenity scan, bypassing the Phase-1 threshold — frequency = his conviction.
CONVICTION_MIN = int(os.environ.get("SERENITY_CONVICTION_MIN", "4"))

# Our scan universe (US tickers) — used to flag which of his mentions are
# already covered vs genuinely new. Keep loosely in sync with SKILL.md.
OUR_UNIVERSE = set((
    "NVDA AMD AVGO MRVL TSM ASML MU ARM CBRS VST CEG TLN GEV ETN PWR NEE SO "
    "VRT MOD ANET COHR LITE FN AAOI IPGP GLW EQIX DLR IRM AMT SMCI DELL HPE "
    "CRWD PANW ZS S OKTA TSLA ISRG ABBNY FANUY SYM SPAI FCX MP LIN APD ALB "
    "IONQ RGTI QBTS QUBT ARQQ LAES HON IBM POET CRDO ALAB GFS INTC "
    "GLD TLT UUP SH"
).split())

# Cashtags that are indices / macro / non-US-equity noise — exclude from picks.
NOISE = {"DRAM", "KOSPI", "KORU", "EWY", "SHA", "SOXL", "LPK", "SIVEF", "SPCX"}
TICKER_RE = re.compile(r"^[A-Z]{1,5}$")

# Bilingual (EN/中文) sentiment lexicon for a fast, zero-LLM heuristic polarity.
# Crude on sarcasm — the nightly LLM digest carries the authoritative narrative;
# this drives the per-ticker 🟢/🔴 badges + trend sparkline.
BULL = ["long", "buy", "bought", "add", "adding", "accumulate", "breakout", "moon",
        "undervalued", "cheap", "upside", "beat", "beats", "strong", "bullish",
        "rip", "ripping", "squeeze", "all-time high", "ath", "outperform", "load",
        "看多", "做多", "買進", "買", "加碼", "突破", "低估", "上漲", "噴", "強",
        "利多", "看好", "抄底", "進場"]
BEAR = ["short", "sell", "sold", "trim", "trimmed", "dump", "crash", "crashing",
        "overvalued", "expensive", "downside", "miss", "misses", "weak", "bearish",
        "avoid", "puts", "drop", "fall", "falling", "scathing", "delay", "delays",
        "看空", "做空", "賣出", "賣", "減碼", "跌", "崩", "高估", "利空", "看壞",
        "出貨", "停損", "泡沫", "警示"]
NEGATORS = ["not ", "no ", "isn't", "aren't", "don't", "avoid", "沒", "不", "非"]


def tweet_polarity(text: str) -> int:
    """+1 bull / -1 bear / 0 neutral from lexicon hit counts (naive)."""
    low = (text or "").lower()
    b = sum(low.count(w) for w in BULL)
    s = sum(low.count(w) for w in BEAR)
    if b > s:
        return 1
    if s > b:
        return -1
    return 0


def fetch_feed():
    req = urllib.request.Request(FEED_URL, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))


def main():
    OUT_DIR.mkdir(exist_ok=True)
    try:
        feed = fetch_feed()
    except Exception as e:
        print(f"serenity: fetch failed: {e}", file=sys.stderr)
        sys.exit(1)

    (OUT_DIR / "signals.json").write_text(
        json.dumps(feed, ensure_ascii=False, indent=2), encoding="utf-8")

    tweets = feed.get("tweets", []) or []
    # Mention count + most-recent timestamp + sentiment timeline per ticker.
    mentions = Counter()
    last_seen = {}
    timeline = {}   # ticker -> [(time, polarity)] oldest..newest
    # tweets come newest-first; reverse for chronological timeline
    for t in reversed(tweets):
        ts = t.get("displayTime") or t.get("createdAt") or ""
        pol = tweet_polarity(t.get("text", ""))
        for c in (t.get("cashtags") or []):
            c = c.upper()
            mentions[c] += 1
            if c not in last_seen or ts > last_seen[c]:
                last_seen[c] = ts
            timeline.setdefault(c, []).append({"time": ts, "pol": pol})

    ranked = []
    for tk, n in mentions.most_common():
        tl = timeline.get(tk, [])
        pos = sum(1 for x in tl if x["pol"] > 0)
        neg = sum(1 for x in tl if x["pol"] < 0)
        neu = sum(1 for x in tl if x["pol"] == 0)
        latest_pol = tl[-1]["pol"] if tl else 0
        latest = "bull" if latest_pol > 0 else "bear" if latest_pol < 0 else "neutral"
        ranked.append({
            "ticker": tk, "mentions": n,
            "last_seen": last_seen.get(tk, ""),
            "in_universe": tk in OUR_UNIVERSE,
            "sentiment": {"latest": latest, "pos": pos, "neg": neg, "neu": neu,
                          "timeline": [x["pol"] for x in tl]},
        })

    # "new picks" = real-looking US tickers he mentions >= MIN_MENTIONS that we
    # don't already scan and aren't index/macro noise. Cap at TOP_N.
    new_picks = [
        r["ticker"] for r in ranked
        if not r["in_universe"] and r["mentions"] >= MIN_MENTIONS
        and TICKER_RE.match(r["ticker"]) and r["ticker"] not in NOISE
    ][:TOP_N]

    # High-conviction subset (mention count >= CONVICTION_MIN) — these force full
    # Phase 2-4 in the serenity scan regardless of the Phase-1 pick threshold.
    force_full = [tk for tk in new_picks
                  if mentions[tk] >= CONVICTION_MIN]

    latest = []
    for t in tweets[:30]:
        latest.append({
            "text": (t.get("text") or "")[:600],
            "url": t.get("url", ""),
            "time": t.get("displayTime") or t.get("createdAt") or "",
            "cashtags": [c.upper() for c in (t.get("cashtags") or [])],
            "is_retweet": bool(t.get("isRetweet")),
        })

    out = {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "source_updated_at": feed.get("updatedAt", ""),
        "account": "@aleabitoreddit (Serenity / 白毛股神)",
        "tickers": ranked,
        "new_picks": new_picks,
        "force_full": force_full,
        "tweets": latest,
    }
    (OUT_DIR / "serenity.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")

    (OUT_DIR / "universe.txt").write_text(
        "# Serenity's top new picks (mentioned >= %d, not in our universe).\n"
        "# Auto-generated by serenity.py; the weekly `serenity` sector scans these.\n"
        % MIN_MENTIONS + "\n".join(new_picks) + "\n", encoding="utf-8")

    (OUT_DIR / "force_full.txt").write_text(
        "# Serenity's high-conviction picks (mentioned >= %d) — force FULL Phase 2-4,\n"
        "# bypassing the Phase-1 threshold. Auto-generated by serenity.py.\n"
        % CONVICTION_MIN + "\n".join(force_full) + "\n", encoding="utf-8")

    print(f"serenity: {len(tweets)} tweets, {len(ranked)} tickers ranked; "
          f"new picks ({len(new_picks)}): {' '.join(new_picks)}")
    print(f"  force-full (>= {CONVICTION_MIN} mentions): {' '.join(force_full) or '—'}")
    print(f"  -> {OUT_DIR/'serenity.json'}, universe.txt, force_full.txt")


if __name__ == "__main__":
    main()
