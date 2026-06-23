#!/usr/bin/env python3
"""
yfinance CLI for Claude Code subagents.

Usage:
  yf.py <ticker> <kind> [--period 1y] [--start YYYY-MM-DD] [--end YYYY-MM-DD] [--limit N]

Kinds:
  info             company profile + key stats (P/E, mkt cap, beta, ...)
  fast_info        slim quote (price, prev close, mkt cap, currency)
  history          OHLCV (use --period or --start/--end)
  financials       income statement (annual)
  quarterly_fin    income statement (quarterly)
  balance_sheet    annual BS
  quarterly_bs     quarterly BS
  cashflow         annual CF
  quarterly_cf     quarterly CF
  earnings_dates   upcoming + recent earnings (date, EPS est, actual)
  recommendations  analyst ratings history
  rec_summary      buy/hold/sell counts current
  insider          insider transactions
  major_holders    top shareholder concentration
  inst_holders     institutional holders
  news             ticker news (limit N, default 20)
  options          option expirations + chain (need --date YYYY-MM-DD for chain)
  splits           historical splits
  dividends        dividend history
  actions          splits + dividends combined

Output: JSON to stdout. Errors to stderr, exit 1.
"""
import argparse
import json
import sys
import warnings

warnings.filterwarnings("ignore")

import yfinance as yf  # noqa: E402


def _df(df):
    if df is None:
        return None
    try:
        if df.empty:
            return []
    except AttributeError:
        return df
    df = df.reset_index()
    df.columns = [str(c) for c in df.columns]
    return json.loads(df.to_json(orient="records", date_format="iso"))


def main():
    p = argparse.ArgumentParser(description="yfinance CLI for subagents")
    p.add_argument("ticker")
    p.add_argument(
        "kind",
        choices=[
            "info", "fast_info", "history",
            "financials", "quarterly_fin",
            "balance_sheet", "quarterly_bs",
            "cashflow", "quarterly_cf",
            "earnings_dates", "recommendations", "rec_summary",
            "insider", "major_holders", "inst_holders",
            "news", "options", "splits", "dividends", "actions",
        ],
    )
    p.add_argument("--period", default="1y")
    p.add_argument("--start")
    p.add_argument("--end")
    p.add_argument("--date", help="option expiration YYYY-MM-DD (kind=options)")
    p.add_argument("--limit", type=int, default=20)
    args = p.parse_args()

    t = yf.Ticker(args.ticker)
    k = args.kind

    if k == "info":
        out = t.info
    elif k == "fast_info":
        fi = t.fast_info
        out = {key: getattr(fi, key, None) for key in [
            "last_price", "previous_close", "open", "day_high", "day_low",
            "fifty_day_average", "two_hundred_day_average",
            "year_high", "year_low", "market_cap", "currency",
            "exchange", "quote_type", "shares", "ten_day_average_volume",
        ]}
    elif k == "history":
        kw = {"period": args.period} if not (args.start or args.end) else {}
        if args.start: kw["start"] = args.start
        if args.end: kw["end"] = args.end
        out = _df(t.history(**kw))
    elif k == "financials":
        out = _df(t.financials)
    elif k == "quarterly_fin":
        out = _df(t.quarterly_financials)
    elif k == "balance_sheet":
        out = _df(t.balance_sheet)
    elif k == "quarterly_bs":
        out = _df(t.quarterly_balance_sheet)
    elif k == "cashflow":
        out = _df(t.cashflow)
    elif k == "quarterly_cf":
        out = _df(t.quarterly_cashflow)
    elif k == "earnings_dates":
        out = _df(t.earnings_dates)
    elif k == "recommendations":
        out = _df(t.recommendations)
    elif k == "rec_summary":
        out = _df(t.recommendations_summary) if hasattr(t, "recommendations_summary") else _df(t.recommendations)
    elif k == "insider":
        out = _df(t.insider_transactions)
    elif k == "major_holders":
        out = _df(t.major_holders)
    elif k == "inst_holders":
        out = _df(t.institutional_holders)
    elif k == "news":
        news = t.news or []
        out = news[: args.limit]
    elif k == "options":
        exps = list(t.options)
        if args.date:
            chain = t.option_chain(args.date)
            out = {
                "expiration": args.date,
                "calls": _df(chain.calls),
                "puts":  _df(chain.puts),
            }
        else:
            out = {"expirations": exps}
    elif k == "splits":
        out = _df(t.splits.reset_index() if hasattr(t.splits, "reset_index") else t.splits)
    elif k == "dividends":
        out = _df(t.dividends.reset_index() if hasattr(t.dividends, "reset_index") else t.dividends)
    elif k == "actions":
        out = _df(t.actions)
    else:
        print(f"unknown kind: {k}", file=sys.stderr)
        sys.exit(1)

    print(json.dumps(out, default=str, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(json.dumps({"error": type(e).__name__, "message": str(e)}), file=sys.stderr)
        sys.exit(1)
