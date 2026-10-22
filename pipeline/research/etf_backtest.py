#!/usr/bin/env python3
"""ETF buy-strategy backtest (zero LLM). Reads <data_dir>/<TICKER>.csv (Date,Close —
dividend-adjusted closes) + meta.json, prints markdown tables:
  1. buy & hold per window (CAGR / vol / Sharpe vs BIL / max DD / worst & best year)
  2. monthly DCA (money-weighted return, final value per $1k/month)
  3. leveraged-ETF cost drag: actual vs k× daily underlying with zero cost
  4. strategies on the QQQ/TQQQ pair (mix, 200-day-MA filter)
Usage: etf_backtest.py <data_dir> [--fetch] [--end YYYY-MM-DD]
  --fetch  download period=max dividend-adjusted closes + fund metadata via yfinance first
"""
import json, sys
import numpy as np, pandas as pd

D = sys.argv[1]
TICKERS = ["SPY", "VOO", "QQQ", "QQQM", "XLK", "VGT", "SMH", "SOXX", "SSO", "UPRO", "QLD", "TQQQ", "SOXL", "SPXL", "BIL"]
if "--fetch" in sys.argv:
    import os, time, warnings, yfinance as yf
    warnings.filterwarnings("ignore"); os.makedirs(D, exist_ok=True); m = {}
    for t in TICKERS:
        tk = yf.Ticker(t); h = tk.history(period="max", auto_adjust=True); h[["Close"]].to_csv(f"{D}/{t}.csv")
        try: i = tk.info
        except Exception: i = {}
        m[t] = {"start": str(h.index[0].date()), "end": str(h.index[-1].date()), "bars": len(h),
                "expense": i.get("netExpenseRatio") or i.get("annualReportExpenseRatio"), "aum": i.get("totalAssets"),
                "name": i.get("shortName") or i.get("longName"), "yield": i.get("yield")}
        time.sleep(0.5)
    json.dump(m, open(f"{D}/meta.json", "w"), indent=1)
END = pd.Timestamp(sys.argv[sys.argv.index("--end") + 1]) if "--end" in sys.argv else None
meta = {k: v for k, v in json.load(open(f"{D}/meta.json")).items() if k in TICKERS}
px = {}
for t in meta:
    s = pd.read_csv(f"{D}/{t}.csv", index_col=0)["Close"]
    s.index = pd.to_datetime(s.index, utc=True).tz_localize(None).normalize()   # yfinance writes tz-aware stamps
    px[t] = s[:END] if END is not None else s
TODAY = max(s.index[-1] for s in px.values())
rf_daily = px["BIL"].pct_change().fillna(0)          # T-bill proxy for the risk-free leg


def stats(s, rf=None):
    s = s.dropna()
    if len(s) < 60:
        return None
    r = s.pct_change().dropna()
    yrs = (s.index[-1] - s.index[0]).days / 365.25
    cagr = (s.iloc[-1] / s.iloc[0]) ** (1 / yrs) - 1
    vol = r.std() * np.sqrt(252)
    ex = r - (rf.reindex(r.index).fillna(0) if rf is not None else 0)
    sharpe = ex.mean() / ex.std() * np.sqrt(252) if ex.std() else float("nan")
    dd = (s / s.cummax() - 1).min()
    yr = s.resample("YE").last().pct_change().dropna()
    return {"years": yrs, "cagr": cagr, "vol": vol, "sharpe": sharpe, "maxdd": dd,
            "worst_yr": yr.min() if len(yr) else float("nan"), "best_yr": yr.max() if len(yr) else float("nan"),
            "total": s.iloc[-1] / s.iloc[0] - 1}


def window(s, years):
    return s[s.index >= TODAY - pd.DateOffset(years=years)]


def dca(s, years, amt=1000.0):
    """Buy `amt` at the first close of every month for `years`; money-weighted IRR."""
    s = window(s, years).dropna()
    if len(s) < 250:
        return None
    buys = s.resample("MS").first().dropna()
    units = (amt / buys).sum()
    final = units * s.iloc[-1]
    contributed = amt * len(buys)
    # IRR by bisection on monthly cashflows
    months = [(d.year - buys.index[0].year) * 12 + d.month - buys.index[0].month for d in buys.index]
    n_end = (s.index[-1].year - buys.index[0].year) * 12 + s.index[-1].month - buys.index[0].month
    def npv(m):
        return sum(-amt / (1 + m) ** k for k in months) + final / (1 + m) ** n_end
    lo, hi = -0.99, 1.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if npv(mid) > 0: lo = mid
        else: hi = mid
    irr = (1 + mid) ** 12 - 1
    return {"contributed": contributed, "final": final, "irr": irr, "multiple": final / contributed}


def pct(x): return "—" if x is None or x != x else f"{x*100:.1f}%"
def num(x): return "—" if x is None or x != x else f"{x:.2f}"

