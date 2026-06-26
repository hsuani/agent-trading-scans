#!/usr/bin/env python3
"""
Render trading-scan results as a single self-contained HTML report.

Usage:
  render_html.py <sector> <date> [--out PATH]

Reads:  /Users/yht/Study/scans/{date}/{sector}/sector_report.md
        /Users/yht/Study/scans/{date}/{TICKER}/*.md (recursive)

Output: dated HTML file, opens in browser-friendly format.
"""
import argparse
import json
import re
import sys
import warnings
from datetime import datetime
from pathlib import Path

warnings.filterwarnings("ignore")

import markdown
import yfinance as yf
from stockstats import wrap

import os as _os
# Portable root: env override, else repo root (<repo>/pipeline/tools/ → parents[2]).
SCANS_ROOT = Path(_os.environ.get("TRADING_SCANS_ROOT") or Path(__file__).resolve().parents[2])
# Per-day scan output lives under daily/<date>/.
DAILY = SCANS_ROOT / "daily"
_DBASE = DAILY if DAILY.is_dir() else SCANS_ROOT   # tolerate pre-migration root

SECTORS = {
    "semi":       ["NVDA", "AMD", "AVGO", "MRVL", "TSM", "ASML", "MU", "ARM", "CBRS"],
    "power":      ["VST", "CEG", "TLN", "GEV", "ETN", "PWR", "NEE", "SO"],
    "cooling":    ["VRT", "MOD", "ANET", "COHR", "LITE", "FN", "AAOI", "IPGP", "GLW"],
    "reit":       ["EQIX", "DLR", "IRM", "AMT"],
    "oem":        ["SMCI", "DELL", "HPE", "2317.TW", "2382.TW"],
    "security":   ["CRWD", "PANW", "ZS", "S", "OKTA"],
    "robotics":   ["TSLA", "ISRG", "ABBNY", "FANUY", "SYM", "SPAI"],
    "materials":  ["FCX", "MP", "LIN", "APD", "ALB"],
    "quantum":    ["IONQ", "RGTI", "QBTS", "QUBT", "ARQQ", "LAES", "HON", "IBM"],
    "photonics":  ["POET", "CRDO", "ALAB", "GFS", "INTC"],
    "hedge":      ["GLD", "TLT", "UUP", "SH"],
    "abf":        ["3037.TW", "8046.TW", "3189.TW"],
    "tw_cooling": ["3324.TWO", "8996.TW", "3017.TW"],
    "tw_server":  ["6669.TW", "3231.TW", "2356.TW"],
    "tw_power":   ["2308.TW", "1513.TW", "1519.TW"],
    "tw_pkg":     ["3661.TW", "8021.TW", "6438.TW"],
    "tw_photonics": ["3081.TWO", "2455.TW", "5455.TWO", "3163.TWO", "3008.TW", "4908.TWO", "3363.TWO", "4979.TWO", "4977.TW", "3711.TW", "6830.TW", "3587.TWO", "3289.TWO"],
    "tw_probe":   ["6510.TWO", "6223.TWO", "6515.TW", "6257.TW", "2449.TW", "3443.TW", "6217.TWO"],
}

MD = markdown.Markdown(extensions=["tables", "fenced_code", "nl2br"])


def md_to_html(text: str) -> str:
    MD.reset()
    return MD.convert(text or "")


def read_md(p: Path) -> str:
    if not p.exists():
        return ""
    try:
        return p.read_text(encoding="utf-8")
    except Exception as e:
        return f"<error reading {p}: {e}>"


