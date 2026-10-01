"""prices/ cache is the last link of quote()/history() and only while fresh."""
import json, os, sys, tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path

tmp = Path(tempfile.mkdtemp())
os.environ["TRADING_SCANS_ROOT"] = str(tmp)
sys.path.insert(0, str(Path(__file__).resolve().parent))
import pricefeed as pf  # noqa: E402

pf.CACHE_DIR.mkdir()
(pf.CACHE_DIR / "NVDA.csv").write_text("date,open,high,low,close,volume\n2026-09-30,180,185,179,184,1000\n2026-10-01,184,190,183,189,1200\n")
now = datetime.now(timezone.utc)
meta = {"NVDA": {"last_price": 189.0, "previous_close": 184.0, "currency": "USD"},
        "_refreshed_at": now.isoformat(timespec="seconds")}
(pf.CACHE_DIR / "quotes.json").write_text(json.dumps(meta))

q = pf._cache_quote("nvda")
assert q["last_price"] == 189.0 and q["source"] == "cache", q
assert pf._cache_quote("AMD") is None
rows = pf._cache_history("NVDA", 400)
assert len(rows) == 2 and rows[-1][4] == 189.0, rows

# every live feed down -> history() lands on the cache, cache=False does not
pf._yahoo_v8_history = pf._cnyes_history = pf._yfinance_history = pf._twse_history = lambda t, d: None
df = pf.history("NVDA", 30)
assert df.attrs["source"] == "cache" and len(df) == 2
try:
    pf.history("NVDA", 30, cache=False); raise AssertionError("cache=False must not read prices/")
except RuntimeError:
    pass

# stale cache (> CACHE_MAX_AGE_DAYS) is ignored -> probe would fail, not pass on old data
meta["_refreshed_at"] = (now - timedelta(days=pf.CACHE_MAX_AGE_DAYS + 1)).isoformat(timespec="seconds")
(pf.CACHE_DIR / "quotes.json").write_text(json.dumps(meta))
assert pf._cache_quote("NVDA") is None and pf._cache_history("NVDA", 30) is None
print("test_pricecache ok")