# ---------- 1. buy & hold ----------
WINDOWS = [("3y", 3), ("5y", 5), ("10y", 10), ("15y", 15)]
print("## 1. 買進持有（含股息再投資）\n")
for name, y in WINDOWS:
    print(f"### {name}（{(TODAY - pd.DateOffset(years=y)).date()} → {TODAY.date()}）\n")
    print("| ETF | 費用率 | CAGR | 年化波動 | Sharpe(vs BIL) | 最大回撤 | 最差年 | 最佳年 | 總報酬 |")
    print("|---|---|---|---|---|---|---|---|---|")
    rows = []
    for t in meta:
        if t == "BIL": continue
        st = stats(window(px[t], y), rf_daily)
        if not st or st["years"] < y * 0.97: continue
        rows.append((st["cagr"], t, st))
    for _, t, st in sorted(rows, reverse=True):
        er = meta[t]["expense"]
        print(f"| {t} | {er:.2f}% | {pct(st['cagr'])} | {pct(st['vol'])} | {num(st['sharpe'])} | {pct(st['maxdd'])} | {pct(st['worst_yr'])} | {pct(st['best_yr'])} | {pct(st['total'])} |")
    print()

# ---------- 2. DCA ----------
print("## 2. 每月定投 $1,000（月初買進）\n")
for y in (5, 10):
    print(f"### {y} 年定投（投入 ${1000*12*y:,}）\n")
    print("| ETF | 期末市值 | 倍數 | 年化報酬(IRR) |")
    print("|---|---|---|---|")
    rows = []
    for t in meta:
        if t == "BIL": continue
        r = dca(px[t], y)
        if r and len(window(px[t], y)) >= y * 250 * 0.97:
            rows.append((r["irr"], t, r))
    for _, t, r in sorted(rows, reverse=True):
        print(f"| {t} | ${r['final']:,.0f} | {r['multiple']:.2f}x | {pct(r['irr'])} |")
    print()

# ---------- 3. leverage cost drag ----------
print("## 3. 槓桿 ETF 真實成本（實際 vs 零成本 k 倍日報酬模擬）\n")
print("| 槓桿 ETF | 標的 | 倍數 | 區間 | 實際 CAGR | 零成本模擬 CAGR | 年拖累 | 費用率 |")
print("|---|---|---|---|---|---|---|---|")
for lev, base, k in (("SSO", "SPY", 2), ("UPRO", "SPY", 3), ("SPXL", "SPY", 3), ("QLD", "QQQ", 2), ("TQQQ", "QQQ", 3), ("SOXL", "SMH", 3)):
    for name, y in (("5y", 5), ("10y", 10), ("15y", 15)):
        a = window(px[lev], y); b = window(px[base], y).reindex(a.index).ffill()
        if len(a) < y * 250 * 0.97: continue
        sim = (1 + k * b.pct_change().fillna(0)).cumprod()
        sa, ss = stats(a), stats(sim)
        print(f"| {lev} | {base} | {k}x | {name} | {pct(sa['cagr'])} | {pct(ss['cagr'])} | {pct(sa['cagr'] - ss['cagr'])} | {meta[lev]['expense']:.2f}% |")
print()

# ---------- 4. strategies ----------
def mix(a, b, wa, rebalance="QE"):
    """Constant-mix of two series, rebalanced at period end."""
    df = pd.concat([a, b], axis=1, sort=False).dropna(); ra, rb = df.iloc[:, 0].pct_change().fillna(0), df.iloc[:, 1].pct_change().fillna(0)
    v, va, vb, out = 1.0, wa, 1 - wa, []
    marks = set(df.resample(rebalance).last().index)
    for d, x, y in zip(df.index, ra, rb):
        va *= 1 + x; vb *= 1 + y; v = va + vb
        if d in marks: va, vb = v * wa, v * (1 - wa)
        out.append(v)
    return pd.Series(out, index=df.index)


def ma_filter(lev, base, n=200, cash="BIL"):
    """Hold `lev` while `base` closes above its n-day MA, else `cash`; act next day."""
    df = pd.concat([px[lev], px[base], px[cash]], axis=1, sort=False).dropna(); df.columns = ["lev", "base", "cash"]
    on = (df["base"] > df["base"].rolling(n).mean()).shift(1).fillna(False)
    r = np.where(on, df["lev"].pct_change().fillna(0), df["cash"].pct_change().fillna(0))
    s = pd.Series((1 + r).cumprod(), index=df.index)
    trades = int(on.astype(int).diff().abs().sum())
    return s, trades