def parse_verdict(final_decision_md: str) -> dict:
    """Extract verdict from final_decision.md."""
    out = {"verdict": "UNKNOWN", "color": "gray", "size": None, "stop": None,
           "t1": None, "t2": None, "horizon": None}
    if not final_decision_md:
        return out

    m = re.search(r"FINAL TRANSACTION PROPOSAL:\s*\*?\*?\s*(BUY|HOLD|SELL)", final_decision_md, re.I)
    if m:
        v = m.group(1).upper()
        out["verdict"] = v
        out["color"] = {"BUY": "green", "HOLD": "amber", "SELL": "red"}[v]

    # Try to pull APPROVE/MODIFY/REJECT
    m = re.search(r"Verdict:?\s*\**(APPROVE|MODIFY|REJECT|HOLD)", final_decision_md, re.I)
    if m:
        out["modify"] = m.group(1).upper()

    return out


def fetch_chart_data(ticker: str, period: str = "1y") -> dict:
    """Fetch OHLCV + indicators for embedding in HTML chart."""
    try:
        df = yf.Ticker(ticker).history(period=period, auto_adjust=True)
        if df.empty:
            return {}
        df = df.rename(columns=str.lower)
        sdf = wrap(df.copy())
        for col in ["close_20_sma", "close_50_sma", "close_200_sma", "rsi_14"]:
            _ = sdf[col]
        out = {
            "dates": [str(d.date()) for d in sdf.index],
            "close": sdf["close"].tolist(),
            "ma20":  sdf["close_20_sma"].fillna(0).tolist(),
            "ma50":  sdf["close_50_sma"].fillna(0).tolist(),
            "ma200": sdf["close_200_sma"].fillna(0).tolist(),
            "rsi":   sdf["rsi_14"].fillna(0).tolist(),
            "volume": sdf["volume"].tolist(),
        }
        return out
    except Exception as e:
        print(f"chart fetch failed for {ticker}: {e}", file=sys.stderr)
        return {}


TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Trading Scan — {sector_upper} — {date}</title>
<script src="https://cdn.tailwindcss.com"></script>
<script src="https://cdn.plot.ly/plotly-2.35.2.min.js"></script>
<style>
  body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }}
  .verdict-BUY  {{ background: #dcfce7; color: #166534; }}
  .verdict-HOLD {{ background: #fef3c7; color: #92400e; }}
  .verdict-SELL {{ background: #fee2e2; color: #991b1b; }}
  .verdict-UNKNOWN {{ background: #f3f4f6; color: #374151; }}
  details > summary {{ cursor: pointer; }}
  details[open] > summary {{ margin-bottom: 0.5rem; }}
  .agent-prose h1, .agent-prose h2, .agent-prose h3 {{ font-weight: 600; margin-top: 1rem; margin-bottom: 0.5rem; }}
  .agent-prose h1 {{ font-size: 1.5rem; }}
  .agent-prose h2 {{ font-size: 1.25rem; }}
  .agent-prose h3 {{ font-size: 1.1rem; }}
  .agent-prose p {{ margin-bottom: 0.5rem; line-height: 1.5; }}
  .agent-prose ul {{ list-style-type: disc; margin-left: 1.5rem; margin-bottom: 0.5rem; }}
  .agent-prose ol {{ list-style-type: decimal; margin-left: 1.5rem; margin-bottom: 0.5rem; }}
  .agent-prose table {{ border-collapse: collapse; margin: 0.75rem 0; font-size: 0.875rem; }}
  .agent-prose th, .agent-prose td {{ border: 1px solid #d1d5db; padding: 0.375rem 0.75rem; text-align: left; }}
  .agent-prose th {{ background: #f9fafb; font-weight: 600; }}
  .agent-prose code {{ background: #f3f4f6; padding: 0.1rem 0.25rem; border-radius: 0.25rem; font-size: 0.875rem; }}
  .agent-prose pre {{ background: #1f2937; color: #f9fafb; padding: 0.75rem; border-radius: 0.375rem; overflow-x: auto; font-size: 0.85rem; margin: 0.5rem 0; }}
  .agent-prose strong {{ font-weight: 600; }}
  nav a {{ color: #2563eb; text-decoration: none; }}
  nav a:hover {{ text-decoration: underline; }}
</style>
</head>
<body class="bg-slate-50 text-slate-900">

<header class="bg-slate-900 text-white p-6 shadow-md">
  <div class="max-w-6xl mx-auto">
    <h1 class="text-3xl font-bold">交易掃描 — {sector_upper}</h1>
    <p class="text-slate-300 text-sm mt-1">as of {date} · 產生於 {generated}</p>
  </div>
</header>

<nav class="bg-slate-100 border-b border-slate-300 p-3 sticky top-0 z-10">
  <div class="max-w-6xl mx-auto flex flex-wrap gap-3 text-sm">
    <a href="#sector-overview" class="font-semibold">族群總覽</a>
    {nav_links}
    <a href="../HOWTO_READ.html" class="ml-auto text-blue-700 hover:underline" target="_blank">📖 閱讀指南</a>
  </div>
</nav>

<main class="max-w-6xl mx-auto p-6">

  <section id="sector-overview" class="mb-10 bg-white rounded-lg shadow p-6">
    <h2 class="text-2xl font-bold mb-4">族群總覽 (Sector overview)</h2>
    <div class="agent-prose text-sm">
      {sector_html}
    </div>
  </section>

  {tickers_html}

</main>

<footer class="bg-slate-200 text-slate-600 text-xs p-4 text-center">
  多 agent 交易研究 — 純研究 / 教學用途, 非投資建議。
</footer>

</body>
</html>
"""

TICKER_TEMPLATE = r"""
<section id="ticker-{ticker_safe}" class="mb-10 bg-white rounded-lg shadow overflow-hidden">

  <div class="flex items-start justify-between p-6 border-b border-slate-200 verdict-{verdict_class}">
    <div>
      <h2 class="text-3xl font-bold">{ticker}</h2>
      <p class="text-sm mt-1 opacity-80">{ticker_desc}</p>
    </div>
    <div class="text-right">
      <div class="text-4xl font-bold">{verdict}</div>
      <div class="text-sm opacity-80 mt-1">{verdict_modify}</div>
    </div>
  </div>

  <div class="p-6 grid grid-cols-1 lg:grid-cols-2 gap-6">

    <div>
      <h3 class="text-lg font-bold mb-2">價格 + 技術指標 (2 年)</h3>
      <div id="chart-{ticker_safe}" style="height: 380px;"></div>
    </div>

    <div>
      <h3 class="text-lg font-bold mb-2">最終決策 (Final decision)</h3>
      <div class="agent-prose text-sm bg-slate-50 p-4 rounded border border-slate-200">
        {final_decision_html}
      </div>
    </div>

  </div>

  <div class="px-6 pb-6">

    <details class="mb-4 border border-slate-200 rounded">
      <summary class="bg-slate-50 px-4 py-2 font-semibold">投資計劃 (Research manager)</summary>
      <div class="agent-prose p-4 text-sm">{investment_plan_html}</div>
    </details>

    <details class="mb-4 border border-slate-200 rounded">
      <summary class="bg-slate-50 px-4 py-2 font-semibold">交易提案 (Trader)</summary>
      <div class="agent-prose p-4 text-sm">{trade_proposal_html}</div>
    </details>

    <details class="mb-4 border border-slate-200 rounded">
      <summary class="bg-slate-50 px-4 py-2 font-semibold">Phase 1 — 四 Analyst 報告</summary>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4 p-4">
        <div>
          <h4 class="font-bold text-slate-700 mb-2">基本面 (Fundamentals)</h4>
          <div class="agent-prose text-sm bg-slate-50 p-3 rounded">{fundamentals_html}</div>
        </div>
        <div>
          <h4 class="font-bold text-slate-700 mb-2">技術面 (Market / Technical)</h4>
          <div class="agent-prose text-sm bg-slate-50 p-3 rounded">{market_html}</div>
        </div>
        <div>
          <h4 class="font-bold text-slate-700 mb-2">新聞 (News)</h4>
          <div class="agent-prose text-sm bg-slate-50 p-3 rounded">{news_html}</div>
        </div>
        <div>
          <h4 class="font-bold text-slate-700 mb-2">情緒 (Sentiment)</h4>
          <div class="agent-prose text-sm bg-slate-50 p-3 rounded">{sentiment_html}</div>
        </div>
      </div>
    </details>

    <details class="mb-4 border border-slate-200 rounded">
      <summary class="bg-slate-50 px-4 py-2 font-semibold">Phase 2 — Bull vs Bear 辯論</summary>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4 p-4">
        <div>
          <h4 class="font-bold text-green-700 mb-2">🐂 多方 (Bull)</h4>
          <div class="agent-prose text-sm bg-green-50 p-3 rounded border border-green-200">{bull_html}</div>
        </div>
        <div>
          <h4 class="font-bold text-red-700 mb-2">🐻 空方 (Bear)</h4>
          <div class="agent-prose text-sm bg-red-50 p-3 rounded border border-red-200">{bear_html}</div>
        </div>
      </div>
    </details>

    <details class="mb-4 border border-slate-200 rounded">
      <summary class="bg-slate-50 px-4 py-2 font-semibold">Phase 4 — 風險辯論 (Risk debate)</summary>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4 p-4">
        <div>
          <h4 class="font-bold text-red-700 mb-2">⚡ 進攻 (Aggressive)</h4>
          <div class="agent-prose text-sm bg-red-50 p-3 rounded border border-red-200">{aggressive_html}</div>
        </div>
        <div>
          <h4 class="font-bold text-blue-700 mb-2">🛡️ 保守 (Conservative)</h4>
          <div class="agent-prose text-sm bg-blue-50 p-3 rounded border border-blue-200">{conservative_html}</div>
        </div>
        <div>
          <h4 class="font-bold text-slate-700 mb-2">⚖️ 中立 (Neutral)</h4>
          <div class="agent-prose text-sm bg-slate-100 p-3 rounded border border-slate-300">{neutral_html}</div>
        </div>
      </div>
    </details>

  </div>

  <script>
    (function() {{
      var d = {chart_data_json};
      if (!d.dates) return;
      var traces = [
        {{x: d.dates, y: d.close, name: 'Close',  line: {{color: '#1f2937', width: 2}}}},
        {{x: d.dates, y: d.ma20,  name: 'MA20',   line: {{color: '#0ea5e9', width: 1, dash: 'dot'}}}},
        {{x: d.dates, y: d.ma50,  name: 'MA50',   line: {{color: '#f59e0b', width: 1, dash: 'dot'}}}},
        {{x: d.dates, y: d.ma200, name: 'MA200',  line: {{color: '#ef4444', width: 1, dash: 'dash'}}}}
      ];
      var layout = {{
        margin: {{l: 50, r: 20, t: 10, b: 40}},
        legend: {{orientation: 'h', y: -0.15}},
        xaxis: {{showgrid: false}},
        yaxis: {{title: '價格 ($)'}}
      }};
      Plotly.newPlot('chart-{ticker_safe}', traces, layout, {{displayModeBar: false, responsive: true}});
    }})();
  </script>

</section>
"""

TICKER_DESCRIPTIONS = {
    # power
    "VST": "Vistra — nat gas + nuclear IPP",
    "CEG": "Constellation Energy — nuclear IPP, MSFT TMI PPA",
    "TLN": "Talen Energy — Susquehanna nuclear, AWS PPA",
    "GEV": "GE Vernova — gas + wind turbines + grid",
    "ETN": "Eaton — power mgmt, UPS, switchgear",
    "PWR": "Quanta Services — T&D construction",
    "NEE": "NextEra Energy — FPL + renewables",
    "SO":  "Southern Company — GA Power, Vogtle nuclear",
    # semi
    "NVDA": "NVIDIA — GPU leader",
    "AMD": "AMD — MI300/350 competitor",
    "AVGO": "Broadcom — TPU ASIC + networking",
    "MRVL": "Marvell — Amazon Trainium ASIC + DPU",
    "TSM": "TSMC — global AI chip foundry",
    "ASML": "ASML — EUV monopoly",
    "MU": "Micron — HBM3E/HBM4",
    "ARM": "Arm Holdings — IP licensing",
    # cooling/networking/optical
    "VRT": "Vertiv — liquid cooling + UPS",
    "MOD": "Modine — datacenter thermal",
    "ANET": "Arista Networks — datacenter switching",
    "COHR": "Coherent — 800G/1.6T optics + EUV laser",
    "LITE": "Lumentum — optical components",
    "FN": "Fabrinet — optical module mfg",
    "AAOI": "Applied Optoelectronics — mid-tier optics",
    "IPGP": "IPG Photonics — industrial laser",
    # reit
    "EQIX": "Equinix — colocation REIT leader",
    "DLR": "Digital Realty — hyperscale REIT",
    "IRM": "Iron Mountain — datacenter REIT pivot",
    "AMT": "American Tower — edge datacenter",
    # oem
    "SMCI": "Super Micro — AI server integrator",
    "DELL": "Dell — PowerEdge AI server",
    "HPE": "HPE — AI server + Juniper",
    "2317.TW": "Hon Hai (Foxconn) — NVDA AI server",
    "2382.TW": "Quanta Computer — AI server ODM",
    # security
    "CRWD": "CrowdStrike — endpoint AI",
    "PANW": "Palo Alto Networks — Cortex XSIAM",
    "ZS": "Zscaler — zero trust",
    "S": "SentinelOne — Singularity AI",
    "OKTA": "Okta — identity",
    # robotics
    "TSLA": "Tesla — FSD + Optimus + Dojo",
    "ISRG": "Intuitive Surgical — surgical robotics",
    "ABBNY": "ABB — industrial robotics",
    "FANUY": "Fanuc — industrial robotics",
    "SYM": "Symbotic — warehouse robotics",
    # materials
    "FCX": "Freeport-McMoRan — copper",
    "MP": "MP Materials — US rare earth",
    "LIN": "Linde — industrial gas (semi process)",
    "APD": "Air Products — industrial gas",
    "ALB": "Albemarle — lithium",
    # quantum
    "IONQ": "IonQ — trapped-ion quantum",
    "RGTI": "Rigetti — superconducting quantum",
    "QBTS": "D-Wave Quantum — quantum annealing",
    "QUBT": "Quantum Computing Inc — photonic quantum",
    "ARQQ": "Arqit Quantum — quantum encryption / QKD",
    "LAES": "SEALSQ — post-quantum semiconductors",
    "HON": "Honeywell — Quantinuum parent (~54%)",
    "IBM": "IBM — superconducting quantum + Qiskit",
    # photonics (silicon photonics / CPO pure-plays)
    "POET": "POET Technologies — silicon photonics interposer",
    "CRDO": "Credo — optical DSP / active electrical cables",
    "ALAB": "Astera Labs — connectivity / retimers (CPO-adjacent)",
    "GFS": "GlobalFoundries — silicon photonics foundry",
    "INTC": "Intel — integrated silicon photonics",
    # tw_photonics (矽光子供應鏈 上中下游 + 檢測)
    "3081.TWO": "聯亞光電 (3081) — 上游 光通訊磊晶 / 雷射",
    "2455.TW":  "全新光電 (2455) — 上游 VCSEL / 光元件磊晶片",
    "5455.TWO": "英特磊 (5455) — 上游 InP/GaAs 磊晶",
    "3163.TWO": "波若威 (3163) — 中游 光模組 (NVDA Spectrum-X 夥伴)",
    "3008.TW":  "大立光 (3008) — 中游 光纖陣列 FAU / 稜鏡準直鏡頭",
    "3711.TW":  "日月光投控 (3711) — 下游 CPO 先進封裝",
    "6830.TW":  "汎銓 (6830) — 檢測 矽光子製程分析",
    "3587.TWO": "閎康 (3587) — 檢測 材料/良率分析",
    "3289.TWO": "宜特 (3289) — 檢測 可靠度驗證",
    # 其餘 TW tickers — 中文名 (避免股號誤認)
    "3037.TW":  "欣興 (3037) — ABF 載板",
    "8046.TW":  "南電 (8046) — ABF 載板",
    "3189.TW":  "景碩 (3189) — ABF 載板",
    "3324.TWO": "雙鴻 (3324) — 散熱模組",
    "8996.TW":  "高力 (8996) — 散熱 / 熱交換器",
    "3017.TW":  "奇鋐 (3017) — 散熱模組",
    "6669.TW":  "緯穎 (6669) — AI server ODM",
    "3231.TW":  "緯創 (3231) — AI server ODM",
    "2356.TW":  "英業達 (2356) — AI server ODM",
    "3363.TWO": "上詮 (3363) — 光通訊 / FAU 精密對準 (CPO)",
    "4979.TWO": "華星光 (4979) — 光通訊 / 光收發",
    "4977.TW":  "眾達-KY (4977) — 光通訊連接器",
    "2308.TW":  "台達電 (2308) — 電源 / 電網",
    "1513.TW":  "中興電 (1513) — 重電 / 電網",
    "1519.TW":  "華城 (1519) — 重電 / 變壓器",
    "3661.TW":  "世芯-KY (3661) — 先進封裝 ASIC 設計",
    "8021.TW":  "尖點 (8021) — 先進封裝 / 探針",
    "6438.TW":  "迅得 (6438) — 先進封裝 設備",
    # tw_probe (探針測試 / IC 測試 / ASIC 服務)
    "6510.TWO": "中華精測 (6510) — 探針卡龍頭",
    "6223.TWO": "旺矽 (6223) — 探針卡 / 光電測試",
    "6515.TW":  "穎崴 (6515) — 探針卡 / test socket",
    "6257.TW":  "矽格 (6257) — IC 測試 / 封裝",
    "2449.TW":  "京元電 (2449) — IC 終測龍頭",
    "3443.TW":  "創意電子 (3443) — ASIC 設計服務 (GUC, TSMC 轉投資)",
    "6217.TWO": "中探針 (6217) — 探針 / 測試介面",
    # hedge
    "GLD": "SPDR Gold Shares ETF",
    "GDX": "VanEck Gold Miners ETF",
    "TLT": "iShares 20+ Year Treasury ETF",
    "MUB": "iShares National Muni Bond ETF",
    "UUP": "Invesco DB US Dollar Bullish ETF",
    "DBC": "Invesco DB Commodity Index ETF",
    "BTAL": "AGFiQ US Market Neutral Anti-Beta ETF",
    "SH": "ProShares Short S&P500 ETF",
}


def render_ticker_block(date: str, ticker: str) -> tuple[str, str]:
    """Returns (nav_link_html, ticker_section_html)."""
    base = _DBASE / date / ticker
    if not base.exists():
        return ("", f"<div class='bg-white p-4 mb-4 rounded shadow'>Missing data for {ticker}</div>")

    final_md = read_md(base / "final_decision.md")
    verdict_info = parse_verdict(final_md)

    fundamentals = md_to_html(read_md(base / "fundamentals.md"))
    market = md_to_html(read_md(base / "market.md"))
    news = md_to_html(read_md(base / "news.md"))
    sentiment = md_to_html(read_md(base / "sentiment.md"))

    bull_files = sorted((base / "debate").glob("round_*_bull.md")) if (base / "debate").exists() else []
    bear_files = sorted((base / "debate").glob("round_*_bear.md")) if (base / "debate").exists() else []
    bull = md_to_html("\n\n---\n\n".join(read_md(f) for f in bull_files))
    bear = md_to_html("\n\n---\n\n".join(read_md(f) for f in bear_files))

    investment_plan = md_to_html(read_md(base / "investment_plan.md"))
    trade_proposal = md_to_html(read_md(base / "trade_proposal.md"))

    rd = base / "risk_debate"
    aggressive = md_to_html(read_md(rd / "aggressive.md"))
    conservative = md_to_html(read_md(rd / "conservative.md"))
    neutral = md_to_html(read_md(rd / "neutral.md"))

    final_decision_html = md_to_html(final_md)

    chart_data = fetch_chart_data(ticker, period="2y")
    chart_json = json.dumps(chart_data)

    ticker_safe = ticker.replace(".", "_")
    ticker_desc = TICKER_DESCRIPTIONS.get(ticker, "")
    verdict = verdict_info.get("verdict", "UNKNOWN")
    verdict_modify = verdict_info.get("modify", "")

    section = TICKER_TEMPLATE.format(
        ticker=ticker,
        ticker_safe=ticker_safe,
        ticker_desc=ticker_desc,
        verdict=verdict,
        verdict_class=verdict,
        verdict_modify=verdict_modify,
        fundamentals_html=fundamentals or "<em>n/a</em>",
        market_html=market or "<em>n/a</em>",
        news_html=news or "<em>n/a</em>",
        sentiment_html=sentiment or "<em>n/a</em>",
        bull_html=bull or "<em>n/a</em>",
        bear_html=bear or "<em>n/a</em>",
        investment_plan_html=investment_plan or "<em>n/a</em>",
        trade_proposal_html=trade_proposal or "<em>n/a</em>",
        aggressive_html=aggressive or "<em>n/a</em>",
        conservative_html=conservative or "<em>n/a</em>",
        neutral_html=neutral or "<em>n/a</em>",
        final_decision_html=final_decision_html or "<em>n/a</em>",
        chart_data_json=chart_json,
    )

    nav = (f'<a href="#ticker-{ticker_safe}" '
           f'class="px-2 py-1 rounded verdict-{verdict}">{ticker}</a>')

    return (nav, section)


def render(sector: str, date: str, out_path: Path | None = None) -> Path:
    if sector not in SECTORS:
        print(f"unknown sector: {sector}; known: {list(SECTORS)}", file=sys.stderr)
        sys.exit(2)

    sector_md_path = _DBASE / date / sector / "sector_report.md"
    if not sector_md_path.exists():
        # Also try lowercase
        alt = _DBASE / date / sector.lower() / "sector_report.md"
        if alt.exists():
            sector_md_path = alt
    sector_md = read_md(sector_md_path) or f"_Sector report not found at {sector_md_path}_"
    sector_html = md_to_html(sector_md)

    nav_parts = []
    ticker_parts = []
    for tk in SECTORS[sector]:
        nav_link, ticker_section = render_ticker_block(date, tk)
        if nav_link:
            nav_parts.append(nav_link)
        ticker_parts.append(ticker_section)

    html = TEMPLATE.format(
        sector_upper=sector.upper(),
        date=date,
        generated=datetime.now().strftime("%Y-%m-%d %H:%M"),
        sector_html=sector_html,
        nav_links="\n".join(nav_parts),
        tickers_html="\n".join(ticker_parts),
    )

    if out_path is None:
        out_path = _DBASE / date / sector / f"{sector}_{date}.html"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(html, encoding="utf-8")
    return out_path


def main():
    p = argparse.ArgumentParser()
    p.add_argument("sector", choices=list(SECTORS))
    p.add_argument("date", help="YYYY-MM-DD")
    p.add_argument("--out", type=Path, help="output HTML path")
    args = p.parse_args()
    out = render(args.sector, args.date, args.out)
    print(str(out))


if __name__ == "__main__":
    main()
