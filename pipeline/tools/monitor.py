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
    p = _plan_status(card)
    lo, hi, stop, t2 = p["entry_lo"], p["entry_hi"], p["stop"], p["t2"]
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
        if not DATE_RE.match(cd) or cd < today or c.get("date_precision", "exact_day") != "exact_day":
            continue   # a quarter token mapped to a mid-quarter day is not a dated catalyst
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
    """Live last price via pricefeed.quote (cnyes -> Yahoo -> TWSE). None on failure."""
    try:
        from pricefeed import quote
        q = quote(ticker)
        return float(q["last_price"]) if q and q.get("last_price") else None
    except Exception:
        return None


from levels import plan_status as _plan_status  # noqa: E402  — shared absolute-price parser


def status(card, px):
    """Classify live price vs locked levels. Returns (urgency, flag list)."""
    if px is None:
        return (5, ["no price"])
    # Absolute prices only (levels.py): "T1 = 2.6" is an R multiple, "10x P/E" is a
    # valuation, "4.30%" is a yield — none of them may fire a price trigger.
    p = _plan_status(card, quote=px)
    if p["plan"] in ("LEVELS_INVALID", "LEVEL_SCALE_SUSPECT"):
        return (9, [f"⚠ {p['plan']} ({p['reason']}) — price monitoring suppressed"])
    lo, hi, stop, t1, t2 = p["entry_lo"], p["entry_hi"], p["stop"], p["t1"], p["t2"]
    if not any((lo, stop, t1, t2)):
        return (9, ["UNPRICED — event / thesis only"])
    flags, urg = [], 9
    if stop is not None and stop > 0:
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


def leverage_rule():
    """正2 (2x leveraged ETF) Beta-adjustment rule tracker — mechanical, zero-LLM.
    Tracks the underlying index (0050) drawdown from its trailing peak and emits
    the deploy/rebalance signal per the 00631L strategy:
      - 0050 回撤 >= TRIGGER% from peak  -> 現金全買 00631L (Beta -> ~2)
      - 0050 回前高 (within NEAR% of peak) -> 回 Beta 1, 重建現金彈藥
      - else                              -> Beta 1, 顯示回撤 + 距觸發還差
    Config: LEVERAGE_UNDERLYING (0050.TW), LEVERAGE_ETF (00631L.TW),
            LEVERAGE_TRIGGER (28), LEVERAGE_NEAR (1), LEVERAGE_LOOKBACK (2y)."""
    und = os.environ.get("LEVERAGE_UNDERLYING", "0050.TW")
    etf = os.environ.get("LEVERAGE_ETF", "00631L.TW")
    trigs = sorted(float(x) for x in
                   os.environ.get("LEVERAGE_TRIGGERS", "10,15,20,25,30").split(",") if x.strip())
    near = float(os.environ.get("LEVERAGE_NEAR", "1"))
    lookback = os.environ.get("LEVERAGE_LOOKBACK", "2y")
    unavailable = {"underlying": und, "etf": etf, "triggers": trigs, "ladder": [],
                   "price": None, "drawdown_pct": None, "max_drawdown_pct": None,
                   "next_trigger": None, "gap_pp": None, "deepest_crossed": None, "etf_price": None,
                   "signal": "DATA_UNAVAILABLE", "urgency": 3,
                   "action": f"⚠ {und} quote unavailable — Beta action paused until the feed recovers"}
    try:
        from pricefeed import history as _hist
        days = {"1y": 400, "2y": 760, "6mo": 200}.get(lookback, 760)
        df = _hist(und, days)
        c = df["close"].dropna()
        if c.empty or not (float(c.iloc[-1]) > 0):
            return unavailable
        peak = float(c.max()); peak_dt = str(c.idxmax().date())
        cur = float(c.iloc[-1])
        after = c[c.index >= c.idxmax()]
        trough = float(after.min()); trough_dt = str(after.idxmin().date())
        dd = (cur - peak) / peak * 100.0            # current drawdown % (negative)
        add = abs(dd)                               # drawdown magnitude
        max_dd = (trough - peak) / peak * 100.0     # deepest drawdown since peak
        epx = price(etf)

        ladder = [{"pct": t, "crossed": add >= t} for t in trigs]
        crossed = [t for t in trigs if add >= t]
        pending = [t for t in trigs if add < t]
        next_t = pending[0] if pending else None
        gap = (next_t - add) if next_t is not None else None
        deepest = crossed[-1] if crossed else None

        if dd >= -near:
            sig = "AT_HIGH"; urg = 1
            action = "🟢 已回前高 → 回 Beta 1, 重建現金彈藥"
        elif deepest is not None:
            sig = "TRIGGER"; urg = 0 if deepest >= trigs[-1] else 2
            nxt = (f"，下一檔 -{next_t:.0f}% 還差 {gap:.1f}pp" if next_t is not None
                   else "（已達最深門檻，Beta 接近 2）")
            action = f"🔴 回撤 -{add:.1f}% 已跨 -{deepest:.0f}% 門檻 → 加碼 {etf}{nxt}"
        else:
            sig = "NORMAL"; urg = 3
            action = (f"⚪ Beta 1 · 現回撤 {dd:.1f}% · 距首檔 -{next_t:.0f}% 還差 {gap:.1f}pp"
                      if next_t is not None else f"⚪ Beta 1 · 現回撤 {dd:.1f}%")
        return {
            "underlying": und, "etf": etf, "triggers": trigs, "ladder": ladder,
            "price": round(cur, 2), "peak": round(peak, 2), "peak_date": peak_dt,
            "trough": round(trough, 2), "trough_date": trough_dt,
            "drawdown_pct": round(dd, 2), "max_drawdown_pct": round(max_dd, 2),
            "next_trigger": next_t, "gap_pp": round(gap, 2) if gap is not None else None,
            "deepest_crossed": deepest, "etf_price": epx,
            "signal": sig, "action": action, "urgency": urg,
        }
    except Exception as e:
        unavailable["error"] = str(e)
        return unavailable


