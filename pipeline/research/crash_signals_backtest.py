#!/usr/bin/env python3
"""Crash-signal event study (zero LLM). For each signal, every FIRST trigger day
(60-trading-day cooldown) is an event; report QQQ / SPY forward returns and how
often the next 6 months were positive. Also the composite (>= N signals the same
week). Data: ^VIX, SPY, QQQ (yfinance, dividends reinvested); FRED BAMLH0A0HYM2
(ICE BofA US HY OAS, %) and DFF (effective fed funds, %).
Usage: crash_signals_backtest.py <cache_dir> [--fetch]
"""
import io, json, sys, urllib.request
import numpy as np, pandas as pd

D = sys.argv[1]
if "--fetch" in sys.argv:
    import os, warnings, yfinance as yf
    warnings.filterwarnings("ignore"); os.makedirs(D, exist_ok=True)
    for t in ("^VIX", "SPY", "QQQ", "HYG", "IEF"):
        h = yf.Ticker(t).history(period="max", auto_adjust=True)[["Close"]]
        h.to_csv(f"{D}/{t.strip('^')}.csv")
    for s in ("BAMLH0A0HYM2", "DFF"):
        raw = urllib.request.urlopen(f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={s}&cosd=1990-01-01", timeout=20).read()
        open(f"{D}/{s}.csv", "wb").write(raw)

def load(n, col="Close"):
    s = pd.read_csv(f"{D}/{n}.csv", index_col=0)
    s.index = pd.to_datetime(s.index, utc=True).tz_localize(None).normalize()
    return pd.to_numeric(s.iloc[:, 0], errors="coerce").dropna()

vix, spy, qqq = load("VIX"), load("SPY"), load("QQQ")
hy, dff = load("BAMLH0A0HYM2"), load("DFF")
idx = spy.index
vix, hy, dff = vix.reindex(idx).ffill(), hy.reindex(idx).ffill(), dff.reindex(idx).ffill()
# FRED's public CSV only returns ~3 years of the ICE BofA OAS (licensing), so the
# backtest uses a tradable proxy from 2007: HYG / IEF (high-yield vs treasuries).
ratio = (load("HYG") / load("IEF")).reindex(idx).ffill()
stress = ratio <= ratio.rolling(120).max() * 0.93                 # HY underperforming treasuries by >= 7% vs 6-month high
easing = ratio >= ratio.rolling(60).min() * 1.02                   # and has bounced >= 2% off its 60-day low

def rsi(s, n=14):
    d = s.diff(); up = d.clip(lower=0).ewm(alpha=1/n, adjust=False).mean(); dn = (-d.clip(upper=0)).ewm(alpha=1/n, adjust=False).mean()
    return 100 - 100 / (1 + up / dn)

ma200 = spy.rolling(200).mean(); r14 = rsi(spy)
sig = {
    "VIX > 30":                      vix > 30,
    "VIX > 40":                      vix > 40,
    "SPY < MA200 且 RSI14 < 30":      (spy < ma200) & (r14 < 30),
    "HY OAS 由 60 日高點回落 ≥ 50bp（且仍 > 4%）［FRED，僅 3 年］": (hy.rolling(60).max() - hy >= 0.5) & (hy > 4.0),
    "信用壓力開始收斂［代理：HYG/IEF 距 6 月高 ≤ -7% 且已從 60 日低點反彈 ≥ 2%，2007 起］": stress & easing,
    "Fed 寬鬆：DFF 較 90 日前降 ≥ 25bp": (dff - dff.shift(63)) <= -0.25,
}
sig["SPY 距 52 週高點 ≥ -20%"] = spy / spy.rolling(252).max() - 1 <= -0.20
count = sum(s.astype(int) for k, s in sig.items() if "僅 3 年" not in k)   # composite uses the proxy, not the truncated OAS
sig["綜合：同日 ≥ 2 個訊號"] = count >= 2
sig["綜合：同日 ≥ 3 個訊號"] = count >= 3

def events(flag, cooldown=60):
    out, last = [], -10**9
    f = flag.fillna(False).values
    for i in range(1, len(f)):
        if f[i] and not f[i-1] and i - last > cooldown:
            out.append(i); last = i
    return out

def fwd(s, i, h):
    j = i + h
    return s.iloc[j] / s.iloc[i] - 1 if j < len(s) else np.nan

H = {"3m": 63, "6m": 126, "12m": 252}
print("## 訊號事件研究（SPY 1993 起；HY 利差 1996-12 起；每次首次觸發為一事件，60 交易日冷卻）\n")
print("| 訊號 | 事件數 | 最近一次 | QQQ 6m 中位 | QQQ 12m 中位 | SPY 6m 中位 | SPY 12m 中位 | 6m 正報酬率 | QQQ 6m 最差 |")
print("|---|---|---|---|---|---|---|---|---|")
base = {h: np.nanmedian([fwd(qqq, i, k) for i in range(0, len(qqq) - k, 21)]) for h, k in H.items()}
for name, flag in sig.items():
    ev = [i for i in events(flag) if idx[i] >= qqq.index[0]]
    if not ev: print(f"| {name} | 0 | — | — | — | — | — | — | — |"); continue
    q6 = [fwd(qqq, qqq.index.get_indexer([idx[i]])[0], 126) for i in ev]; q12 = [fwd(qqq, qqq.index.get_indexer([idx[i]])[0], 252) for i in ev]
    s6 = [fwd(spy, i, 126) for i in ev]; s12 = [fwd(spy, i, 252) for i in ev]
    pos = np.nanmean([x > 0 for x in q6 if x == x]) if any(x == x for x in q6) else np.nan
    print(f"| {name} | {len(ev)} | {idx[ev[-1]].date()} | {np.nanmedian(q6)*100:+.1f}% | {np.nanmedian(q12)*100:+.1f}% | {np.nanmedian(s6)*100:+.1f}% | {np.nanmedian(s12)*100:+.1f}% | {pos*100:.0f}% | {np.nanmin(q6)*100:+.1f}% |")
print(f"| 基準：任意月份買 QQQ | — | — | {base['6m']*100:+.1f}% | {base['12m']*100:+.1f}% | — | — | — | — |")
print("\n## 今日讀數\n")
last = idx[-1]
print(f"- {last.date()}: VIX {vix.iloc[-1]:.1f} · SPY {spy.iloc[-1]:.2f} vs MA200 {ma200.iloc[-1]:.2f} ({(spy.iloc[-1]/ma200.iloc[-1]-1)*100:+.1f}%) · RSI14 {r14.iloc[-1]:.1f} · 距 52 週高 {(spy.iloc[-1]/spy.rolling(252).max().iloc[-1]-1)*100:+.1f}%")
print(f"- HYG/IEF {ratio.iloc[-1]:.3f} vs 6 月高 {ratio.rolling(120).max().iloc[-1]:.3f} ({(ratio.iloc[-1]/ratio.rolling(120).max().iloc[-1]-1)*100:+.1f}%) · HY OAS {hy.iloc[-1]:.2f}% (60 日高 {hy.rolling(60).max().iloc[-1]:.2f}%) · DFF {dff.iloc[-1]:.2f}% (90 日前 {dff.shift(63).iloc[-1]:.2f}%) · 今日同時觸發 {int(count.iloc[-1])} 個")
