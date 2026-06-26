#!/usr/bin/env python3
"""
Aggregate all latest sector scans → single interactive dashboard.html.

Walks /Users/yht/Study/scans/{DATE}/{SECTOR}/sector_report.md and each
ticker's final_decision.md, parses key fields (verdict, entry, stop,
T1/T2, size, triggers), embeds the whole thing as a JSON payload into
a self-contained HTML page that:

  - Lists every ticker grouped by sector
  - Color-codes verdict (BUY/HOLD/SELL)
  - Lets user check / uncheck "armed" status per ticker
  - Lets user record trade entries (size, price, time) per ticker
  - Persists everything to localStorage (no server)
  - Shows "next step" message based on current state
  - Provides "arm all triggers" / "disarm all" bulk actions
  - Links to per-sector full HTML report and catalyst calendar

Run after each sector scan or via launchd post-step.
"""
import json
import re
from datetime import date, datetime
from pathlib import Path

import os as _os
# Portable root: env override, else repo root (<repo>/pipeline/tools/ → parents[2]).
SCANS = Path(_os.environ.get("TRADING_SCANS_ROOT") or Path(__file__).resolve().parents[2])
# Per-day scan output lives under daily/<date>/. dashboard.html, _catalysts.json,
# alerts.json and the doc HTMLs stay at the SCANS root.
DAILY = SCANS / "daily"


def _date_dirs():
    """Yield date-named dirs from daily/ (tolerating a missing daily/ → root)."""
    base = DAILY if DAILY.is_dir() else SCANS
    for d in base.iterdir():
        if d.is_dir() and re.fullmatch(r"\d{4}-\d{2}-\d{2}", d.name):
            yield d


OUT = SCANS / "dashboard.html"

SECTOR_LABELS = {
    "semi":       "A. 半導體核心",
    "power":      "B. 電力 / 電網",
    "cooling":    "C. 散熱 / 網通 / 光通訊",
    "reit":       "D. 資料中心 REIT",
    "oem":        "E. AI 伺服器 OEM (US+TW)",
    "security":   "F. AI 安全",
    "robotics":   "G. 機器人 / 自駕",
    "materials":  "H. 原料 / 稀土",
    "hedge":      "I. 避險",
    "abf":        "J. ABF 載板 (TW)",
    "tw_cooling": "K. 散熱模組 (TW)",
    "tw_server":  "L. AI server ODM (TW)",
    "tw_power":   "N. 電源 / 電網 (TW)",
    "tw_pkg":     "O. 先進封裝 (TW)",
    "quantum":    "P. 量子運算 (incl. Quantinuum=HON)",
    "photonics":  "Q. 矽光子 (US pure-play)",
    "tw_photonics": "R. 矽光子供應鏈 上中下游+檢測 (TW)",
    "tw_probe":   "S. 探針測試 / IC 測試 / ASIC 服務 (TW)",
}

SECTORS_ORDER = list(SECTOR_LABELS.keys())


def latest_scan_for_sector(sector: str) -> Path | None:
    """Find the most recent date dir that has scans/{date}/{sector}/sector_report.md."""
    candidates = []
    for d in _date_dirs():
        rpt = d / sector / "sector_report.md"
        if rpt.exists():
            candidates.append((d.name, d))
    if not candidates:
        return None
    candidates.sort(reverse=True)
    return candidates[0][1]


def parse_final_decision(text: str) -> dict:
    """Best-effort parse of a final_decision.md (Chinese or English)."""
    out = {
        "verdict": "UNKNOWN",
        "modify":  "",
        "entry":   "",
        "stop":    "",
        "t1":      "",
        "t2":      "",
        "size":    "",
        "horizon": "",
        "triggers": [],
        "monitoring": "",
        "raw_preview": "",
    }
    if not text:
        return out

    out["raw_preview"] = text[:400]

    # Verdict appears in several formats across agent outputs:
    #   "FINAL TRANSACTION PROPOSAL: **BUY**"  /  "## VERDICT: BUY"  /  "VERDICT：HOLD"
    for _vpat in (r"FINAL TRANSACTION PROPOSAL[:：]\s*\*{0,2}\s*(BUY|HOLD|SELL)",
                  r"VERDICT[:：]\s*\*{0,2}\s*(BUY|HOLD|SELL)"):
        m = re.search(_vpat, text, re.I)
        if m:
            out["verdict"] = m.group(1).upper()
            break

    # MODIFY/APPROVE/REJECT
    m = re.search(r"(APPROVE|MODIFY|REJECT)", text)
    if m:
        out["modify"] = m.group(1)

    # Trade card lines (markdown table or bullet-like)
    def grab(pattern: str) -> str:
        m = re.search(pattern, text, re.I)
        return m.group(1).strip().rstrip(" ,") if m else ""

    # SEP tolerates markdown bold (**進場**:) between label and colon.
    SEP = r"\s*\*{0,2}\s*[:：\|]"
    out["entry"]   = grab(r"(?:Entry zone|Entry|進場區?間?|進場)" + SEP + r"\s*([^\n|]+)")
    out["stop"]    = grab(r"(?:Stop[- ]loss|Stop|停損|止損)" + SEP + r"\s*([^\n|]+)")
    out["size"]    = grab(r"(?:Size|尺寸|倉位|大小)" + SEP + r"\s*([^\n|]+)")
    out["horizon"] = grab(r"(?:Horizon|時間範圍|時間框架|持有期|期限|時程)" + SEP + r"\s*([^\n|]+)")
    # T1/T2 may be on their own line ("目標1: $78") OR combined on one
    # "目標: T1 $78 / T2 $105" line where the value follows a space, not a
    # colon. Make the separator optional and stop the capture at "/" or ",".
    out["t1"]      = grab(r"(?:Target ?1|T1|目標 ?1|目標一)" + SEP + r"?\s*\$?\s*([0-9][^\n/|，,（(]*)")
    out["t2"]      = grab(r"(?:Target ?2|T2|目標 ?2|目標二)" + SEP + r"?\s*\$?\s*([0-9][^\n/|，,（(]*)")

    # Trade-card markdown TABLE fallback: rows like "| **Target 1 (T1)** | $237 |"
    # defeat the line regexes (parenthetical "(T1)" sits between label and value,
    # value in a separate cell). Parse table rows generically and fill any field
    # still empty. Price fields require the value to start with $/digit so R:R
    # formula rows ("($237 − $228)/…") and notes don't leak in.
    _PRICE = ("entry", "stop", "t1", "t2")
    _TABLE_KW = [
        ("entry",   ("進場", "entry", "建倉", "buy zone", "進場區間", "進場價")),
        ("stop",    ("止損", "停損", "stop")),
        ("t1",      ("target 1", "t1", "目標1", "目標 1", "目標一")),
        ("t2",      ("target 2", "t2", "目標2", "目標 2", "目標二")),
        ("size",    ("倉位", "position", "size", "nav", "部位")),
        ("horizon", ("時間", "horizon", "持有", "期限", "時程", "時間框架")),
    ]
    for line in text.splitlines():
        if line.count("|") < 2:
            continue
        cells = [c.strip().strip("*").strip() for c in line.split("|") if c.strip()]
        if len(cells) < 2:
            continue
        label, value = cells[0].lower(), cells[1]
        if set(value) <= set("-: "):   # skip header separator rows
            continue
        for field, kws in _TABLE_KW:
            if out[field] or not any(kw in label for kw in kws):
                continue
            if field in _PRICE and not re.match(r"^[\$0-9]", value):
                continue
            out[field] = value.rstrip(" ,")
            break

    # Triggers — collect lines mentioning "trigger" / "觸發" / "若 ... 則"
    triggers = []
    for line in text.splitlines():
        s = line.strip().lstrip("-* ").rstrip()
        if not s or len(s) > 280:
            continue
        if re.search(r"(trigger|觸發|若.*則|破 ?\$|跌破|突破|reclaim|站上|站穩|invalidat|失效)",
                     s, re.I):
            triggers.append(s)
    out["triggers"] = triggers[:8]

    # Monitoring trigger
    mon = grab(r"(?:Monitoring trigger|監控觸發|監測觸發)\s*[:：\|]\s*([^\n]+)")
    if mon:
        out["monitoring"] = mon

    return out