def dca_rule(hist=None):
    """ETF 定投 / 加碼 / TQQQ 濾網 tracker — mechanical, zero-LLM. Everything is
    quoted per $1,000 so the user scales it; DCA_RESERVE (cash parked in BOXX) is
    echoed for absolute amounts. Three rules, all keyed on QQQ:
      core   : fixed monthly split (DCA_PLAN weights per $1,000) — never paused
      boost  : the accumulated 加碼 reserve is deployed by a drawdown ladder on
               QQQ's 2-year high (DCA_BOOST_TIERS "10:30,15:30,20:40" = at -10%
               deploy 30% of the reserve, -15% another 30%, -20% the rest);
               ladder resets once QQQ is back within 1% of its high
      sleeve : TQQQ held only while QQQ closes above its 200-day MA — exit the
               day after a close below, re-enter the day after a close above"""
    tickers = [t.strip().upper() for t in os.environ.get("DCA_TICKERS", "QQQ,SPY,SMH,XLK,VGT,TQQQ,VOO,QQQM").split(",") if t.strip()]
    plan = [(k.strip().upper(), float(v)) for k, v in
            (x.split(":") for x in os.environ.get("DCA_PLAN", "VOO:450,QQQM:300,SMH:150,XLK:100").split(",") if ":" in x)]
    tiers = [(float(k), float(v)) for k, v in
             (x.split(":") for x in os.environ.get("DCA_BOOST_TIERS", "10:30,15:30,20:40").split(",") if ":" in x)]
    reserve = float(os.environ.get("DCA_RESERVE", "11200"))
    if hist is None:
        from pricefeed import history as hist
    rows, err = [], None
    for t in tickers:
        try:
            c = hist(t, 760)["close"].dropna()
            if len(c) < 210:
                raise RuntimeError(f"{len(c)} bars")
            ma = c.rolling(200).mean()
            state = (c > ma).astype(int)
            flips = state[state.diff().fillna(0) != 0]
            last_flip = flips.index[-1] if len(flips) else c.index[0]
            rows.append({"ticker": t, "close": round(float(c.iloc[-1]), 2), "ma200": round(float(ma.iloc[-1]), 2),
                         "vs_ma200_pct": round(float(c.iloc[-1] / ma.iloc[-1] - 1) * 100, 2),
                         "vs_high_pct": round(float(c.iloc[-1] / c.max() - 1) * 100, 2), "high": round(float(c.max()), 2),
                         "high_date": str(c.idxmax().date()), "above": bool(state.iloc[-1]),
                         "cross_date": str(last_flip.date()), "days_in_state": int((c.index[-1] - last_flip).days),
                         "as_of": str(c.index[-1].date())})
        except Exception as e:                        # noqa: BLE001
            err = f"{t}: {e}"
            rows.append({"ticker": t, "close": None, "above": None, "error": str(e)})
    lead = rows[0] if rows else {}
    out = {"tickers": rows, "reserve": reserve,
           "closes": {r["ticker"]: r["close"] for r in rows if r.get("close")},
           "plan": [{"ticker": k, "per_1000": v} for k, v in plan], "plan_total": sum(v for _, v in plan)}
    if lead.get("above") is None:
        out.update(signal="DATA_UNAVAILABLE", urgency=3, boost=None, sleeve=None,
                   action=f"⚠ {tickers[0] if tickers else '—'} history unavailable — 濾網／加碼狀態未知，核心定投照常")
        if err:
            out["error"] = err
        return out
    # --- sleeve: TQQQ on/off ---
    sleeve = {"etf": "TQQQ", "hold": lead["above"], "exit_below": lead["ma200"], "enter_above": lead["ma200"],
              "buffer_pct": lead["vs_ma200_pct"], "days": lead["days_in_state"], "since": lead["cross_date"],
              "tqqq_price": next((r.get("close") for r in rows if r["ticker"] == "TQQQ"), None)}
    # --- boost ladder on QQQ drawdown ---
    dd = -lead["vs_high_pct"]                       # magnitude
    ladder, cum = [], 0.0
    for pct, share in tiers:
        cum += share
        ladder.append({"pct": pct, "share": share, "cum_share": cum, "crossed": dd >= pct,
                       "per_1000": round(10 * share, 0), "reserve_amt": round(reserve * share / 100, 0),
                       "qqq_level": round(lead["high"] * (1 - pct / 100), 2)})
    crossed = [x for x in ladder if x["crossed"]]
    pending = [x for x in ladder if not x["crossed"]]
    at_high = dd <= 1.0
    boost = {"drawdown_pct": round(-dd, 2), "high": lead["high"], "high_date": lead["high_date"], "ladder": ladder,
             "deployable_share": sum(x["share"] for x in crossed), "deployable_per_1000": round(10 * sum(x["share"] for x in crossed), 0),
             "deployable_reserve": round(reserve * sum(x["share"] for x in crossed) / 100, 0),
             "next_pct": pending[0]["pct"] if pending else None, "next_level": pending[0]["qqq_level"] if pending else None,
             "gap_pp": round(pending[0]["pct"] - dd, 2) if pending else None, "reset": at_high}
    # --- headline ---
    if not lead["above"]:
        sig, urg = "BELOW", 0
        action = (f"🔻 QQQ 跌破 200 日線 {lead['vs_ma200_pct']:.1f}%（{lead['days_in_state']} 天）→ TQQQ 濾網=出場區；"
                  f"核心定投照常" + (f"；加碼階梯已跨 -{crossed[-1]['pct']:.0f}%" if crossed else ""))
    elif crossed:
        sig, urg = "BOOST", 2
        action = (f"🟠 QQQ 距高點 {-dd:.1f}% 已跨 -{crossed[-1]['pct']:.0f}% → 加碼金可投 {boost['deployable_share']:.0f}%"
                  f"（每 $1,000 投 ${boost['deployable_per_1000']:.0f}）；TQQQ 濾網=持有區")
    else:
        sig, urg = "ABOVE", 1
        action = (f"🟢 QQQ 在 200 日線上 +{lead['vs_ma200_pct']:.1f}%（{lead['days_in_state']} 天）→ 核心定投照常、"
                  f"TQQQ 濾網=持有區、加碼金續存（距首檔 -{tiers[0][0]:.0f}% 還差 {boost['gap_pp']:.1f}pp）" if pending else
                  f"🟢 QQQ 在 200 日線上 → 核心定投照常、TQQQ 濾網=持有區")
    out.update(signal=sig, urgency=urg, action=action, sleeve=sleeve, boost=boost)
    if err:
        out["error"] = err
    return out


