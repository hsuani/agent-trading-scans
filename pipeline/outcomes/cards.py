"""Collect every final_decision.md as one flat record with the metadata every
Phase-0 tool needs (sector / held / era / stub / parsed levels / horizon).
Parsing itself is build_dashboard's — nothing is re-implemented here."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "pipeline" / "tools"))
import build_dashboard as bd  # noqa: E402

PROMPT_CUTOFF = "2026-08-28"     # first scan date after the 08-27 PM exit-frame commit
DEFAULT_HORIZON = 60             # trading days, when the card gives none
_UNIT = {"交易日": 1, "週": 5, "周": 5, "w": 5, "月": 21, "m": 21, "季": 63, "年": 252, "y": 252,
         "天": 0.7, "日": 0.7}
_HZ = re.compile(r"(\d+(?:\.\d+)?)(?:\s*[–—~-]\s*(\d+(?:\.\d+)?))?\s*個?\s*"
                 r"(交易日|週|周|個月|月|季|年|天|日|m|w|y)\b", re.I)


def parse_horizon(s, default=DEFAULT_HORIZON):
    """Upper bound of the card's horizon in trading days ('1–3 個月' -> 63)."""
    m = _HZ.search(s or "")
    if not m:
        return default
    n = float(m.group(2) or m.group(1))
    unit = m.group(3).lower().replace("個", "")
    return max(1, round(n * _UNIT[unit]))


def held_set():
    out = set()
    for line in (ROOT / "pipeline" / "tools" / "held_tickers.txt").read_text().splitlines():
        s = line.split("#", 1)[0].strip()
        if s:
            out.add(s)
    return out


import universe as _u  # noqa: E402  (pipeline/tools is already on sys.path)


def collect():
    held = held_set()
    for fd in sorted((ROOT / "daily").glob("*/*/final_decision.md")):
        text = fd.read_text(encoding="utf-8", errors="ignore")
        card = bd.parse_final_decision(text)
        rr = bd.parse_rr(text)
        em, st, t1, t2 = bd.derive_targets(card["entry"], card["stop"], rr)
        en = bd._first_nums(card["entry"], 2)
        # Prefer the analyst's own T1. derive_targets falls back to rr=1.5 when no
        # R:R parses, which puts T1 at 0.75R — a dashboard placeholder, not a thesis.
        stated = bd._first_nums(card["t1"], 1)
        if stated and em and stated[0] > em:
            t1, t1_source = stated[0], "stated"
        else:
            t1_source = "derived_rr" if rr != 1.5 else "derived_default"
        yield {
            "ticker": fd.parent.name, "scan_date": fd.parts[-3],
            # sector_v1 = frozen v2.0-baseline taxonomy (what the card was scanned under);
            # primary_group_v2 = the 1A peer group, derived by mapping — history is never rewritten.
            "sector_v1": _u.v1_group(fd.parent.name) or "other",
            "primary_group_v2": _u.primary_group(fd.parent.name)
                                or ("unassigned" if fd.parent.name in _u.UNASSIGNED else "other"),
            "verdict": card["verdict"], "modify": card["modify"],
            # currently_held_ticker = in TODAY's held_tickers.txt (single commit, 06-23) —
            # not a point-in-time holding. held_at_decision = the PM's own framing,
            # only written since the 08-27 prompt (held verdicts are Chinese words).
            "currently_held_ticker": fd.parent.name in held,
            "held_at_decision": (True if card["modify"] in ("加碼", "續抱", "減碼", "出場")
                                 else False if card["modify"] in ("APPROVE", "MODIFY", "REJECT")
                                 and fd.parts[-3] >= PROMPT_CUTOFF else None),
            "era": "post" if fd.parts[-3] >= PROMPT_CUTOFF else "pre",
            "stub": bd.is_phase1_only(text) or not (fd.parent / "trade_proposal.md").exists(),
            "entry_lo": min(en) if en else None, "entry_hi": max(en) if en else None,
            "entry_mid": em, "stop": st, "t1": t1, "t2": t2, "rr": rr, "t1_source": t1_source,
            "horizon_raw": card["horizon"], "horizon_days": parse_horizon(card["horizon"]),
            "conviction": bd.parse_conviction(text),
        }


def priced(cards):
    """Long-shaped cards with a full ladder: entry, stop below it, T1 above it."""
    return [c for c in cards if c["entry_mid"] and c["stop"] and c["t1"]
            and c["stop"] < c["entry_mid"] < c["t1"]]
