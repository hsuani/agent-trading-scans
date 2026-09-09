#!/usr/bin/env python3
"""Canonical scan universe — the ONE place peer groups, dynamic sources and the
weekly schedule are defined. Everything else (SKILL.md, daily_scan.sh,
build_dashboard, render_html, extract_catalysts, pending, serenity) reads from
here or is checked against it by test_universe.py.

Three separate ideas, kept separate on purpose:
  PEER_GROUPS      who a company's comparables are   -> Phase 5 = sector-comparator
  DYNAMIC_SOURCES  why a ticker surfaced today       -> Phase 5 = watchlist-digest
  theme tags       exposure, no peer claim           -> UNASSIGNED tickers carry only these

Historical daily/<date>/<v1 key>/ artifacts are never rewritten; V1_GROUPS is
the frozen v2.0-baseline taxonomy for outcome cohorts, LEGACY_DIRS lets the
dashboard read old reports until each new group has its own.

    python3 pipeline/tools/universe.py tw_asic      # tickers, comma-separated
    python3 pipeline/tools/universe.py --json       # every group
    python3 pipeline/tools/universe.py --group SNDK # primary group of a ticker
"""
import json
import os
import sys
from collections import OrderedDict
from pathlib import Path

ROOT = Path(os.environ.get("TRADING_SCANS_ROOT") or Path(__file__).resolve().parents[2])

PEER_GROUPS = OrderedDict([
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
    ("memory",     ["000660.KS", "005930.KS", "SNDK", "WDC"]),
    ("hedge",      ["GLD", "TLT", "UUP", "SH"]),
    # Taiwan supply chain — one primary peer group per ticker, no overlaps
    ("tw_ic_substrate",  ["3037.TW", "8046.TW", "3189.TW"]),                 # ABF 載板三雄
    ("tw_ai_pcb",        ["2368.TW", "4958.TW"]),                            # AI PCB (金像電 / 臻鼎)
    ("tw_cooling",       ["3324.TWO", "8996.TW", "3017.TW", "3653.TW", "6805.TW"]),
    ("tw_server",        ["6669.TW", "3231.TW", "2356.TW", "2376.TW"]),
    ("tw_power",         ["2308.TW", "1513.TW", "1519.TW", "2301.TW"]),
    ("tw_asic",          ["3661.TW", "3443.TW"]),                            # ASIC 設計服務 (世芯 / 創意)
    ("tw_photonics",     ["3081.TWO", "2455.TW", "5455.TWO", "3163.TWO", "3008.TW", "4908.TWO",
                          "3363.TWO", "4979.TWO", "4977.TW", "3711.TW", "6830.TW", "3587.TWO", "3289.TWO"]),
    ("tw_probe",         ["6510.TWO", "6223.TWO", "6515.TW", "6217.TWO"]),  # 探針卡 only
    ("tw_test_services", ["6257.TW", "2449.TW"]),                            # IC 測試服務 (矽格 / 京元電)
    ("tw_memory",        ["2408.TW", "2344.TW", "8299.TWO", "3260.TW"]),
])

# Scanned (Phase 1-4) but with NO primary peer group — theme tags only. They are
# routed through the `tw_unassigned` bucket for scheduling; Phase 5 = digest.
# TODO(1A): give them a peer group once there are >= 3 real comparables each.
UNASSIGNED = OrderedDict([
    ("8021.TW", ["pcb_consumables"]),        # 尖點 — PCB 鑽針耗材
    ("6438.TW", ["automation_equipment"]),   # 迅得 — 自動化設備
])
UNASSIGNED_KEY = "tw_unassigned"

DYNAMIC_SOURCES = ("serenity",)                     # universe resolved at run time
NO_PEER_RANKING = DYNAMIC_SOURCES + (UNASSIGNED_KEY,)  # Phase 5 = watchlist-digest, never a ranking

LABELS = {
    "semi": "A. 半導體核心", "power": "B. 電力 / 電網", "cooling": "C. 散熱 / 網通 / 光通訊",
    "reit": "D. 資料中心 REIT", "oem": "E. AI 伺服器 OEM (US+TW)", "security": "F. AI 安全",
    "robotics": "G. 機器人 / 自駕", "materials": "H. 原料 / 稀土", "hedge": "I. 避險",
    "tw_ic_substrate": "J. ABF 載板 (TW)", "tw_ai_pcb": "J2. AI PCB (TW)",
    "tw_cooling": "K. 散熱模組 (TW)", "tw_server": "L. AI server ODM (TW)",
    "tw_power": "N. 電源 / 電網 (TW)", "tw_asic": "O. ASIC 設計服務 (TW)",
    "quantum": "P. 量子運算 (incl. Quantinuum=HON)", "photonics": "Q. 矽光子 (US pure-play)",
    "memory": "Q2. 記憶體 HBM/DRAM/NAND", "tw_photonics": "R. 矽光子供應鏈 上中下游+檢測 (TW)",
    "tw_probe": "S. 探針卡 (TW)", "tw_test_services": "S2. IC 測試服務 (TW)",
    "tw_memory": "T2. 記憶體 DRAM/NAND (TW)",
    "tw_unassigned": "U. 未分組 — theme tags only (TW)",
    "serenity": "T. Serenity 追蹤標的 (@aleabitoreddit picks)",
}

