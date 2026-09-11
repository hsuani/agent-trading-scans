#!/usr/bin/env python3
"""One price chain for every tool. Yahoo's cookie/crumb flow is rate-limited
locally and the whole host is blocked in the cloud sandbox (CONNECT 403).

  quotes : cnyes (鉅亨網) -> Yahoo fast_info -> TWSE
  history: Yahoo v8 chart (no crumb, split-adjusted) -> cnyes charting (NOT
           split-adjusted upstream: 0050 4:1, CRWD 4:1, 6669 3:1 all show as
           gaps, so a heuristic back-adjustment is applied) -> yfinance -> TWSE

  quote(ticker)            -> {"last_price", "previous_close", ..., "source"} | None
  history(ticker, days)    -> pandas DataFrame [open high low close volume], ascending, .attrs["source"]
  probe()                  -> {"us": {...}, "tw": {...}, "ok": bool}

CLI:
  pricefeed.py NVDA quote
  pricefeed.py 2330.TW history --days 400
  pricefeed.py probe            # exit 0 when a US and a TW ticker both have quote + history
"""
import json
import sys
import time
import urllib.request
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

UA = {"User-Agent": "Mozilla/5.0"}


def _get(url, timeout=12):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8"))


def cnyes_symbol(ticker):
    u = ticker.upper()
    if u.endswith((".TW", ".TWO")):
        return "TWS:" + u.split(".")[0] + ":STOCK"
    if u.endswith(".KS"):
        return None                                   # cnyes has no Korean market
    return "USS:" + u + ":STOCK"


# ---------------- quotes ----------------
def quote(ticker):
    from yf import _cnyes_quote, _twse_quote          # existing, proven helpers
    q = _cnyes_quote(ticker)
    if q and q.get("last_price"):
        q["source"] = "cnyes"; return q
    try:
        import yfinance as yf
        fi = yf.Ticker(ticker).fast_info
        p = fi.get("last_price") or fi.get("lastPrice")
        if p:
            return {"last_price": float(p), "previous_close": fi.get("previous_close"),
                    "day_high": fi.get("day_high"), "day_low": fi.get("day_low"),
                    "currency": fi.get("currency"), "source": "yahoo"}
    except Exception:
        pass
    if ticker.upper().endswith((".TW", ".TWO")):
        q = _twse_quote(ticker)
        if q and q.get("last_price"):
            q["source"] = "twse"; return q
    return None


# ---------------- history ----------------
SPLIT_GAP = 1.6   # a close/close jump beyond x1.6 or below /1.6 overnight is a split, not a move


def split_adjust(rows):
    """Back-adjust unadjusted daily rows: at each overnight gap beyond SPLIT_GAP the
    factor prev_close / open is applied to every earlier bar (prices divided,
    volume multiplied). Heuristic — stock-dividend ratios of 1.05–1.2 pass through."""
    out, factor = [], 1.0
    for i in range(len(rows) - 1, -1, -1):
        d, o, h, l, c, v = rows[i]
        out.append((d, o / factor, h / factor, l / factor, c / factor, (v or 0) * factor))
        if i > 0 and rows[i - 1][4] and o:
            r = rows[i - 1][4] / o
            if r > SPLIT_GAP or r < 1 / SPLIT_GAP:
                factor *= r
    return out[::-1]


def _cnyes_history(ticker, days):
    sym = cnyes_symbol(ticker)
    if not sym:
        return None
    now = int(time.time())
    # NB: the API wants from=newest, to=oldest (reversed); bars come newest-first
    d = _get(f"https://ws.api.cnyes.com/ws/api/v1/charting/history?symbol={sym}"
             f"&resolution=D&from={now}&to={now - 86400 * days}")["data"]
    if not d.get("t"):
        return None
    rows = sorted(zip(d["t"], d["o"], d["h"], d["l"], d["c"], d["v"]))
    return split_adjust([(datetime.fromtimestamp(t, timezone.utc).date(), o, h, l, c, v)
                         for t, o, h, l, c, v in rows])


