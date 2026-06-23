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


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("list")
    sub.add_parser("sectors")
    a = sub.add_parser("add"); a.add_argument("items", nargs="+")
    r = sub.add_parser("remove"); r.add_argument("items", nargs="+")
    p = sub.add_parser("prune"); p.add_argument("--date", required=True)
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


if __name__ == "__main__":
    main()