# Weekly schedule (isoweekday 1..7). Same tickers per day as v1; only the keys changed.
SCHEDULE = {
    1: ["semi", "tw_asic", "tw_unassigned", "serenity"],
    2: ["power", "tw_power", "quantum"],
    3: ["cooling", "tw_cooling", "memory"],
    4: ["oem", "tw_server", "tw_ic_substrate", "tw_ai_pcb", "tw_memory"],
    5: ["security", "materials", "robotics"],
    6: ["hedge", "reit", "tw_probe", "tw_test_services"],
    7: ["photonics", "tw_photonics"],
}

# Frozen v2.0-baseline taxonomy (what daily/<date>/<key>/ dirs were written under
# before 1A). Outcome cohorts keep this as `sector_v1`; never edit.
V1_GROUPS = OrderedDict(list(PEER_GROUPS.items())[:12] + [
    ("abf",        ["3037.TW", "8046.TW", "3189.TW", "4958.TW", "2368.TW"]),
    ("tw_cooling", PEER_GROUPS["tw_cooling"]), ("tw_server", PEER_GROUPS["tw_server"]),
    ("tw_power",   PEER_GROUPS["tw_power"]),
    ("tw_pkg",     ["3661.TW", "8021.TW", "6438.TW"]),
    ("tw_photonics", PEER_GROUPS["tw_photonics"]),
    ("tw_probe",   ["6510.TWO", "6223.TWO", "6515.TW", "6257.TW", "2449.TW", "3443.TW", "6217.TWO"]),
    ("tw_memory",  PEER_GROUPS["tw_memory"]),
])
# v2 key -> v1 dirs that hold its tickers' history (read-only fallback for the dashboard
# and for pending.py staleness, so a freshly split group is not "never scanned")
LEGACY_DIRS = {"tw_ic_substrate": ["abf"], "tw_ai_pcb": ["abf"], "tw_asic": ["tw_pkg"],
               "tw_unassigned": ["tw_pkg"], "tw_test_services": ["tw_probe"]}
# retired v1 key -> v2 keys (pending.txt entries written before 1A are translated on read)
RETIRED_KEYS = {"abf": ["tw_ic_substrate", "tw_ai_pcb"], "tw_pkg": ["tw_asic", "tw_unassigned"]}


def serenity_universe():
    f = ROOT / "serenity" / "universe.txt"
    if not f.is_file():
        return []
    return [s for s in (l.split("#", 1)[0].strip() for l in f.read_text(encoding="utf-8").splitlines()) if s]


def static_universe():
    """Every ticker a peer group or the unassigned bucket covers (not dynamic picks)."""
    return {t for ts in PEER_GROUPS.values() for t in ts} | set(UNASSIGNED)


def in_static_universe(ticker):
    return ticker.upper() in static_universe()


_PRIMARY = {t: g for g, ts in PEER_GROUPS.items() for t in ts}
_V1 = {t: g for g, ts in V1_GROUPS.items() for t in ts}


def primary_group(ticker):
    """Peer group key, or None (unassigned / dynamic pick / unknown)."""
    return _PRIMARY.get(ticker.upper())


def v1_group(ticker):
    return _V1.get(ticker.upper())


def theme_tags(ticker):
    return list(UNASSIGNED.get(ticker.upper(), []))


def resolve(key):
    """Tickers for a schedule key: peer group, unassigned bucket, or dynamic source."""
    if key in PEER_GROUPS:
        return list(PEER_GROUPS[key])
    if key == UNASSIGNED_KEY:
        return list(UNASSIGNED)
    if key == "serenity":
        return serenity_universe()
    raise KeyError(key)


def all_groups():
    """Every scan key -> tickers, in dashboard order (dynamic sources last)."""
    out = OrderedDict(PEER_GROUPS)
    out[UNASSIGNED_KEY] = list(UNASSIGNED)
    for d in DYNAMIC_SOURCES:
        out[d] = resolve(d)
    return out


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a or a[0] == "--json":
        print(json.dumps(all_groups(), ensure_ascii=False, indent=1))
    elif a[0] == "--group":
        print(primary_group(a[1]) or ("unassigned" if a[1].upper() in UNASSIGNED else "none"))
    else:
        print(",".join(resolve(a[0])))
