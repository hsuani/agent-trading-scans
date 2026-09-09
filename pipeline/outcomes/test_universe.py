#!/usr/bin/env python3
"""1A regression guard: the taxonomy is defined once (universe.py) and every
copy that must exist for non-Python consumers (SKILL.md dict, daily_scan.sh
schedule) is byte-for-byte consistent with it. Also asserts 1A changed routing
only: same ticker set as v2.0-baseline, no overlaps, dynamic sources dedup.
Run: python3 pipeline/outcomes/test_universe.py"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "pipeline" / "tools"))
import universe as u  # noqa: E402

# 1. same static universe as v2.0-baseline, one primary group per ticker
v1 = {t for ts in u.V1_GROUPS.values() for t in ts}
assert u.static_universe() == v1, u.static_universe() ^ v1
flat = [t for ts in u.PEER_GROUPS.values() for t in ts] + list(u.UNASSIGNED)
assert len(flat) == len(set(flat)), "ticker in two groups"
assert u.primary_group("8021.TW") is None and u.theme_tags("8021.TW") == ["pcb_consumables"]
assert u.primary_group("3443.TW") == "tw_asic" and u.v1_group("3443.TW") == "tw_probe"

# 2. dynamic-source dedup uses the same resolver (the SNDK bug)
assert u.in_static_universe("SNDK") and u.in_static_universe("nvda") and not u.in_static_universe("GOOGL")
assert set(u.NO_PEER_RANKING) == {"serenity", "tw_unassigned"}

# 3. every key scheduled exactly once; every schedule key resolvable
sched = [k for d in u.SCHEDULE.values() for k in d]
assert sorted(sched) == sorted(u.all_groups()), set(sched) ^ set(u.all_groups())
for k in sched:
    u.resolve(k)
for k in u.LEGACY_DIRS:
    assert k in u.all_groups()

# 4. SKILL.md's in-context dict == universe.py
skill = (ROOT / ".claude" / "skills" / "trading-scan" / "SKILL.md").read_text(encoding="utf-8")
block = re.search(r"```\nSECTORS = \{(.*?)\n\}\n```", skill, re.S).group(1)
ns = {}
exec("SECTORS = {" + block + "\n}", ns)  # noqa: S102 — our own file
want = dict(u.PEER_GROUPS); want[u.UNASSIGNED_KEY] = list(u.UNASSIGNED)
assert ns["SECTORS"] == want, {k for k in set(ns["SECTORS"]) | set(want) if ns["SECTORS"].get(k) != want.get(k)}

# 5. daily_scan.sh DAY_SECTORS == universe.SCHEDULE
sh = (ROOT / "pipeline" / "tools" / "daily_scan.sh").read_text(encoding="utf-8")
days = re.findall(r'^\s+"([^"]*)"\s+#', sh[sh.index("DAY_SECTORS=("):sh.index("\n)\n", sh.index("DAY_SECTORS=("))], re.M)
assert [d.split() for d in days[1:]] == [u.SCHEDULE[i] for i in range(1, 8)], days

# 6. Phase 5 agents exist; watchlist-digest forbids ranking
agents = ROOT / ".claude" / "agents" / "trading"
assert (agents / "sector-comparator.md").exists() and (agents / "watchlist-digest.md").exists()
assert "watchlist-digest" in skill and "tw_unassigned" in skill
print("ok")
