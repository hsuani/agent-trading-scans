#!/usr/bin/env python3
"""
Merge the dashboard's exported holdings into held_tickers.txt.

Bridges the gap between two DIFFERENT records:
  - dashboard localStorage fills  = what you ACTUALLY hold (entry price, size)
  - held_tickers.txt              = the "force full Phase 2-4" list the scan reads

The dashboard is static HTML on file://, so its JS cannot write the repo file
directly. The "📤 匯出持倉" button downloads held_export.txt; save it to
/Users/yht/Study/scans/ (canonical read point). This script merges any
newly-held tickers into held_tickers.txt (append-only, deduped). Existing
manual entries / comments are preserved — nothing is removed.

daily_scan.sh runs this automatically at startup (if the export exists), so a
fresh export is picked up before the scan reads held_tickers.txt.

Usage:
  python3 ~/.claude/tools/trading/sync_held.py
  python3 ~/.claude/tools/trading/sync_held.py --export /path/to/held_export.txt
  python3 ~/.claude/tools/trading/sync_held.py --dry-run
"""
import argparse
import re
import sys
from datetime import date
from pathlib import Path

TOOL_DIR = Path(__file__).resolve().parent
HELD_FILE = TOOL_DIR / "held_tickers.txt"
DEFAULT_EXPORT = Path("/Users/yht/Study/scans/held_export.txt")

TICKER_RE = re.compile(r"^[A-Z0-9.]+$")


def read_tickers(path: Path) -> list:
    """Return ordered list of ticker symbols from a file (skip comments/blanks)."""
    out = []
    if not path.exists():
        return out
    for line in path.read_text(encoding="utf-8").splitlines():
        s = line.split("#", 1)[0].strip()
        if s and TICKER_RE.match(s):
            out.append(s)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--export", type=Path, default=DEFAULT_EXPORT,
                    help=f"dashboard export file (default {DEFAULT_EXPORT})")
    ap.add_argument("--dry-run", action="store_true", help="show plan, don't write")
    args = ap.parse_args()

    if not args.export.exists():
        print(f"export file not found: {args.export}", file=sys.stderr)
        print("Tip: click '📤 匯出持倉 → held_tickers' on the dashboard first.",
              file=sys.stderr)
        sys.exit(1)

    exported = read_tickers(args.export)
    existing = read_tickers(HELD_FILE)
    existing_set = set(existing)

    additions = [t for t in exported if t not in existing_set]
    # dedupe additions while preserving order
    seen = set()
    additions = [t for t in additions if not (t in seen or seen.add(t))]

    # Manual-only entries: in held_tickers.txt but NOT in the dashboard export.
    # These are watchlist / 掛單 items you keep forcing-full without holding yet.
    exported_set = set(exported)
    manual_only = [t for t in existing if t not in exported_set]

    print(f"dashboard export : {len(exported)} held  ({', '.join(exported) or '—'})")
    print(f"held_tickers.txt : {len(existing)} entries")
    print(f"new to add       : {len(additions)} ({', '.join(additions) or '—'})")
    if manual_only:
        print(f"manual-only kept : {len(manual_only)} ({', '.join(manual_only)}) "
              f"— in list but not held on dashboard (watchlist/掛單), preserved")

    if not additions:
        print("nothing to add. held_tickers.txt already covers all held tickers.")
        return

    if args.dry_run:
        print("[dry-run] would append the above additions.")
        return

    block = (f"\n# synced from dashboard {date.today().isoformat()}\n"
             + "\n".join(additions) + "\n")
    with HELD_FILE.open("a", encoding="utf-8") as f:
        f.write(block)
    print(f"appended {len(additions)} ticker(s) to {HELD_FILE}")
    print("next scan that covers them will force full Phase 2-4.")


if __name__ == "__main__":
    main()
