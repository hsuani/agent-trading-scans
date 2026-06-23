#!/usr/bin/env python3
"""
Technical-analysis CLI for Claude Code subagents.

Computes indicators from yfinance OHLCV, returns JSON. Avoids LLM doing
arithmetic on raw price arrays.

Usage:
  ta.py <ticker> <indicator> [--period 1y]

Indicators:
  snapshot   single dict: price, MA20/50/200, MACD, RSI14, BB%, ATR14,
             20d vol, 52w hi/lo, distance to MA, momentum 1m/3m/6m/12m
  series     full DataFrame with all indicators (longer output)
  levels     S/R levels via recent local min/max
"""
import argparse
import json
import sys
import warnings

warnings.filterwarnings("ignore")

import yfinance as yf  # noqa: E402
import pandas as pd  # noqa: E402
from stockstats import wrap  # noqa: E402


def fetch(ticker, period):
    df = yf.Ticker(ticker).history(period=period, auto_adjust=True)
    if df.empty:
        raise RuntimeError(f"no history for {ticker}")
    df = df.rename(columns=str.lower)
    return df


def compute(df):
    sdf = wrap(df.copy())
    cols = [
        "close_20_sma", "close_50_sma", "close_200_sma",
        "macd", "macds", "macdh",
        "rsi_14",
        "boll", "boll_ub", "boll_lb",
        "atr_14",
    ]
    for c in cols:
        _ = sdf[c]
    out = sdf
    out["mom_1m"] = out["close"].pct_change(21)
    out["mom_3m"] = out["close"].pct_change(63)
    out["mom_6m"] = out["close"].pct_change(126)
    out["mom_12m"] = out["close"].pct_change(252)
    out["vol_20d_annualized"] = out["close"].pct_change().rolling(20).std() * (252 ** 0.5)
    return out


def snapshot(out):
    last = out.iloc[-1]
    px = float(last["close"])
    ma20 = float(last["close_20_sma"])
    ma50 = float(last["close_50_sma"])
    ma200 = float(last["close_200_sma"]) if not pd.isna(last["close_200_sma"]) else None
    hi52 = float(out["high"].tail(252).max())
    lo52 = float(out["low"].tail(252).min())
    return {
        "as_of": str(out.index[-1].date()),
        "price": px,
        "ma20": ma20, "ma50": ma50, "ma200": ma200,
        "pct_to_ma20": (px / ma20 - 1) if ma20 else None,
        "pct_to_ma50": (px / ma50 - 1) if ma50 else None,
        "pct_to_ma200": (px / ma200 - 1) if ma200 else None,
        "macd": float(last["macd"]),
        "macd_signal": float(last["macds"]),
        "macd_hist": float(last["macdh"]),
        "rsi14": float(last["rsi_14"]),
        "bb_mid": float(last["boll"]),
        "bb_upper": float(last["boll_ub"]),
        "bb_lower": float(last["boll_lb"]),
        "bb_pct": (px - float(last["boll_lb"])) / (float(last["boll_ub"]) - float(last["boll_lb"]))
                  if last["boll_ub"] != last["boll_lb"] else None,
        "atr14": float(last["atr_14"]),
        "vol_20d_annualized": float(last["vol_20d_annualized"]) if not pd.isna(last["vol_20d_annualized"]) else None,
        "mom_1m": float(last["mom_1m"]) if not pd.isna(last["mom_1m"]) else None,
        "mom_3m": float(last["mom_3m"]) if not pd.isna(last["mom_3m"]) else None,
        "mom_6m": float(last["mom_6m"]) if not pd.isna(last["mom_6m"]) else None,
        "mom_12m": float(last["mom_12m"]) if not pd.isna(last["mom_12m"]) else None,
        "hi52w": hi52, "lo52w": lo52,
        "pct_from_52w_high": px / hi52 - 1 if hi52 else None,
        "pct_from_52w_low":  px / lo52 - 1 if lo52 else None,
    }


def levels(out, lookback=120, window=10):
    sub = out.tail(lookback)
    highs, lows = [], []
    for i in range(window, len(sub) - window):
        slc = sub.iloc[i - window:i + window + 1]
        if sub.iloc[i]["high"] == slc["high"].max():
            highs.append((str(sub.index[i].date()), float(sub.iloc[i]["high"])))
        if sub.iloc[i]["low"] == slc["low"].min():
            lows.append((str(sub.index[i].date()), float(sub.iloc[i]["low"])))
    return {"resistance": highs[-5:], "support": lows[-5:]}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("ticker")
    p.add_argument("indicator", choices=["snapshot", "series", "levels"])
    p.add_argument("--period", default="1y")
    args = p.parse_args()

    df = fetch(args.ticker, args.period)
    out = compute(df)

    if args.indicator == "snapshot":
        print(json.dumps(snapshot(out), indent=2, default=str))
    elif args.indicator == "levels":
        print(json.dumps(levels(out), indent=2, default=str))
    elif args.indicator == "series":
        keep = [
            "open", "high", "low", "close", "volume",
            "close_20_sma", "close_50_sma", "close_200_sma",
            "macd", "macds", "macdh", "rsi_14",
            "boll", "boll_ub", "boll_lb", "atr_14",
        ]
        slim = out[keep].tail(60).reset_index()
        slim["Date"] = slim["Date"].astype(str) if "Date" in slim.columns else slim.iloc[:, 0].astype(str)
        print(json.dumps(json.loads(slim.to_json(orient="records", date_format="iso")), indent=2))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(json.dumps({"error": type(e).__name__, "message": str(e)}), file=sys.stderr)
        sys.exit(1)
