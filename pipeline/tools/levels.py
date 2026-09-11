#!/usr/bin/env python3
"""Shared level parsing for the dashboard, the L0 monitor and validate.py.

One rule: a trade level is an ABSOLUTE PRICE or it is nothing. "2.6", "1.25x",
"+20%", "entry + 2R", "10x P/E", "4.30%" (a yield) are never prices. A bare
number is accepted only when it looks like a price (>= 10, or thousands comma,
or two decimals) AND, when a reference is available, sits within a sane band
of it. Without a reliable absolute value the level is UNPRICED and no price
trigger may fire from it.

  parse_price(s, ref=None)             -> float | None
  parse_zone(s, ref=None)              -> (lo, hi) | (None, None)
  sane(v, ref, lo=0.3, hi=5.0)         -> bool
  validate_long(lo, hi, stop, t1, t2)  -> reason | None
  plan_status(card, quote=None)        -> {"plan": PRICED|UNPRICED|LEVELS_INVALID|LEVEL_SCALE_SUSPECT, levels...}
  quote_status(quote_at, now=None)     -> LIVE | STALE | UNAVAILABLE
  trade_ready(plan, quote, scan_date, phase1_only, today=None) -> ACTIONABLE|RESEARCH_ONLY|NEEDS_REPRICE|DATA_STALE
"""
import re
from datetime import date, datetime, timezone

# A card that says any of these declined to quote a real level; numbers in the
# same field belong to a condition or a placeholder, never to a price.
DECLINED_PHRASES = ("PRICE_DATA_UNAVAILABLE", "無即時", "暫不給", "無法計算", "不設固定價位", "不設價位",
                    "不填列", "不給具體", "DERIVED", "非即時報價", "非實時報價", "文件參考", "estimated anchor",
                    "待盤口", "待即時", "待觸發")

# Units that make a number NOT a price — stripped before any price search.
NON_PRICE_PATTERNS = (
    r"\d+(?:\.\d+)?\s*[xX×]\b",                      # multiples 1.25x / 10x
    r"\d+(?:\.\d+)?\s*[xX×](?!\d)",
    r"\d+(?:\.\d+)?\s*R\b",                           # 2R
    r"\d+(?:\.\d+)?\s*倍",
    r"[+\-−]?\d+(?:\.\d+)?\s*%",                      # +20% / -3% / 4.30%
    r"\d+(?:\.\d+)?\s*(?:pp|bps|BPS|bp)\b",
    r"20\d{2}\s*[-/]\s*\d{1,2}(?:\s*[-/]\s*\d{1,2})?", # dates
    r"\d{4}\s*年", r"\d{1,2}\s*月", r"\d{1,2}\s*日",
    r"\d{4}\s*Q[1-4]", r"Q[1-4]\s*\d{2,4}", r"\b[QH][1-4]\b", r"FY\s?\d{2,4}\w*",
    r"\d+(?:\.\d+)?\s*[億萬兆]",
    r"\d+(?:\.\d+)?(?:\s*[–—~-]\s*\d+(?:\.\d+)?)?\s*個?\s*(?:交易日|營業日|工作天|小時|天|週|周|日|月|季)",
    r"\d+\s*(?:yr|y)\b",                              # 10yr UST
    r"(?:NT\$|US\$|\$)?\s*\d+(?:\.\d+)?\s*[BMK](?![A-Za-z$])", # $2.0B revenue, 500M, 10K — magnitudes, not prices
    r"\b\d{1,2}-\d{1,2}\b",                          # 09-21 short dates
    r"(?:S&P|Nasdaq|NASDAQ|Russell|Dow|SOX|PHLX|MSCI|台股|加權)\s*\d+",  # index names
)

MONEY_RE = re.compile(
    r"(?:NT\$|US\$|TWD|USD|NTD|\$)\s*(\d+(?:,\d{3})*(?:\.\d+)?)"
    r"(?:\s*[–—~-]\s*(?:NT\$|US\$|TWD|USD|NTD|\$)?\s*(\d+(?:,\d{3})*(?:\.\d+)?))?")
BARE_RE = re.compile(r"(?<![\w.])(\d+(?:,\d{3})*(?:\.\d+)?)(?![\w.])")


def _clean(s):
    out = s
    for pat in NON_PRICE_PATTERNS:
        out = re.sub(pat, " ", out)
    return out


def _bare_ok(tok):
    v = float(tok.replace(",", ""))
    return v > 0 and ("," in tok or v >= 10 or re.fullmatch(r"\d+\.\d{2}", tok) is not None)


def price_tokens(s):
    """[(value, currency_marked)] in text order, non-price units removed."""
    if not s or any(ph in s for ph in DECLINED_PHRASES):
        return []
    cleaned = _clean(s)
    marked = [float(g.replace(",", "")) for pair in MONEY_RE.findall(cleaned) for g in pair if g]
    if marked:
        return [(v, True) for v in marked if v > 0]
    return [(float(t.replace(",", "")), False) for t in BARE_RE.findall(cleaned) if _bare_ok(t)]