def _yahoo_v8_history(ticker, days):
    rng = "2y" if days > 365 else "1y" if days > 180 else "6mo" if days > 90 else "3mo"
    d = _get(f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?range={rng}&interval=1d")
    res = d["chart"]["result"][0]
    q = res["indicators"]["quote"][0]
    out = []
    for t, o, h, l, c, v in zip(res["timestamp"], q["open"], q["high"], q["low"], q["close"], q["volume"]):
        if c is not None:
            out.append((datetime.fromtimestamp(t, timezone.utc).date(), o, h, l, c, v))
    return out or None


def _yfinance_history(ticker, days):
    import yfinance as yf
    df = yf.Ticker(ticker).history(period=f"{max(days, 30)}d", auto_adjust=True)
    if df is None or df.empty:
        return None
    return [(i.date(), r["Open"], r["High"], r["Low"], r["Close"], r["Volume"]) for i, r in df.iterrows()]


def _twse_history(ticker, days):
    u = ticker.upper()
    if not u.endswith(".TW"):                          # STOCK_DAY is TWSE (上市) only
        return None
    num, out, first = u.split(".")[0], [], date.today() - timedelta(days=days)
    m = date.today().replace(day=1)
    while m >= first.replace(day=1):
        d = _get(f"https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date={m:%Y%m}01&stockNo={num}")
        for r in d.get("data", []):
            y, mo, dd = r[0].split("/")
            f = lambda x: float(x.replace(",", "")) if x not in ("--", "") else None  # noqa: E731
            out.append((date(int(y) + 1911, int(mo), int(dd)), f(r[3]), f(r[4]), f(r[5]), f(r[6]), f(r[1])))
        m = (m - timedelta(days=1)).replace(day=1)
        time.sleep(0.4)
    return sorted(out) or None


def history(ticker, days=400):
    """DataFrame of daily OHLCV, ascending by date; .attrs['source'] names the feed."""
    import pandas as pd
    last = None
    for name, fn in (("yahoo_v8", _yahoo_v8_history), ("cnyes", _cnyes_history),
                     ("yfinance", _yfinance_history), ("twse", _twse_history)):
        try:
            rows = fn(ticker, days)
        except Exception as e:                        # noqa: BLE001 — try the next feed
            last = f"{name}: {e}"
            continue
        if rows:
            df = pd.DataFrame(rows, columns=["date", "open", "high", "low", "close", "volume"])
            df["date"] = pd.to_datetime(df["date"])
            df = df.set_index("date").sort_index()
            df.attrs["source"] = name
            return df
    raise RuntimeError(f"no history for {ticker} ({last})")


def probe(us="NVDA", tw="2330.TW"):
    out = {}
    for k, t in (("us", us), ("tw", tw)):
        q = quote(t)
        try:
            h = history(t, 30)
            hs, hn = h.attrs["source"], len(h)
        except Exception as e:                        # noqa: BLE001
            hs, hn = None, 0
        out[k] = {"ticker": t, "quote": q and q.get("last_price"), "quote_source": q and q.get("source"),
                  "history_source": hs, "history_bars": hn}
    out["ok"] = all(v["quote"] and v["history_bars"] >= 10 for v in (out["us"], out["tw"]))
    out["checked_at"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    return out


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "probe":
        r = probe()
        print(json.dumps(r, ensure_ascii=False))
        sys.exit(0 if r["ok"] else 1)
    tk, kind = a[0], a[1]
    if kind == "quote":
        print(json.dumps(quote(tk), ensure_ascii=False))
    elif kind == "history":
        days = int(a[a.index("--days") + 1]) if "--days" in a else 400
        df = history(tk, days)
        print(json.dumps({"source": df.attrs["source"], "bars": len(df),
                          "rows": [{"date": i.date().isoformat(), **{c: (None if r[c] != r[c] else r[c]) for c in df.columns}}
                                   for i, r in df.iterrows()]}, ensure_ascii=False))