def parse_sector_report(text: str) -> dict:
    """Pull the ranking table + top pick from sector_report.md."""
    out = {"top_pick": "", "contrarian": "", "pairs": "", "risk_budget": ""}
    if not text:
        return out

    def grab(pat: str) -> str:
        m = re.search(pat, text, re.I)
        return m.group(1).strip()[:160] if m else ""

    out["top_pick"]    = grab(r"(?:Top pick|Consensus top pick|共識首選)[\s\S]{0,300}?\*\*([A-Z\.]+)\*\*")
    out["contrarian"]  = grab(r"(?:Contrarian pick|逆向選股|反向首選)[\s\S]{0,300}?\*\*([A-Z\.]+)\*\*")
    out["pairs"]       = grab(r"(?:Pairs trade|配對交易|對沖交易)([\s\S]{0,200})")
    out["risk_budget"] = grab(r"(?:Sector risk budget|Risk budget|風險預算)([\s\S]{0,200})")

    return out


def collect_ticker_history(ticker: str) -> dict:
    """Walk all dated scans/ dirs and collect any final_decision.md for this ticker.
    Returns {date: card_dict} ordered ascending."""
    history = {}
    for d in sorted(_date_dirs()):
        final = d / ticker / "final_decision.md"
        if not final.exists():
            continue
        try:
            text = final.read_text(encoding="utf-8", errors="ignore")
            card = parse_final_decision(text)
            card["scan_date"] = d.name
            # Drop bulky fields from history to keep payload small
            card.pop("raw_preview", None)
            card.pop("triggers", None)
            history[d.name] = card
        except Exception:
            continue
    return history


def parse_conviction(text: str) -> int:
    """Parse confidence % from final_decision.md. Returns 0-100."""
    if not text:
        return 50
    # Match "信心度 X%" / "conviction X%" / "信心 X%"
    m = re.search(r"(?:conviction|信心(?:度)?)[^0-9]{0,30}(\d{1,3})\s*%", text, re.I)
    if m:
        return int(m.group(1))
    # Match "MEDIUM (62%)" — first %-pattern in early lines
    head = text[:1500]
    m = re.search(r"\((\d{2,3})\s*%\)", head)
    if m:
        v = int(m.group(1))
        if 30 <= v <= 100:
            return v
    return 50


def parse_rr(text: str) -> float:
    """Parse R:R to T2 if any. Returns ratio (default 1.5)."""
    if not text:
        return 1.5
    # Match "R:R T2 = 2.7" or "T2 R:R 3.0" or "R:R to T2 ≈ 2.70" or "T2 = 3.5x"
    patterns = [
        r"R[:\s]?R[\s\(\)]*(?:to\s+)?T2[^\d]{0,20}(\d+(?:\.\d+)?)",
        r"T2[^\d\n]{0,15}R[:\s]?R[^\d]{0,5}(\d+(?:\.\d+)?)",
        r"T2[^\n]{0,40}?(\d+(?:\.\d+)?)\s*[xX×]",
    ]
    for p in patterns:
        m = re.search(p, text)
        if m:
            try:
                v = float(m.group(1))
                if 0.2 <= v <= 20:
                    return v
            except ValueError:
                continue
    return 1.5


def is_phase1_only(text: str) -> bool:
    if not text:
        return False
    return bool(re.search(r"PHASE 1 ONLY|Phase-1-only|跳過.*Top\s*\d", text, re.I))


def compute_score(card: dict, text: str) -> tuple[float, int, float, bool]:
    """Score a ticker for Top 20 ranking. Returns (score, conviction%, rr_t2, phase1_only)."""
    v = (card.get("verdict") or "UNKNOWN").upper()
    weight = {"BUY": 1.0, "SELL": 0.65, "HOLD": 0.3, "UNKNOWN": 0.05}.get(v, 0.05)
    conf = parse_conviction(text)
    rr = parse_rr(text)
    phase1 = is_phase1_only(text)
    modifier = 0.35 if phase1 else 1.0
    # Score: verdict * conviction * (1 + rr/5) * phase modifier
    score = weight * conf * (1 + min(rr, 5) / 5) * modifier
    return round(score, 1), conf, rr, phase1


def compute_top20(sectors_data: dict) -> list:
    """Rank all tickers across sectors. Return top 20 by composite score."""
    ranked = []
    for sector, sd in sectors_data.items():
        for t in sd.get("tickers", []):
            # Re-read final_decision text for scoring
            scan_date = t.get("scan_date")
            ticker = t.get("ticker")
            final_md = DAILY / scan_date / ticker / "final_decision.md"
            text = ""
            if final_md.exists():
                try:
                    text = final_md.read_text(encoding="utf-8", errors="ignore")
                except Exception:
                    text = ""
            score, conf, rr, phase1 = compute_score(t, text)
            ranked.append({
                "ticker":       ticker,
                "sector":       sector,
                "sector_label": SECTOR_LABELS.get(sector, sector),
                "verdict":      t.get("verdict", "UNKNOWN"),
                "modify":       t.get("modify", ""),
                "scan_date":    scan_date,
                "entry":        t.get("entry", "-"),
                "stop":         t.get("stop", "-"),
                "t1":           t.get("t1", "-"),
                "t2":           t.get("t2", "-"),
                "size":         t.get("size", "-"),
                "horizon":      t.get("horizon", "-"),
                "report_url":   t.get("report_url", ""),
                "score":        score,
                "conviction":   conf,
                "rr_t2":        rr,
                "phase1_only":  phase1,
            })
    ranked.sort(key=lambda x: (x["score"], x["conviction"]), reverse=True)
    return ranked[:20]