def _fred(series, days=400):
    """Latest `days` observations of a FRED series as [(date, value)], via the
    public CSV endpoint (no key). Raises on network failure; callers soft-fail."""
    import urllib.request
    from datetime import date, timedelta
    start = (date.today() - timedelta(days=days)).isoformat()
    raw = urllib.request.urlopen(f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={series}&cosd={start}", timeout=15).read().decode()
    out = []
    for line in raw.splitlines()[1:]:
        d, v = line.split(",")[:2]
        try:
            out.append((d, float(v)))
        except ValueError:
            continue                                  # "." = missing
    return out


def crash_rule(hist=None, fred=None, breadth_closes=None):
    """進階加碼訊號 — mechanical, zero-LLM, independent of the QQQ drawdown ladder.
    Five flags, each with a level, a threshold and whether it is ON today:
      vix      ^VIX close > 30 (fear) / > 40 (panic)
      spx      SPY close < MA200 AND RSI14 < 30
      breadth  share of the scan universe's US names within 10% of their 52-week
               low >= 40% (proxy; no free index-wide breadth feed)
      hy       ICE BofA HY OAS (FRED BAMLH0A0HYM2) > 4% AND >= 50bp below its
               60-day high — credit stress that has started to EASE
      fed      effective fed funds (FRED DFF) >= 25bp below 90 days ago
    Composite = number of ON flags. Deployment (share of the boost reserve) by
    CRASH_TIERS "2:25,3:50,4:100" — informational: the backtest shows VIX > 40
    and >= 3 flags are the only ones that beat buying on a random day."""
    if hist is None:
        from pricefeed import history as hist
    fred = fred or _fred
    tiers = [(int(k), float(v)) for k, v in
             (x.split(":") for x in os.environ.get("CRASH_TIERS", "2:25,3:50,4:100").split(",") if ":" in x)]
    flags, errs = {}, []

    def flag(key, label, on, level, threshold, note=""):
        flags[key] = {"label": label, "on": bool(on) if on is not None else None, "level": level,
                      "threshold": threshold, "note": note}
    # vix
    try:
        v = hist("^VIX", 400, cache=False)["close"].dropna()
        lv = float(v.iloc[-1]); hi60 = float(v.tail(60).max())
        flag("vix", "VIX 恐慌", lv > 30, f"{lv:.1f}", "> 30（> 40 極端）",
             f"60 日高 {hi60:.1f}" + ("，極端 > 40 ✓" if lv > 40 else ""))
    except Exception as e:                            # noqa: BLE001
        errs.append(f"vix: {e}"); flag("vix", "VIX 恐慌", None, "—", "> 30")
    # spx
    try:
        c = hist("SPY", 760)["close"].dropna()
        ma = float(c.rolling(200).mean().iloc[-1])
        d = c.diff(); up = d.clip(lower=0).ewm(alpha=1/14, adjust=False).mean(); dn = (-d.clip(upper=0)).ewm(alpha=1/14, adjust=False).mean()
        rsi = float((100 - 100 / (1 + up / dn)).iloc[-1]); px = float(c.iloc[-1]); hi52 = float(c.tail(252).max())
        flag("spx", "SPY 跌破年線且超賣", px < ma and rsi < 30,
             f"{px:.0f} vs MA200 {ma:.0f}（{(px/ma-1)*100:+.1f}%），RSI14 {rsi:.0f}", "收盤 < MA200 且 RSI14 < 30",
             f"距 52 週高 {(px/hi52-1)*100:+.1f}%")
    except Exception as e:                            # noqa: BLE001
        errs.append(f"spx: {e}"); flag("spx", "SPY 跌破年線且超賣", None, "—", "< MA200 且 RSI14 < 30")
    # breadth (proxy from the scan universe's US names)
    try:
        if breadth_closes is None:
            import universe as _u
            us = sorted(t for t in _u.static_universe() if "." not in t)
            breadth_closes = {}
            for t in us:
                try:
                    breadth_closes[t] = hist(t, 400)["close"].dropna()
                except Exception:                     # noqa: BLE001
                    continue
        near_low = [float(c.iloc[-1]) <= float(c.tail(252).min()) * 1.10 for c in breadth_closes.values() if len(c) >= 200]
        below_ma = [float(c.iloc[-1]) < float(c.rolling(200).mean().iloc[-1]) for c in breadth_closes.values() if len(c) >= 200]
        if not near_low:
            raise RuntimeError("no closes")
        pl, pb = 100 * sum(near_low) / len(near_low), 100 * sum(below_ma) / len(below_ma)
        flag("breadth", "市場寬度極差（代理）", pl >= 40, f"{pl:.0f}% 在 52 週低點 10% 內；{pb:.0f}% 在年線下", ">= 40% 近 52 週低點",
             f"樣本 = 掃描 universe 美股 {len(near_low)} 檔，非全市場")
    except Exception as e:                            # noqa: BLE001
        errs.append(f"breadth: {e}"); flag("breadth", "市場寬度極差（代理）", None, "—", ">= 40% 近 52 週低點")
    # hy
    try:
        h = fred("BAMLH0A0HYM2", 200)
        vals = [x[1] for x in h]; cur = vals[-1]; hi60 = max(vals[-60:])
        flag("hy", "高收益債利差由高點收斂", cur > 4.0 and hi60 - cur >= 0.5, f"{cur:.2f}%（60 日高 {hi60:.2f}%，{(cur-hi60)*100:+.0f}bp）",
             "> 4% 且較 60 日高點回落 >= 50bp", f"FRED BAMLH0A0HYM2 {h[-1][0]}")
    except Exception as e:                            # noqa: BLE001
        errs.append(f"hy: {e}"); flag("hy", "高收益債利差由高點收斂", None, "—", "> 4% 且回落 >= 50bp")
    # fed
    try:
        f = fred("DFF", 200)
        cur = f[-1][1]; ago = f[-91][1] if len(f) > 91 else f[0][1]
        flag("fed", "聯準會轉向寬鬆", cur - ago <= -0.25, f"{cur:.2f}%（90 日前 {ago:.2f}%，{(cur-ago)*100:+.0f}bp）", "較 90 日前降 >= 25bp",
             "回測：單獨出現時 6 個月正報酬率僅 48%，當輔助不當觸發")
    except Exception as e:                            # noqa: BLE001
        errs.append(f"fed: {e}"); flag("fed", "聯準會轉向寬鬆", None, "—", "降 >= 25bp / 90 日")
    on = [k for k, x in flags.items() if x["on"]]
    unknown = [k for k, x in flags.items() if x["on"] is None]
    n = len(on)
    share = max([v for k, v in tiers if n >= k], default=0.0)
    if n == 0:
        sig, urg, action = "CALM", 3, f"⚪ 崩跌訊號 0/5 → 進階加碼不啟動" + (f"（{len(unknown)} 項無資料）" if unknown else "")
    elif share == 0:
        sig, urg, action = "WATCH", 2, f"🟡 崩跌訊號 {n}/5（{'、'.join(flags[k]['label'] for k in on)}）→ 觀察，未達加碼門檻 {tiers[0][0]} 個"
    else:
        sig, urg, action = "DEPLOY", 0, (f"🔴 崩跌訊號 {n}/5（{'、'.join(flags[k]['label'] for k in on)}）→ 進階加碼：投入加碼金 {share:.0f}%"
                                         f"（每 $1,000 存量投 ${10*share:.0f}）")
    return {"flags": flags, "count": n, "unknown": unknown, "tiers": [{"min_signals": k, "share": v} for k, v in tiers],
            "deploy_share": share, "signal": sig, "urgency": urg, "action": action, **({"errors": errs} if errs else {})}


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
        "leverage": leverage_rule(),
        "dca": dca_rule(),
        "crash": crash_rule(),
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