def sane(v, ref, lo=0.3, hi=5.0):
    return v is not None and v > 0 and (ref is None or ref <= 0 or lo <= v / ref <= hi)


def parse_price(s, ref=None, lo=0.3, hi=5.0):
    for v, _marked in price_tokens(s):
        if sane(v, ref, lo, hi):
            return v
    return None


def parse_zone(s, ref=None, lo=0.3, hi=5.0, max_width=1.5):
    """Entry zone. Two numbers only form a zone when they are within max_width of
    each other; a bare "21 … 100" is two stray numbers, not a range."""
    toks = [(v, m) for v, m in price_tokens(s) if sane(v, ref, lo, hi)][:2]
    if not toks:
        return (None, None)
    vals = [v for v, _ in toks]
    if len(vals) == 2 and max(vals) / min(vals) > max_width:
        if all(m for _, m in toks):
            return (vals[0], vals[0])   # marked but far apart: keep the first as a point level
        return (None, None)
    return (min(vals), max(vals))


def validate_long(lo, hi, stop, t1, t2, scale_ratio=5.0):
    present = [x for x in (lo, hi, stop, t1, t2) if x]
    if len(present) >= 2 and max(present) / min(present) > scale_ratio:
        return f"scale x{max(present) / min(present):.0f}"
    if stop and lo and stop >= lo:
        return "stop >= entry"
    if stop and t1 and stop >= t1:
        return "stop >= T1"
    if t1 and hi and t1 <= hi:
        return "T1 <= entry"
    if t1 and t2 and t2 < t1:
        return "T2 < T1"
    return None


def plan_status(card, quote=None, scale_band=(0.5, 2.0)):
    """Absolute levels of a card + one plan status. Targets and stop are sanity
    checked against the entry midpoint (else the quote); the entry midpoint
    against the quote for LEVEL_SCALE_SUSPECT (e.g. a NT$340 card on a NT$1,330
    stock)."""
    entry_txt = card.get("entry", "") or ""
    if any(ph in entry_txt for ph in DECLINED_PHRASES):
        # The card itself said it had no real price when written (PRICE_DATA_UNAVAILABLE /
        # DERIVED / 文件參考): every level on it is derived, so none may fire a trigger.
        return {"entry_lo": None, "entry_hi": None, "entry_mid": None, "stop": None, "t1": None, "t2": None,
                "plan": "UNPRICED", "reason": "card declined pricing"}
    lo, hi = parse_zone(entry_txt)
    mid = (lo + hi) / 2 if lo else None
    ref = mid or (quote if quote and quote > 0 else None)
    stop = parse_price(card.get("stop", ""), ref)
    t1 = parse_price(card.get("t1", ""), ref)
    t2 = parse_price(card.get("t2", ""), ref)
    out = {"entry_lo": lo, "entry_hi": hi, "entry_mid": mid, "stop": stop, "t1": t1, "t2": t2, "reason": None}
    if mid and quote and quote > 0 and not sane(mid, quote, *scale_band):
        out["plan"], out["reason"] = "LEVEL_SCALE_SUSPECT", f"entry {mid:g} vs quote {quote:g}"
        return out
    if not any((lo, stop, t1, t2)):
        out["plan"], out["reason"] = "UNPRICED", "no absolute level"
        return out
    bad = validate_long(lo, hi, stop, t1, t2)
    if bad:
        out["plan"], out["reason"] = "LEVELS_INVALID", bad
        return out
    out["plan"] = "PRICED" if (lo and stop) else "UNPRICED"
    if out["plan"] == "UNPRICED":
        out["reason"] = "missing " + "/".join(n for n, v in (("entry", lo), ("stop", stop)) if not v)
    return out


def quote_status(quote_at, now=None, stale_hours=24):
    if not quote_at:
        return "UNAVAILABLE"
    try:
        t = datetime.fromisoformat(str(quote_at).replace("Z", "+00:00"))
    except ValueError:
        return "UNAVAILABLE"
    now = now or datetime.now(timezone.utc)
    if t.tzinfo is None:
        t = t.replace(tzinfo=timezone.utc)
    return "LIVE" if (now - t).total_seconds() <= stale_hours * 3600 else "STALE"


def trade_ready(plan, quote, scan_date, phase1_only=False, today=None, stale_days=10):
    today = today or date.today()
    if phase1_only:
        return "RESEARCH_ONLY"
    if plan in ("UNPRICED", "LEVELS_INVALID", "LEVEL_SCALE_SUSPECT"):
        return "NEEDS_REPRICE"
    if quote == "UNAVAILABLE":
        return "RESEARCH_ONLY"
    if quote == "STALE" or (scan_date and (today - date.fromisoformat(scan_date)).days > stale_days):
        return "DATA_STALE"
    return "ACTIONABLE"
