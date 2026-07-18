#!/usr/bin/env python3
"""
Manage pending.txt — the list of sectors/tickers that failed to complete and
need a FRESH run at the latest date. Used by the cloud backfill routine to
catch up missed work without ever re-running a stale past date.

Entry forms (one per line in pending.txt at repo root):
  SECTOR          whole sector
  SECTOR:TICKER   single ticker within a sector   (informational; runners
                  generally re-run the whole SECTOR)

Commands:
  pending.py list                       # print current entries (no comments)
  pending.py add SECTOR [SECTOR...]     # append (delete-dup)
  pending.py remove SECTOR [SECTOR...]  # drop matching entries
  pending.py prune --date YYYY-MM-DD    # drop entries whose sector now has
                                        # daily/<date>/<sector>/sector_report.md
  pending.py sectors                    # space-joined sector names (for shell)

Root resolves from TRADING_SCANS_ROOT, else repo root (parents[2]).
"""
import argparse
import os
import re
import sys
from pathlib import Path

ROOT = Path(os.environ.get("TRADING_SCANS_ROOT") or Path(__file__).resolve().parents[2])
DAILY = ROOT / "daily"
PENDING = ROOT / "pending.txt"

# Full sector universe (every sector that should get a complete scan once per
# cycle). Used by `detect` to find sectors whose most recent complete run is
# stale — catching whole days that died (e.g. session limit) without ever
# updating pending.txt. Keep in sync with SKILL.md SECTORS / daily_scan.sh.
ALL_SECTORS = [
    "semi", "power", "cooling", "reit", "oem", "security", "robotics",
    "materials", "quantum", "photonics", "hedge",
    "abf", "tw_cooling", "tw_server", "tw_power", "tw_pkg",
    "tw_photonics", "tw_probe", "tw_memory", "memory", "serenity",
]

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

HEADER = """\
# Pending scans — sectors/tickers that failed to complete and need a FRESH run
# at the LATEST date (never re-run a stale past date; prices have moved on).
# Managed by pipeline/tools/pending.py. One entry per line: SECTOR or SECTOR:TICKER.
"""


def read_entries():
    """Ordered list of (raw_entry) excluding comments/blanks, de-duped."""
    if not PENDING.exists():
        return []
    out, seen = [], set()
    for line in PENDING.read_text(encoding="utf-8").splitlines():
        s = line.split("#", 1)[0].strip()
        if s and s not in seen:
            seen.add(s)
            out.append(s)
    return out


def write_entries(entries):
    seen, ordered = set(), []
    for e in entries:
        if e and e not in seen:
            seen.add(e)
            ordered.append(e)
    PENDING.write_text(HEADER + "".join(e + "\n" for e in ordered), encoding="utf-8")


def sector_of(entry):
    return entry.split(":", 1)[0]


def latest_complete(sector):
    """Most recent date (str) with a non-empty daily/<date>/<sector>/sector_report.md,
    or None if the sector has never completed."""
    best = None
    if not DAILY.is_dir():
        return None
    for d in DAILY.iterdir():
        if not (d.is_dir() and DATE_RE.match(d.name)):
            continue
        rpt = d / sector / "sector_report.md"
        if rpt.exists() and rpt.stat().st_size > 0:
            if best is None or d.name > best:
                best = d.name
    return best


def detect_stale(stale_days, today):
    """Sectors whose latest complete run is older than stale_days (or never run).
    Returns list of sector names. `today` is YYYY-MM-DD str."""
    from datetime import date as _date
    t = _date.fromisoformat(today)
    stale = []
    for sec in ALL_SECTORS:
        last = latest_complete(sec)
        if last is None:
            stale.append((sec, "never"))
            continue
        age = (t - _date.fromisoformat(last)).days
        if age > stale_days:
            stale.append((sec, f"{last} ({age}d)"))
    return stale


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("list")
    sub.add_parser("sectors")
    a = sub.add_parser("add"); a.add_argument("items", nargs="+")
    r = sub.add_parser("remove"); r.add_argument("items", nargs="+")
    p = sub.add_parser("prune"); p.add_argument("--date", required=True)
    dt = sub.add_parser("detect")
    dt.add_argument("--today", required=True)
    dt.add_argument("--stale-days", type=int, default=7)
    dt.add_argument("--add", action="store_true", help="add detected stale sectors to pending")
    dt.add_argument("--prune-fresh", action="store_true",
                    help="also drop whole-sector entries already scanned within stale-days "
                         "(keeps pending == the real gap set; SECTOR:TICKER entries untouched)")
    args = ap.parse_args()

    entries = read_entries()

    if args.cmd == "list":
        print("\n".join(entries))
    elif args.cmd == "sectors":
        # unique sector names, space-joined — handy for `for s in $(... sectors)`
        seen, secs = set(), []
        for e in entries:
            s = sector_of(e)
            if s not in seen:
                seen.add(s); secs.append(s)
        print(" ".join(secs))
    elif args.cmd == "add":
        write_entries(entries + args.items)
        print(f"added: {' '.join(args.items)}")
    elif args.cmd == "remove":
        drop = set(args.items)
        kept = [e for e in entries if e not in drop and sector_of(e) not in drop]
        write_entries(kept)
        print(f"removed: {' '.join(args.items)}")
    elif args.cmd == "prune":
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", args.date):
            print("bad --date (YYYY-MM-DD)", file=sys.stderr); sys.exit(2)
        kept, pruned = [], []
        for e in entries:
            sec = sector_of(e)
            done = (DAILY / args.date / sec / "sector_report.md")
            if done.exists() and done.stat().st_size > 0:
                pruned.append(e)
            else:
                kept.append(e)
        write_entries(kept)
        print(f"pruned {len(pruned)} done @ {args.date}: {' '.join(pruned) or '—'}")
        print(f"remaining: {' '.join(kept) or '—'}")
    elif args.cmd == "detect":
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", args.today):
            print("bad --today (YYYY-MM-DD)", file=sys.stderr); sys.exit(2)
        from datetime import date as _date
        stale = detect_stale(args.stale_days, args.today)
        stale_secs = {s for s, _ in stale}
        if stale:
            print(f"stale (>{args.stale_days}d) sectors:")
            for sec, why in stale:
                print(f"  {sec:14} last={why}")
        else:
            print(f"no stale sectors (all ran within {args.stale_days}d)")

        new_entries = list(entries)
        if args.prune_fresh:
            t = _date.fromisoformat(args.today)
            kept, dropped = [], []
            for e in new_entries:
                if ":" in e:                       # manual SECTOR:TICKER — leave alone
                    kept.append(e); continue
                if e in stale_secs:                # still stale — keep
                    kept.append(e); continue
                last = latest_complete(e)
                if last is not None and (t - _date.fromisoformat(last)).days <= args.stale_days:
                    dropped.append(e)              # recently scanned → drop
                else:
                    kept.append(e)
            new_entries = kept
            print(f"prune-fresh dropped {len(dropped)}: {' '.join(dropped) or '—'}")
        if args.add:
            new_entries = new_entries + [s for s, _ in stale]
            print(f"added {len(stale_secs)} to pending: {' '.join(sorted(stale_secs)) or '—'}")
        if args.prune_fresh or args.add:
            write_entries(new_entries)
            final = []
            for e in new_entries:            # dedup preserving order (matches write_entries)
                if e not in final:
                    final.append(e)
            print(f"pending now: {' '.join(final) or '—'}")


if __name__ == "__main__":
    main()
