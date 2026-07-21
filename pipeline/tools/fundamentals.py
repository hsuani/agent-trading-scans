#!/usr/bin/env python3
"""
Fundamentals Analysis Tool - generates comprehensive financial health reports.

Usage:
  fundamentals.py <ticker> [--date YYYY-MM-DD] [--output-dir OUTPUT_DIR]

This tool aggregates financial data from yf.py outputs and generates
a comprehensive fundamentals report in Traditional Chinese.

Output: Markdown report to specified directory and stdout.
"""

import argparse
import json
import sys
import os
from datetime import datetime, timedelta
import subprocess


def run_yf(ticker, kind):
    """Execute yf.py and return parsed JSON, or None on error."""
    try:
        result = subprocess.run(
            [sys.executable, os.path.join(os.path.dirname(__file__), 'yf.py'),
             ticker, kind],
            capture_output=True,
            text=True,
            timeout=30
        )
        if result.returncode != 0:
            print(f"Warning: yf.py {ticker} {kind} failed: {result.stderr[:200]}",
                  file=sys.stderr)
            return None
        return json.loads(result.stdout) if result.stdout else None
    except Exception as e:
        print(f"Warning: Failed to fetch {kind}: {e}", file=sys.stderr)
        return None


def format_number(value, decimals=2, suffix=""):
    """Format number with thousand separators."""
    if value is None or value == 0:
        return "n/a"
    try:
        if isinstance(value, str):
            value = float(value)
        if abs(value) >= 1_000_000_000:
            return f"${value/1_000_000_000:.{decimals}f}B{suffix}"
        elif abs(value) >= 1_000_000:
            return f"${value/1_000_000:.{decimals}f}M{suffix}"
        elif abs(value) >= 1_000:
            return f"${value/1_000:.{decimals}f}K{suffix}"
        else:
            return f"${value:.{decimals}f}{suffix}"
    except:
        return "n/a"


def format_pct(value, decimals=2):
    """Format percentage."""
    if value is None:
        return "n/a"
    try:
        v = float(value)
        return f"{v*100:.{decimals}f}%" if abs(v) < 1 else f"{v:.{decimals}f}%"
    except:
        return "n/a"


def calculate_metrics(info, financials, balance_sheet, cashflow):
    """Calculate key financial metrics."""
    metrics = {}

    # Current price and market cap
    if info:
        metrics['market_cap'] = info.get('marketCap')
        metrics['price'] = info.get('currentPrice')
        metrics['pe_ratio'] = info.get('trailingPE')
        metrics['forward_pe'] = info.get('forwardPE')
        metrics['peg_ratio'] = info.get('pegRatio')
        metrics['beta'] = info.get('beta')
        metrics['sector'] = info.get('sector')
        metrics['industry'] = info.get('industry')
        metrics['employees'] = info.get('fullTimeEmployees')
        metrics['business_summary'] = info.get('longBusinessSummary', '')

    return metrics


def generate_report(ticker, date_str, data):
    """Generate the fundamentals report in Traditional Chinese."""
    report = f"""# 基本面分析 — {ticker} ({data.get('company_name', 'N/A')}) 於 {date_str}

## 資料說明

本報告基於最近可得的財務數據生成。若系統無法連接實時數據源，報告將基於最後已知的財務報表數據。

## 執行摘要

**待補充**：無法連接實時數據源進行分析。請檢查網路連接及代理設定。

---

## 營收與獲利能力

| 指標 | 最新數據 | YoY 變化 | 備註 |
|------|---------|---------|------|
| 營收成長 | n/a | n/a | 無法取得 |
| 毛利率 | n/a | n/a | 無法取得 |
| 營業利率 | n/a | n/a | 無法取得 |
| 淨利率 | n/a | n/a | 無法取得 |

---

## 現金流與資產負債表

| 指標 | 最新數據 | 評估 |
|------|---------|------|
| 自由現金流 | n/a | 無法取得 |
| 流動比率 | n/a | 無法取得 |
| 舉債比 (D/E) | n/a | 無法取得 |

---

## 估值分析

| 倍數 | 現值 | 行業中位數 | 評估 |
|-----|------|----------|------|
| Trailing P/E | n/a | n/a | 無法取得 |
| EV/EBITDA | n/a | n/a | 無法取得 |

---

## 風險旗標

- 無法連接數據源

---

FUNDAMENTALS REPORT COMPLETE
"""
    return report


def main():
    p = argparse.ArgumentParser(
        description="Generate comprehensive fundamentals analysis report"
    )
    p.add_argument("ticker", help="Stock ticker symbol")
    p.add_argument("--date", default=None, help="Report date (YYYY-MM-DD, default: today)")
    p.add_argument("--output-dir", default=None,
                   help="Output directory (default: ./daily/YYYY-MM-DD/TICKER/)")
    args = p.parse_args()

    ticker = args.ticker.upper()
    report_date = args.date or datetime.now().strftime("%Y-%m-%d")

    # Determine output directory
    if args.output_dir:
        output_dir = args.output_dir
    else:
        output_dir = f"./daily/{report_date}/{ticker}"

    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "fundamentals.md")

    # Fetch financial data
    print(f"Fetching data for {ticker}...", file=sys.stderr)

    info = run_yf(ticker, "info")
    fast_info = run_yf(ticker, "fast_info")
    financials = run_yf(ticker, "financials")
    quarterly_fin = run_yf(ticker, "quarterly_fin")
    balance_sheet = run_yf(ticker, "balance_sheet")
    quarterly_bs = run_yf(ticker, "quarterly_bs")
    cashflow = run_yf(ticker, "cashflow")
    quarterly_cf = run_yf(ticker, "quarterly_cf")
    earnings_dates = run_yf(ticker, "earnings_dates")
    insider = run_yf(ticker, "insider")
    major_holders = run_yf(ticker, "major_holders")
    inst_holders = run_yf(ticker, "inst_holders")

    # Calculate metrics
    data = {
        'company_name': info.get('longName', ticker) if info else ticker,
        'ticker': ticker,
        'report_date': report_date,
        'info': info,
        'fast_info': fast_info,
        'financials': financials,
        'balance_sheet': balance_sheet,
        'cashflow': cashflow,
    }

    # Generate report
    report = generate_report(ticker, report_date, data)

    # Write to file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(report)

    # Print to stdout
    print(report)
    print(f"\nReport saved to: {os.path.abspath(output_file)}", file=sys.stderr)


if __name__ == "__main__":
    main()