print("## 4. 策略比較（QQQ / TQQQ / SMH / SOXL 組合）\n")
STRATS = {
    "QQQ 買進持有": lambda: px["QQQ"],
    "SSO 買進持有 (2x S&P)": lambda: px["SSO"],
    "QLD 買進持有 (2x QQQ)": lambda: px["QLD"],
    "TQQQ 買進持有 (3x QQQ)": lambda: px["TQQQ"],
    "QQQ 80% + TQQQ 20%, 季再平衡": lambda: mix(px["QQQ"], px["TQQQ"], 0.8),
    "QQQ 60% + TQQQ 40%, 季再平衡": lambda: mix(px["QQQ"], px["TQQQ"], 0.6),
    "TQQQ 50% + BIL 50%, 季再平衡": lambda: mix(px["TQQQ"], px["BIL"], 0.5),
    "TQQQ 200日線濾網 (QQQ>MA200 持有, 否則 BIL)": lambda: ma_filter("TQQQ", "QQQ")[0],
    "SMH 買進持有": lambda: px["SMH"],
    "SOXL 200日線濾網 (SMH>MA200)": lambda: ma_filter("SOXL", "SMH")[0],
    "VOO 80% + SOXL 20%, 季再平衡": lambda: mix(px["VOO"], px["SOXL"], 0.8),
}
for name, y in (("5y", 5), ("10y", 10), ("15y", 15)):
    print(f"### {name}\n")
    print("| 策略 | CAGR | 年化波動 | Sharpe | 最大回撤 | 最差年 | 總報酬 |")
    print("|---|---|---|---|---|---|---|")
    rows = []
    for n, fn in STRATS.items():
        st = stats(window(fn(), y), rf_daily)
        if st and st["years"] >= y * 0.97: rows.append((st["cagr"], n, st))
    for _, n, st in sorted(rows, reverse=True):
        print(f"| {n} | {pct(st['cagr'])} | {pct(st['vol'])} | {num(st['sharpe'])} | {pct(st['maxdd'])} | {pct(st['worst_yr'])} | {pct(st['total'])} |")
    print()
_, ntr = ma_filter("TQQQ", "QQQ")
print(f"TQQQ 200 日線濾網 全期間換手次數：{ntr}（每次換手 = 一筆賣出 + 一筆買進，含稅務與滑價未計）\n")

# ---------- 5. drawdown episodes for the leveraged core ----------
print("## 5. 三次壓力測試（峰值→谷底，含股息）\n")
print("| 區間 | QQQ | QLD | TQQQ | SMH | SOXL | SPY | UPRO |")
print("|---|---|---|---|---|---|---|---|")
for lab, a, b in (("2020 COVID 2/19→3/23", "2020-02-19", "2020-03-23"), ("2022 升息 1/3→12/28", "2022-01-03", "2022-12-28"), ("2025 關稅 2/19→4/8", "2025-02-19", "2025-04-08")):
    cells = []
    for t in ("QQQ", "QLD", "TQQQ", "SMH", "SOXL", "SPY", "UPRO"):
        s = px[t][a:b]
        cells.append(pct(s.iloc[-1] / s.iloc[0] - 1) if len(s) > 5 else "—")
    print(f"| {lab} | " + " | ".join(cells) + " |")

# ---------- 6. synthetic leverage through the lost decade ----------
print("\n## 6. 合成槓桿回測 2000–2010（實際槓桿 ETF 尚未存在；用 QQQ/SPY 日報酬 ×k，再扣第 3 節量到的年拖累）\n")
print("| 合成部位 | 2000-03-10 → 2010-12-31 CAGR | 最大回撤 | 回到 2000 高點的年份 | 2000-03-10 → 今 CAGR |")
print("|---|---|---|---|---|")
DRAG = {2: 0.04, 3: 0.08}
for lab, base, k in (("QQQ ×1", "QQQ", 1), ("QLD 合成 (QQQ ×2)", "QQQ", 2), ("TQQQ 合成 (QQQ ×3)", "QQQ", 3), ("SPY ×1", "SPY", 1), ("SSO 合成 (SPY ×2)", "SPY", 2), ("UPRO 合成 (SPY ×3)", "SPY", 3)):
    b = px[base]["2000-03-10":]
    r = k * b.pct_change().fillna(0) - DRAG.get(k, 0) / 252
    s_ = (1 + r).cumprod(); s_ = s_ / s_.iloc[0]
    dec = s_[:"2010-12-31"]; st = stats(dec); st_all = stats(s_)
    rec = s_[s_.index > s_.idxmax()[:1][0] if False else s_.index[0]]
    back = s_[(s_ >= 1.0) & (s_.index > "2000-03-10")]
    first_back = back.index[back.index > dec.idxmin()].min() if len(back[back.index > dec.idxmin()]) else None
    print(f"| {lab} | {pct(st['cagr'])} | {pct(st['maxdd'])} | {first_back.year if first_back is not None else '尚未'} | {pct(st_all['cagr'])} |")