def collect_payload() -> dict:
    """Walk scans/ and assemble the full dashboard data payload."""
    from collections import OrderedDict
    SECTOR_TICKERS = OrderedDict([
        ("semi",       ["NVDA", "AMD", "AVGO", "MRVL", "TSM", "ASML", "MU", "ARM", "CBRS"]),
        ("power",      ["VST", "CEG", "TLN", "GEV", "ETN", "PWR", "NEE", "SO"]),
        ("cooling",    ["VRT", "MOD", "ANET", "COHR", "LITE", "FN", "AAOI", "IPGP", "GLW"]),
        ("reit",       ["EQIX", "DLR", "IRM", "AMT"]),
        ("oem",        ["SMCI", "DELL", "HPE", "2317.TW", "2382.TW"]),
        ("security",   ["CRWD", "PANW", "ZS", "S", "OKTA"]),
        ("robotics",   ["TSLA", "ISRG", "ABBNY", "FANUY", "SYM", "SPAI"]),
        ("materials",  ["FCX", "MP", "LIN", "APD", "ALB"]),
        ("quantum",    ["IONQ", "RGTI", "QBTS", "QUBT", "ARQQ", "LAES", "HON", "IBM"]),
        ("photonics",  ["POET", "CRDO", "ALAB", "GFS", "INTC"]),
        ("hedge",      ["GLD", "TLT", "UUP", "SH"]),
        ("abf",        ["3037.TW", "8046.TW", "3189.TW"]),
        ("tw_cooling", ["3324.TWO", "8996.TW", "3017.TW"]),
        ("tw_server",  ["6669.TW", "3231.TW", "2356.TW"]),
        ("tw_power",   ["2308.TW", "1513.TW", "1519.TW"]),
        ("tw_pkg",     ["3661.TW", "8021.TW", "6438.TW"]),
        ("tw_photonics", ["3081.TWO", "2455.TW", "5455.TWO", "3163.TWO", "3008.TW", "4908.TWO", "3363.TWO", "4979.TWO", "4977.TW", "3711.TW", "6830.TW", "3587.TWO", "3289.TWO"]),
        ("tw_probe",   ["6510.TWO", "6223.TWO", "6515.TW", "6257.TW", "2449.TW", "3443.TW", "6217.TWO"]),
    ])

    sectors_data = {}
    for sector in SECTORS_ORDER:
        scan_dir = latest_scan_for_sector(sector)
        if scan_dir is None:
            continue
        sector_report = scan_dir / sector / "sector_report.md"
        sr_text = sector_report.read_text(encoding="utf-8", errors="ignore") if sector_report.exists() else ""

        tickers = []
        # Only include tickers that belong to THIS sector (per SECTOR_TICKERS map).
        # For each ticker, use the LATEST scan that has a final_decision.md,
        # which may be newer than the sector_report.md date (e.g. ad-hoc
        # single-ticker scan of CBRS post sector run).
        for tname in SECTOR_TICKERS.get(sector, []):
            history = collect_ticker_history(tname)  # {date: card}
            if not history:
                continue
            latest_date = sorted(history.keys())[-1]
            # Find the sector_report HTML matching that ticker's scan_date
            # (may differ from sector_scan_dir.name if ad-hoc); fall back to
            # the sector scan_dir.
            ticker_scan_dir = DAILY / latest_date
            data = history[latest_date].copy()
            data["ticker"] = tname
            data["scan_date"] = latest_date
            # Report URL: prefer same-date sector html, else latest sector html
            same_date_sector_html = ticker_scan_dir / sector / f"{sector}_{latest_date}.html"
            if same_date_sector_html.exists():
                data["report_url"] = f"./daily/{latest_date}/{sector}/{sector}_{latest_date}.html#ticker-{tname.replace('.', '_')}"
            else:
                data["report_url"] = f"./daily/{scan_dir.name}/{sector}/{sector}_{scan_dir.name}.html#ticker-{tname.replace('.', '_')}"
            data["history"] = history
            tickers.append(data)

        sectors_data[sector] = {
            "label":       SECTOR_LABELS.get(sector, sector),
            "scan_date":   scan_dir.name,
            "report_url":  f"./daily/{scan_dir.name}/{sector}/{sector}_{scan_dir.name}.html",
            "sector_meta": parse_sector_report(sr_text),
            "tickers":     tickers,
        }

    # Pull catalyst calendar if present
    cat_file = SCANS / "_catalysts.json"
    catalysts = {}
    if cat_file.exists():
        try:
            cat_data = json.loads(cat_file.read_text(encoding="utf-8"))
            # Just keep next 30 upcoming events per ticker
            from collections import defaultdict
            today = date.today().isoformat()
            by_ticker = defaultdict(list)
            for c in cat_data.get("all", []):
                if c["date"] >= today:
                    by_ticker[c["ticker"]].append({
                        "date": c["date"], "category": c["category"],
                        "desc": (c["description"][:160] + "…") if len(c["description"]) > 160 else c["description"],
                    })
            for t in by_ticker:
                by_ticker[t] = sorted(by_ticker[t], key=lambda x: x["date"])[:8]
            catalysts = dict(by_ticker)
        except Exception:
            catalysts = {}

    top20 = compute_top20(sectors_data)

    return {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "today":        date.today().isoformat(),
        "sectors":      sectors_data,
        "catalysts":    catalysts,
        "top20":        top20,
    }


HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<title>Trading Dashboard — 互動式</title>
<script src="https://cdn.tailwindcss.com"></script>
<style>
  body { font-family: "PingFang TC", -apple-system, BlinkMacSystemFont, "Microsoft JhengHei", sans-serif; }
  .v-BUY  { background: #dcfce7; color: #166534; }
  .v-HOLD { background: #fef3c7; color: #92400e; }
  .v-SELL { background: #fee2e2; color: #991b1b; }
  .v-UNKNOWN { background: #f3f4f6; color: #374151; }
  .armed { border-left: 4px solid #f59e0b; }
  .filled-LONG { border-left: 4px solid #16a34a; background: #f0fdf4; }
  .filled-SHORT { border-left: 4px solid #dc2626; background: #fef2f2; }
  table { border-collapse: collapse; font-size: 0.85rem; }
  th, td { border: 1px solid #e5e7eb; padding: 0.4rem 0.6rem; vertical-align: top; }
  th { background: #f9fafb; }
  details > summary { cursor: pointer; padding: 0.25rem 0; }
  input[type="text"], input[type="number"], textarea {
    border: 1px solid #d1d5db; border-radius: 4px; padding: 4px 6px;
    font-size: 0.875rem; width: 100%;
  }
  textarea { min-height: 60px; }
  .next-step {
    background: #1e293b; color: #f8fafc; padding: 10px 14px;
    border-radius: 6px; font-size: 0.85rem; line-height: 1.5;
  }
</style>
</head>
<body class="bg-slate-50 text-slate-900">

<header class="bg-slate-900 text-white p-6 shadow">
  <div class="max-w-7xl mx-auto flex flex-wrap items-center gap-4">
    <div>
      <h1 class="text-3xl">交易 Dashboard</h1>
      <p class="text-slate-300 text-sm mt-1">產生於 __GENERATED__ · 互動狀態自動存 localStorage</p>
    </div>
    <div class="ml-auto flex gap-2">
      <button onclick="armAll()" class="bg-amber-500 hover:bg-amber-600 text-white px-3 py-2 rounded text-sm font-semibold">⚡ Arm 全部</button>
      <button onclick="disarmAll()" class="bg-slate-600 hover:bg-slate-700 text-white px-3 py-2 rounded text-sm">🔒 Disarm 全部</button>
      <button onclick="exportLog()" class="bg-blue-600 hover:bg-blue-700 text-white px-3 py-2 rounded text-sm">📥 匯出 trade log (CSV)</button>
      <button onclick="exportHeld()" class="bg-emerald-600 hover:bg-emerald-700 text-white px-3 py-2 rounded text-sm">📤 匯出持倉 → held_tickers</button>
      <button onclick="resetAll()" class="bg-rose-600 hover:bg-rose-700 text-white px-3 py-2 rounded text-sm">🗑 清空狀態</button>
    </div>
  </div>
</header>

<nav class="bg-slate-100 border-b border-slate-300 p-3 sticky top-0 z-10 text-sm">
  <div class="max-w-7xl mx-auto flex flex-wrap gap-3">
    <a class="text-blue-700 hover:underline font-semibold" href="#top20">🏆 Top 20</a>
    __NAV_LINKS__
    <a class="ml-auto text-blue-700 hover:underline" href="./SECTOR_OVERVIEWS.html" target="_blank">📖 族群 overview</a>
    <a class="text-blue-700 hover:underline" href="./HOWTO_READ.html" target="_blank">📘 閱讀指南</a>
    <a class="text-blue-700 hover:underline" href="./_catalysts.json" target="_blank">📅 catalyst JSON</a>
    <a class="text-rose-700 hover:underline font-semibold" href="./alerts.html" target="_blank">🚨 L0 Alerts</a>
  </div>
</nav>

<main class="max-w-7xl mx-auto p-6 space-y-6">

  __ALERTS__

  <section id="top20" class="bg-white rounded-lg shadow p-4">
    <div class="flex items-baseline justify-between mb-3 border-b pb-2">
      <div>
        <h2 class="text-xl font-bold">🏆 Top 20 綜合排行</h2>
        <p class="text-xs text-slate-500">跨族群 score = verdict × conviction × (1 + R:R T2 / 5) × phase modifier · Phase-1-only 標 × 0.35</p>
      </div>
      <div class="text-xs text-slate-500">指標說明: Score 為相對分數 · Conv 信心% · R:R T2 目標報酬風險比 · Phase1=只跑 Phase 1</div>
    </div>
    <div class="overflow-x-auto">
      <table class="w-full text-xs">
        <thead>
          <tr class="bg-slate-100">
            <th class="text-center">#</th>
            <th>Ticker</th>
            <th>Sector</th>
            <th>Verdict</th>
            <th class="text-right">Score</th>
            <th class="text-right">Conv%</th>
            <th class="text-right">R:R T2</th>
            <th>Phase</th>
            <th>Entry</th>
            <th>Stop</th>
            <th>T1</th>
            <th>T2</th>
            <th>Size</th>
            <th>Scan</th>
            <th>Report</th>
          </tr>
        </thead>
        <tbody id="top20-tbody">
__TOP20_ROWS__
        </tbody>
      </table>
    </div>
  </section>

  <div id="filter-bar" class="bg-white rounded-lg shadow p-4 flex flex-wrap items-center gap-4 text-sm">
    <span class="font-semibold">過濾:</span>
    <label><input type="checkbox" id="f-buy"  checked> BUY</label>
    <label><input type="checkbox" id="f-hold" checked> HOLD</label>
    <label><input type="checkbox" id="f-sell" checked> SELL</label>
    <label><input type="checkbox" id="f-armed"> 僅顯示 armed</label>
    <label><input type="checkbox" id="f-filled"> 僅顯示已下單</label>
    <input type="text" id="f-search" placeholder="搜尋 ticker (e.g. TLN)" class="ml-auto" style="max-width:200px;">
  </div>

  <div id="dashboard-root"></div>

</main>

<script>
const DATA = __DATA__;
const STORAGE_KEY = "trading_dashboard_v2";  // v2: adds active_card snapshot (strategy A)

function loadState() {
  try {
    return JSON.parse(localStorage.getItem(STORAGE_KEY) || "{}");
  } catch { return {}; }
}
function saveState(s) {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(s));
}

const STATE = loadState();

function tState(ticker) {
  if (!STATE[ticker]) STATE[ticker] = { armed: false, fills: [], notes: "", active_card: null };
  // Backward compat: older state may lack active_card
  if (STATE[ticker].active_card === undefined) STATE[ticker].active_card = null;
  return STATE[ticker];
}

// Snapshot a trade card into state. Used when user fills first time.
// Locks the stop/target you actually entered with so later scans don't drift.
function snapshotCard(ticker, scanCard) {
  return {
    locked_at:  new Date().toISOString(),
    scan_date:  scanCard.scan_date,
    verdict:    scanCard.verdict,
    entry:      scanCard.entry || "",
    stop:       scanCard.stop || "",
    t1:         scanCard.t1 || "",
    t2:         scanCard.t2 || "",
    size:       scanCard.size || "",
    horizon:    scanCard.horizon || "",
  };
}

// Find the historical scan card whose date is closest to (and <=) fill_date.
// Falls back to the earliest history entry if fill_date is before any scan,
// or to scanCard (latest) if no history.
function pickHistoricalCard(scanCard, fillDate) {
  const hist = scanCard.history || {};
  const dates = Object.keys(hist).sort();
  if (dates.length === 0) return scanCard;
  // Pick latest date <= fillDate
  let chosen = null;
  for (const d of dates) {
    if (d <= fillDate) chosen = d;
    else break;
  }
  if (chosen === null) chosen = dates[0];  // fill_date earlier than any scan, use earliest
  const c = hist[chosen];
  // Merge minimal latest fields into the historical card (ticker, report_url)
  return Object.assign({}, c, {ticker: scanCard.ticker, report_url: scanCard.report_url});
}

// Extract a single representative price from a string like "$310-315" or "$301.45".
function parsePrice(s) {
  if (s == null) return null;
  const m = String(s).match(/\$?\s*([\d,]+(?:\.\d+)?)/);
  return m ? Number(m[1].replace(/,/g, "")) : null;
}

// Return drift label "(+5.2% 🔻)" / "(-3.1% 🟢)" / "" if cannot compute.
// For stop/T1/T2 — positive drift downward is bearish for longs, upward is bullish.
function drift(activeVal, latestVal, field) {
  const a = parsePrice(activeVal);
  const b = parsePrice(latestVal);
  if (a == null || b == null || a === 0) return "";
  const pct = ((b - a) / a) * 100;
  if (Math.abs(pct) < 1) return `<span class="text-slate-400">(${pct >= 0 ? "+" : ""}${pct.toFixed(1)}%)</span>`;
  let arrow = "";
  if (field === "stop") {
    // For long: lower stop = bad (further loss); higher stop = better (tighter)
    arrow = pct < 0 ? " 🔻" : " 🟢";
  } else if (field === "t1" || field === "t2") {
    // Lower target = bad; higher = good
    arrow = pct < 0 ? " 🔻" : " 🟢";
  } else {
    arrow = pct < 0 ? " 🔻" : " 🟢";
  }
  const cls = Math.abs(pct) > 5 ? "text-rose-600 font-semibold" : "text-amber-600";
  return `<span class="${cls}">(${pct >= 0 ? "+" : ""}${pct.toFixed(1)}%${arrow})</span>`;
}

function armAll() {
  for (const s of Object.values(DATA.sectors)) {
    for (const t of s.tickers) {
      tState(t.ticker).armed = true;
    }
  }
  saveState(STATE); render();
}
function disarmAll() {
  for (const k of Object.keys(STATE)) STATE[k].armed = false;
  saveState(STATE); render();
}
function resetAll() {
  if (!confirm("確定清空所有 armed / 下單紀錄?")) return;
  localStorage.removeItem(STORAGE_KEY);
  for (const k of Object.keys(STATE)) delete STATE[k];
  render();
}

function toggleArmed(ticker) {
  tState(ticker).armed = !tState(ticker).armed;
  saveState(STATE); render();
}
function setNotes(ticker, txt) {
  tState(ticker).notes = txt;
  saveState(STATE);
}
function addFill(ticker, fill, scanCard) {
  const s = tState(ticker);
  // Snapshot active_card on first non-CLOSE fill (LONG / SHORT). Strategy A:
  // first entry locks the trade card; later scans don't auto-overwrite.
  // IMPORTANT: pick the historical scan card whose date matches the fill date,
  // not the latest scan — back-dated fills should reflect the conditions that
  // were known when the user actually traded.
  if (s.active_card === null && fill.side !== "CLOSE" && scanCard) {
    const histCard = pickHistoricalCard(scanCard, fill.time || new Date().toISOString().slice(0,10));
    s.active_card = snapshotCard(ticker, histCard);
  }
  s.fills.push(fill);
  saveState(STATE); render();
}

// Re-snapshot active_card from historical scan, based on a user-supplied date.
// Useful when fill was back-dated and the original snapshot grabbed the wrong scan.
function resnapFromDate(ticker, scanCard) {
  const s = tState(ticker);
  const firstFill = (s.fills && s.fills[0]) ? s.fills[0].time : new Date().toISOString().slice(0,10);
  const histDates = Object.keys(scanCard.history || {}).sort();
  if (histDates.length === 0) {
    alert("此 ticker 無歷史 scan, 無法重抓.");
    return;
  }
  const prompt_msg = `輸入進場日 (YYYY-MM-DD), 會抓 ≤ 此日的最近 scan.\n可用 scan: ${histDates.join(", ")}`;
  const dateInput = prompt(prompt_msg, firstFill);
  if (!dateInput) return;
  const dateClean = dateInput.trim();
  const histCard = pickHistoricalCard(scanCard, dateClean);
  if (!confirm(`重抓 ${histCard.scan_date} 的 scan: stop ${histCard.stop || "-"} / T1 ${histCard.t1 || "-"} / T2 ${histCard.t2 || "-"}?`)) return;
  s.active_card = snapshotCard(ticker, histCard);
  saveState(STATE); render();
}

// Manual edit of active_card fields. Useful if user filled at a date with no
// scan history, or if scan snapshot doesn't match what they actually traded.
function editActiveCard(ticker) {
  const s = tState(ticker);
  if (!s.active_card) {
    alert("尚未鎖定 active_card. 先 fill 一筆才能編輯.");
    return;
  }
  const a = s.active_card;
  const fields = ["entry", "stop", "t1", "t2", "size", "horizon", "scan_date"];
  const labels = {entry:"Entry", stop:"Stop", t1:"T1", t2:"T2", size:"Size", horizon:"Horizon", scan_date:"鎖定 scan 日期"};
  const updated = {};
  for (const f of fields) {
    const v = prompt(labels[f] + " (原: " + (a[f] || "-") + ")", a[f] || "");
    if (v === null) return;  // user cancelled
    updated[f] = v.trim();
  }
  Object.assign(s.active_card, updated);
  s.active_card.edited_at = new Date().toISOString();
  saveState(STATE); render();
}
function removeFill(ticker, i) {
  const s = tState(ticker);
  s.fills.splice(i, 1);
  // If no fills remain, also clear the active_card snapshot
  if (s.fills.length === 0) s.active_card = null;
  saveState(STATE); render();
}

// Manual override: replace the locked active_card with the latest scan card.
// Use after deliberate re-evaluation when the new scan thesis is convincing.
function updateActiveCard(ticker, scanCard) {
  if (!confirm("確定用最新 scan 覆蓋已鎖定的進場條件? (建議: 只在明確 thesis 改變時)")) return;
  tState(ticker).active_card = snapshotCard(ticker, scanCard);
  saveState(STATE); render();
}

// Exit position: clear all fills + active_card (preserves notes).
function exitPosition(ticker) {
  if (!confirm("確定登記出場? 會清除 active_card + fills (不可復原, 但 notes 保留)")) return;
  const s = tState(ticker);
  s.fills = [];
  s.active_card = null;
  saveState(STATE); render();
}

// Compute weighted-average entry price for net position.
// Strategy: process fills in time order. LONG adds to position with weighted avg cost.
// CLOSE reduces position at FIFO. SHORT treated as separate inverse position.
// Returns {netSize, avgPrice, side, totalCost} for net position.
function computePosition(fills) {
  let longLots = [];   // [{size, price}] FIFO queue
  let shortLots = [];
  const sorted = [...(fills||[])].sort((a, b) => (a.time||"").localeCompare(b.time||""));
  for (const f of sorted) {
    const sz = Number(f.size || 0);
    const px = Number(f.price || 0);
    if (sz <= 0 || px <= 0) continue;
    if (f.side === "LONG") {
      longLots.push({size: sz, price: px});
    } else if (f.side === "SHORT") {
      shortLots.push({size: sz, price: px});
    } else if (f.side === "CLOSE") {
      // Close reduces existing position (long first, then short)
      let remaining = sz;
      while (remaining > 0 && longLots.length > 0) {
        const lot = longLots[0];
        const take = Math.min(remaining, lot.size);
        lot.size -= take;
        remaining -= take;
        if (lot.size <= 1e-9) longLots.shift();
      }
      while (remaining > 0 && shortLots.length > 0) {
        const lot = shortLots[0];
        const take = Math.min(remaining, lot.size);
        lot.size -= take;
        remaining -= take;
        if (lot.size <= 1e-9) shortLots.shift();
      }
    }
  }
  const netLong = longLots.reduce((a, b) => a + b.size, 0);
  const netShort = shortLots.reduce((a, b) => a + b.size, 0);
  const longCost = longLots.reduce((a, b) => a + b.size * b.price, 0);
  const shortCost = shortLots.reduce((a, b) => a + b.size * b.price, 0);
  if (netLong > 0 && netShort === 0) {
    return {netSize: netLong, avgPrice: longCost / netLong, side: "LONG", totalCost: longCost};
  }
  if (netShort > 0 && netLong === 0) {
    return {netSize: netShort, avgPrice: shortCost / netShort, side: "SHORT", totalCost: shortCost};
  }
  if (netLong > 0 && netShort > 0) {
    // Hedged or both sides — show net direction
    const netSize = netLong - netShort;
    return {netSize: netSize, avgPrice: netSize > 0 ? longCost / netLong : shortCost / netShort,
            side: netSize > 0 ? "LONG" : "SHORT", totalCost: longCost + shortCost};
  }
  return {netSize: 0, avgPrice: 0, side: "FLAT", totalCost: 0};
}

// Compute unrealized P/L % based on avg cost vs current scan price (entry midpoint).
function unrealizedPL(pos, t) {
  if (pos.netSize === 0 || pos.avgPrice === 0) return null;
  // Try to get current price from active_card entry or latest scan entry midpoint
  const priceStr = (t.entry || "").match(/\$?\s*([\d,]+(?:\.\d+)?)/);
  if (!priceStr) return null;
  const curPrice = Number(priceStr[1].replace(/,/g, ""));
  if (curPrice <= 0) return null;
  const pct = pos.side === "LONG"
    ? (curPrice - pos.avgPrice) / pos.avgPrice * 100
    : (pos.avgPrice - curPrice) / pos.avgPrice * 100;
  return {pct, curPrice};
}

function nextStep(t) {
  const s = tState(t.ticker);
  const fills = s.fills || [];
  const pos = computePosition(fills);
  const net = pos.side === "LONG" ? pos.netSize : (pos.side === "SHORT" ? -pos.netSize : 0);
  // Strategy A: when filled, monitor against ACTIVE (locked) card not latest.
  const active = s.active_card;

  if (!s.armed && fills.length === 0) {
    return "⚪ 未 armed, 無持倉. " + (t.verdict === "BUY" ? "考慮 Arm 等觸發 / 進場." :
                                       t.verdict === "HOLD" ? "Arm 後觀察條件式 trigger." :
                                       t.verdict === "SELL" ? "Arm 後等空單條件." : "等下次掃描");
  }
  if (s.armed && fills.length === 0) {
    if (t.verdict === "BUY") return "🟢 已 Arm. 觸發條件達到時, 按 trade card 多單建倉 (尺寸 " + (t.size||"見計劃") + ").";
    if (t.verdict === "HOLD") return "🟡 已 Arm. 等任一 trigger 觸發 (見下方). 觸發後選邊執行.";
    if (t.verdict === "SELL") return "🔴 已 Arm. 觸發後做空 (尺寸 " + (t.size||"見計劃") + ").";
    return "已 Arm.";
  }
  if (net > 0) {
    const useStop = (active && active.stop) || t.stop || "見計劃";
    const useT1 = (active && active.t1) || t.t1 || "";
    const useT2 = (active && active.t2) || t.t2 || "";
    const tag = active ? "鎖定條件 (active_card)" : "最新 scan";
    return "🟢 已建多倉 " + net.toFixed(2) + " 股 @ 均價 $" + pos.avgPrice.toFixed(2) + ". 監控 [" + tag + "] stop " + useStop + " / T1 " + useT1 + " / T2 " + useT2 + ". 達 T1 → 半止盈; 觸 stop → 全出.";
  }
  if (net < 0) {
    const useStop = (active && active.stop) || t.stop || "見計劃";
    return "🔴 已建空倉 " + Math.abs(net).toFixed(2) + " 股 @ 均價 $" + pos.avgPrice.toFixed(2) + ". 監控空單 stop " + useStop + ". 注意空頭 squeeze.";
  }
  return "⚖️ 進出已 net flat. 紀錄複盤 vs trade card.";
}

function tickerCard(sector, t) {
  const s = tState(t.ticker);
  const filled = (s.fills && s.fills.length > 0);
  const pos = computePosition(s.fills || []);
  const net = pos.side === "LONG" ? pos.netSize : (pos.side === "SHORT" ? -pos.netSize : 0);
  const pnl = unrealizedPL(pos, t);
  const armedClass = s.armed ? "armed " : "";
  const fillClass = net > 0 ? "filled-LONG " : net < 0 ? "filled-SHORT " : "";
  const verdictClass = "v-" + (t.verdict || "UNKNOWN");

  // Avg holding price banner (shown when net position exists)
  let avgBanner = "";
  if (pos.netSize > 0) {
    const pnlHtml = pnl ? (
      pnl.pct >= 0
        ? `<span class="text-green-700 font-semibold">+${pnl.pct.toFixed(2)}% (latest ~$${pnl.curPrice.toFixed(2)})</span>`
        : `<span class="text-rose-700 font-semibold">${pnl.pct.toFixed(2)}% (latest ~$${pnl.curPrice.toFixed(2)})</span>`
    ) : '<span class="text-slate-400">no scan price</span>';
    const sideColor = pos.side === "LONG" ? "bg-green-50 border-green-300 text-green-900" : "bg-rose-50 border-rose-300 text-rose-900";
    avgBanner = `
      <div class="mb-3 ${sideColor} border rounded p-2 text-xs flex flex-wrap items-center gap-3">
        <span class="font-bold">💼 持倉 ${pos.side}</span>
        <span><b>淨部位:</b> ${pos.netSize.toFixed(2)} 股</span>
        <span><b>平均成本:</b> $${pos.avgPrice.toFixed(2)}</span>
        <span><b>總成本:</b> $${pos.totalCost.toFixed(2)}</span>
        <span class="ml-auto"><b>未實現 P/L:</b> ${pnlHtml}</span>
      </div>`;
  }

  const catalysts = (DATA.catalysts[t.ticker] || []).slice(0, 5);
  const catHtml = catalysts.length === 0 ? '<em class="text-slate-500">無即將事件</em>' :
    '<ul class="text-xs">' + catalysts.map(c =>
      `<li><b>${c.date}</b> [<span class="text-blue-700">${c.category}</span>] ${escapeHtml(c.desc)}</li>`
    ).join('') + '</ul>';

  const fillsHtml = (s.fills||[]).map((f, i) => `
    <tr>
      <td>${f.time||""}</td>
      <td>${f.side||""}</td>
      <td>${f.size||""}</td>
      <td>${f.price||""}</td>
      <td><button onclick="removeFill('${t.ticker}', ${i})" class="text-rose-600 hover:underline">×</button></td>
    </tr>
  `).join('');

  const trigsHtml = (t.triggers||[]).map(x => `<li class="text-xs">${escapeHtml(x)}</li>`).join('');

  return `
  <div class="bg-white rounded-lg shadow-sm border border-slate-200 p-4 ${armedClass}${fillClass}">
    <div class="flex items-start gap-3 mb-2">
      <div class="${verdictClass} px-3 py-1 rounded text-lg font-bold min-w-[80px] text-center">${t.verdict}</div>
      <div class="flex-1">
        <div class="flex items-baseline gap-2">
          <span class="text-xl font-bold">${t.ticker}</span>
          <span class="text-xs text-slate-500">${t.modify||""} · scan ${t.scan_date}</span>
          <a href="${t.report_url}" target="_blank" class="ml-auto text-xs text-blue-700 hover:underline">完整報告 →</a>
        </div>
      </div>
      <label class="flex items-center gap-2 text-sm whitespace-nowrap">
        <input type="checkbox" ${s.armed ? "checked" : ""} onchange="toggleArmed('${t.ticker}')" class="w-5 h-5">
        <span>Armed</span>
      </label>
    </div>

    ${avgBanner}

    ${
      s.active_card ? `
      <div class="mb-3 bg-amber-50 border border-amber-300 rounded p-3">
        <div class="flex items-center gap-2 mb-2">
          <span class="bg-amber-200 text-amber-900 px-2 py-0.5 text-xs font-bold rounded">🔒 ACTIVE (進場已鎖定)</span>
          <span class="text-xs text-slate-600">鎖定於 scan ${escapeHtml(s.active_card.scan_date)}</span>
          <div class="ml-auto flex gap-1 flex-wrap">
            <button onclick='resnapFromDate("${t.ticker}", ${JSON.stringify(t).replace(/'/g,"&apos;")})'
                    class="bg-violet-600 hover:bg-violet-700 text-white text-xs px-2 py-1 rounded">🔄 從進場日重抓</button>
            <button onclick='editActiveCard("${t.ticker}")'
                    class="bg-amber-600 hover:bg-amber-700 text-white text-xs px-2 py-1 rounded">✏️ 編輯</button>
            <button onclick='updateActiveCard("${t.ticker}", ${JSON.stringify(t).replace(/'/g,"&apos;")})'
                    class="bg-blue-600 hover:bg-blue-700 text-white text-xs px-2 py-1 rounded">用最新覆蓋</button>
            <button onclick='exitPosition("${t.ticker}")'
                    class="bg-rose-600 hover:bg-rose-700 text-white text-xs px-2 py-1 rounded">出場</button>
          </div>
        </div>
        <div class="grid grid-cols-2 lg:grid-cols-4 gap-2 text-xs">
          <div class="bg-white border border-amber-200 p-2 rounded">
            <b>Entry</b><br>${escapeHtml(s.active_card.entry||"-")}
            <div class="text-[10px] text-slate-500 mt-1">latest: ${escapeHtml(t.entry||"-")} ${drift(s.active_card.entry, t.entry, "entry")}</div>
          </div>
          <div class="bg-white border border-amber-200 p-2 rounded">
            <b>Stop</b><br>${escapeHtml(s.active_card.stop||"-")}
            <div class="text-[10px] text-slate-500 mt-1">latest: ${escapeHtml(t.stop||"-")} ${drift(s.active_card.stop, t.stop, "stop")}</div>
          </div>
          <div class="bg-white border border-amber-200 p-2 rounded">
            <b>T1</b><br>${escapeHtml(s.active_card.t1||"-")}
            <div class="text-[10px] text-slate-500 mt-1">latest: ${escapeHtml(t.t1||"-")} ${drift(s.active_card.t1, t.t1, "t1")}</div>
          </div>
          <div class="bg-white border border-amber-200 p-2 rounded">
            <b>T2</b><br>${escapeHtml(s.active_card.t2||"-")}
            <div class="text-[10px] text-slate-500 mt-1">latest: ${escapeHtml(t.t2||"-")} ${drift(s.active_card.t2, t.t2, "t2")}</div>
          </div>
        </div>
        <div class="text-[11px] text-slate-600 mt-2">Size: ${escapeHtml(s.active_card.size||"-")} · Horizon: ${escapeHtml(s.active_card.horizon||"-")} · 進場時 verdict: <b>${escapeHtml(s.active_card.verdict||"-")}</b></div>
      </div>
      <div class="mb-3 bg-sky-50 border border-sky-300 rounded p-3">
        <div class="flex items-center gap-2 mb-2 flex-wrap">
          <span class="bg-sky-200 text-sky-900 px-2 py-0.5 text-xs font-bold rounded">📊 最新 scan 分析 (比對追蹤)</span>
          <span class="text-xs text-slate-600">scan ${escapeHtml(t.scan_date)} · verdict <b class="${verdictClass} px-1 rounded">${escapeHtml(t.verdict||"-")}</b>${t.modify?` · ${escapeHtml(t.modify)}`:""}</span>
          <a href="${t.report_url}" target="_blank" class="ml-auto text-xs text-blue-700 hover:underline">完整報告 →</a>
        </div>
        <div class="grid grid-cols-2 lg:grid-cols-4 gap-2 text-xs">
          <div class="bg-white border border-sky-200 p-2 rounded">
            <b>Entry</b><br>${escapeHtml(t.entry||"-")}
            <div class="text-[10px] text-slate-500 mt-1">vs 鎖定 ${escapeHtml(s.active_card.entry||"-")} ${drift(s.active_card.entry, t.entry, "entry")}</div>
          </div>
          <div class="bg-white border border-sky-200 p-2 rounded">
            <b>Stop</b><br>${escapeHtml(t.stop||"-")}
            <div class="text-[10px] text-slate-500 mt-1">vs 鎖定 ${escapeHtml(s.active_card.stop||"-")} ${drift(s.active_card.stop, t.stop, "stop")}</div>
          </div>
          <div class="bg-white border border-sky-200 p-2 rounded">
            <b>T1</b><br>${escapeHtml(t.t1||"-")}
            <div class="text-[10px] text-slate-500 mt-1">vs 鎖定 ${escapeHtml(s.active_card.t1||"-")} ${drift(s.active_card.t1, t.t1, "t1")}</div>
          </div>
          <div class="bg-white border border-sky-200 p-2 rounded">
            <b>T2</b><br>${escapeHtml(t.t2||"-")}
            <div class="text-[10px] text-slate-500 mt-1">vs 鎖定 ${escapeHtml(s.active_card.t2||"-")} ${drift(s.active_card.t2, t.t2, "t2")}</div>
          </div>
        </div>
        <div class="text-[11px] text-slate-600 mt-2">Size: ${escapeHtml(t.size||"-")} · Horizon: ${escapeHtml(t.horizon||"-")}${(t.verdict && s.active_card.verdict && t.verdict !== s.active_card.verdict)?` · <b class="text-rose-700">⚠️ verdict 已由 ${escapeHtml(s.active_card.verdict)} 變為 ${escapeHtml(t.verdict)}</b>`:""}</div>
      </div>
      ` : `
      <div class="grid grid-cols-2 lg:grid-cols-4 gap-2 text-xs mb-3">
        <div class="bg-slate-50 p-2 rounded"><b>Entry</b><br>${escapeHtml(t.entry||"-")}</div>
        <div class="bg-slate-50 p-2 rounded"><b>Stop</b><br>${escapeHtml(t.stop||"-")}</div>
        <div class="bg-slate-50 p-2 rounded"><b>T1</b><br>${escapeHtml(t.t1||"-")}</div>
        <div class="bg-slate-50 p-2 rounded"><b>T2</b><br>${escapeHtml(t.t2||"-")}</div>
      </div>
      `
    }

    <div class="grid grid-cols-1 lg:grid-cols-2 gap-3 mb-3">
      <div>
        <details><summary class="font-semibold text-sm">🔔 Triggers (${(t.triggers||[]).length})</summary>
          <ul class="list-disc ml-5 mt-1">${trigsHtml}</ul>
          ${t.monitoring ? '<p class="text-xs mt-2"><b>監控:</b> '+escapeHtml(t.monitoring)+'</p>' : ''}
        </details>
      </div>
      <div>
        <details><summary class="font-semibold text-sm">📅 即將事件 (${catalysts.length})</summary>
          ${catHtml}
        </details>
      </div>
    </div>

    <div class="next-step mb-3">${nextStep(t)}</div>

    <details>
      <summary class="font-semibold text-sm">📝 下單紀錄 (${(s.fills||[]).length}) / 備註</summary>
      <table class="w-full mt-2 mb-2">
        <thead><tr><th>時間</th><th>方向</th><th>數量</th><th>價位</th><th></th></tr></thead>
        <tbody>
          ${fillsHtml || '<tr><td colspan="5" class="text-center text-slate-400">尚無紀錄</td></tr>'}
        </tbody>
      </table>
      <form onsubmit="event.preventDefault(); submitFill('${t.ticker}', this);" class="grid grid-cols-5 gap-2 mb-3">
        <input name="time"  type="date" value="${new Date().toISOString().slice(0,10)}" required>
        <select name="side"  required class="border border-slate-300 rounded px-2 py-1 text-sm">
          <option value="LONG">LONG</option>
          <option value="SHORT">SHORT</option>
          <option value="CLOSE">CLOSE</option>
        </select>
        <input name="size"  type="number" step="any" placeholder="數量" required>
        <input name="price" type="number" step="any" placeholder="價位" required>
        <button class="bg-blue-600 hover:bg-blue-700 text-white rounded text-sm">加入</button>
      </form>
      <textarea placeholder="備註 (本地端儲存)..." oninput="setNotes('${t.ticker}', this.value)">${escapeHtml(s.notes||"")}</textarea>
    </details>
  </div>
  `;
}

function escapeHtml(s) {
  return String(s == null ? "" : s)
    .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;').replace(/'/g, '&#39;');
}

function submitFill(ticker, form) {
  const fd = new FormData(form);
  // Find the matching latest scan card for this ticker so addFill can snapshot it.
  let scanCard = null;
  for (const s of Object.values(DATA.sectors)) {
    const found = s.tickers.find(x => x.ticker === ticker);
    if (found) { scanCard = found; break; }
  }
  addFill(ticker, {
    time:  fd.get("time"),
    side:  fd.get("side"),
    size:  fd.get("size"),
    price: fd.get("price"),
  }, scanCard);
  form.reset();
  form.time.value = new Date().toISOString().slice(0,10);
}

function applyFilters(t) {
  const showBuy  = document.getElementById("f-buy").checked;
  const showHold = document.getElementById("f-hold").checked;
  const showSell = document.getElementById("f-sell").checked;
  const onlyArmed  = document.getElementById("f-armed").checked;
  const onlyFilled = document.getElementById("f-filled").checked;
  const search = (document.getElementById("f-search").value || "").toUpperCase();

  if (!showBuy  && t.verdict === "BUY") return false;
  if (!showHold && t.verdict === "HOLD") return false;
  if (!showSell && t.verdict === "SELL") return false;

  const s = tState(t.ticker);
  if (onlyArmed && !s.armed) return false;
  if (onlyFilled && (s.fills||[]).length === 0) return false;
  if (search && !t.ticker.includes(search)) return false;
  return true;
}

function render() {
  const root = document.getElementById("dashboard-root");
  let html = "";
  for (const sec of Object.keys(DATA.sectors)) {
    const s = DATA.sectors[sec];
    const visibleTickers = s.tickers.filter(applyFilters);
    if (visibleTickers.length === 0) continue;
    html += `
      <section id="sec-${sec}" class="bg-white rounded-lg shadow p-4">
        <div class="flex items-baseline justify-between mb-3 border-b pb-2">
          <div>
            <h2 class="text-xl font-bold">${escapeHtml(s.label)}</h2>
            <p class="text-xs text-slate-500">scan ${s.scan_date} · ${visibleTickers.length} / ${s.tickers.length} ticker 顯示</p>
          </div>
          <a href="${s.report_url}" target="_blank" class="text-sm text-blue-700 hover:underline">族群完整報告 →</a>
        </div>
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-3">
          ${visibleTickers.map(t => tickerCard(sec, t)).join('')}
        </div>
      </section>
    `;
  }
  root.innerHTML = html || '<div class="bg-white p-6 rounded shadow text-center text-slate-500">無符合條件的 ticker</div>';
}

function exportLog() {
  const rows = [["ticker","sector","verdict","time","side","size","price","notes"]];
  for (const sec of Object.keys(DATA.sectors)) {
    for (const t of DATA.sectors[sec].tickers) {
      const s = STATE[t.ticker] || {};
      for (const f of (s.fills||[])) {
        rows.push([t.ticker, sec, t.verdict, f.time, f.side, f.size, f.price, (s.notes||"").replace(/[\n,]/g," ")]);
      }
    }
  }
  if (rows.length === 1) { alert("尚無交易紀錄"); return; }
  const csv = rows.map(r => r.map(x => `"${String(x||"").replace(/"/g,'""')}"`).join(",")).join("\n");
  const blob = new Blob([csv], {type:"text/csv;charset=utf-8;"});
  const link = document.createElement("a");
  link.href = URL.createObjectURL(blob);
  link.download = "trade_log_" + new Date().toISOString().slice(0,10) + ".csv";
  link.click();
}

// Export the set of held tickers (net position > 0 OR active_card locked) so
// the backend can sync held_tickers.txt to what you actually hold. Browser
// JS can't write the repo file directly (file:// sandbox), so it downloads
// held_export.txt; save it to /Users/yht/Study/scans/ (canonical read point).
// sync_held.py — run manually or auto at daily_scan.sh startup — merges it.
function exportHeld() {
  const held = new Set();
  for (const sec of Object.keys(DATA.sectors)) {
    for (const t of DATA.sectors[sec].tickers) {
      const s = STATE[t.ticker] || {};
      const pos = computePosition(s.fills || []);
      if (pos.netSize > 0 || s.active_card) held.add(t.ticker);
    }
  }
  const list = Array.from(held).sort();
  if (list.length === 0) { alert("尚無持倉 (需有 fill 淨部位或鎖定卡)"); return; }
  const body = "# exported from dashboard " + new Date().toISOString().slice(0,10) +
               "\n# tickers with net position > 0 or locked active_card\n" +
               list.join("\n") + "\n";
  const blob = new Blob([body], {type:"text/plain;charset=utf-8;"});
  const link = document.createElement("a");
  link.href = URL.createObjectURL(blob);
  link.download = "held_export.txt";
  link.click();
  alert("已匯出 " + list.length + " 檔 (held_export.txt → ~/Downloads):\n" +
        list.join(", ") +
        "\n\n下次 daily_scan.sh 開頭會自動把它從 ~/Downloads 搬進 scans/ 並併進 held_tickers.txt。\n" +
        "要立即併: mv ~/Downloads/held_export.txt /Users/yht/Study/scans/ && python3 ~/.claude/tools/trading/sync_held.py");
}

document.getElementById("f-buy").onchange = render;
document.getElementById("f-hold").onchange = render;
document.getElementById("f-sell").onchange = render;
document.getElementById("f-armed").onchange = render;
document.getElementById("f-filled").onchange = render;
document.getElementById("f-search").oninput = render;

render();
</script>

</body>
</html>
"""


def _esc(s) -> str:
    return (str(s) if s is not None else "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def render_top20_rows(top20: list) -> str:
    rows = []
    for i, t in enumerate(top20, 1):
        v = t["verdict"]
        vcls = {"BUY": "bg-green-100 text-green-800", "HOLD": "bg-amber-100 text-amber-800",
                "SELL": "bg-rose-100 text-rose-800"}.get(v, "bg-slate-100 text-slate-700")
        phase_cell = ('<span class="bg-slate-200 text-slate-700 px-1.5 py-0.5 rounded text-[10px]">P1 only</span>'
                      if t["phase1_only"] else
                      '<span class="bg-blue-100 text-blue-800 px-1.5 py-0.5 rounded text-[10px]">Full</span>')
        rr_color = "text-green-700 font-semibold" if t["rr_t2"] >= 2.0 else "text-slate-700"
        conv_color = "text-green-700 font-semibold" if t["conviction"] >= 60 else "text-slate-700"
        rank_color = ("bg-yellow-100 text-yellow-900 font-bold" if i == 1 else
                      "bg-slate-100 text-slate-700 font-semibold" if i <= 3 else
                      "text-slate-600")
        rows.append(f"""
          <tr class="hover:bg-slate-50">
            <td class="text-center {rank_color}">{i}</td>
            <td class="font-mono font-bold"><a href="#sec-{t['sector']}" class="text-blue-700 hover:underline">{_esc(t['ticker'])}</a></td>
            <td class="text-xs">{_esc(t['sector_label'])}</td>
            <td><span class="{vcls} px-2 py-0.5 rounded font-semibold">{_esc(v)}</span></td>
            <td class="text-right font-mono font-semibold">{t['score']:.1f}</td>
            <td class="text-right font-mono {conv_color}">{t['conviction']}%</td>
            <td class="text-right font-mono {rr_color}">{t['rr_t2']:.2f}x</td>
            <td>{phase_cell}</td>
            <td class="text-xs">{_esc(t['entry'])[:30]}</td>
            <td class="text-xs">{_esc(t['stop'])[:20]}</td>
            <td class="text-xs">{_esc(t['t1'])[:20]}</td>
            <td class="text-xs">{_esc(t['t2'])[:20]}</td>
            <td class="text-xs">{_esc(t['size'])[:25]}</td>
            <td class="text-xs text-slate-500">{_esc(t['scan_date'])}</td>
            <td><a href="{_esc(t['report_url'])}" target="_blank" class="text-blue-700 hover:underline text-xs">↗</a></td>
          </tr>""")
    return "\n".join(rows)


def render_alert_banner() -> str:
    """Top-of-dashboard L0 monitor banner from alerts.json (zero-LLM price
    tracker output). Shows the most urgent actionable alerts (urgency<=2:
    stop breached / near stop / T1-T2 hit / in entry zone). Empty if no file."""
    f = SCANS / "alerts.json"
    if not f.exists():
        return ""
    try:
        data = json.loads(f.read_text(encoding="utf-8"))
    except Exception:
        return ""
    hot = [a for a in data.get("alerts", []) if a.get("urgency", 9) <= 2]
    if not hot:
        return ""
    chips = []
    color = {0: "bg-rose-200 text-rose-900", 1: "bg-amber-200 text-amber-900",
             2: "bg-sky-200 text-sky-900"}
    for a in hot[:24]:
        c = color.get(a["urgency"], "bg-slate-200 text-slate-800")
        px = f"${a['price']:.2f}" if a.get("price") else "—"
        flag = (a.get("flags") or ["—"])[0]
        chips.append(
            f'<span class="{c} px-2 py-1 rounded text-xs whitespace-nowrap" '
            f'title="{_esc(", ".join(a.get("flags", [])))}">'
            f'<b>{_esc(a["ticker"])}</b> {px} · {_esc(flag)}</span>'
        )
    gen = _esc(data.get("generated_at", ""))
    return (
        '<section class="bg-slate-900 text-white rounded-lg shadow p-4">'
        '<div class="flex items-baseline justify-between mb-2 border-b border-slate-700 pb-2">'
        f'<h2 class="text-lg font-bold">🚨 L0 Monitor — {len(hot)} 個觸發</h2>'
        f'<span class="text-xs text-slate-400">價格追蹤 (零 LLM) · {gen} UTC · '
        '<a class="text-blue-400 hover:underline" href="./alerts.html" target="_blank">完整 →</a></span>'
        '</div><div class="flex flex-wrap gap-2">' + "".join(chips) + "</div></section>"
    )


def main():
    payload = collect_payload()

    nav_links = []
    for sec, sd in payload["sectors"].items():
        nav_links.append(f'<a class="text-blue-700 hover:underline" href="#sec-{sec}">{sd["label"]}</a>')

    top20_html = render_top20_rows(payload.get("top20", []))

    html = (HTML_TEMPLATE
            .replace("__GENERATED__", payload["generated_at"])
            .replace("__NAV_LINKS__", "\n".join(nav_links))
            .replace("__ALERTS__", render_alert_banner())
            .replace("__TOP20_ROWS__", top20_html)
            .replace("__DATA__", json.dumps(payload, ensure_ascii=False)))

    OUT.write_text(html, encoding="utf-8")
    print(f"dashboard → {OUT}")
    print(f"  sectors covered: {len(payload['sectors'])}")
    total = sum(len(s['tickers']) for s in payload['sectors'].values())
    print(f"  tickers: {total}")
    print(f"  catalysts: {sum(len(v) for v in payload['catalysts'].values())} upcoming")
    print(f"  Top 20 ranked from {total} tickers (top score {payload['top20'][0]['score'] if payload['top20'] else 0})")


if __name__ == "__main__":
    main()
