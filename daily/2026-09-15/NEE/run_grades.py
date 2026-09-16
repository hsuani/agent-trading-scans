#!/usr/bin/env python3
import sys
sys.path.insert(0, '/Users/yht/Study/scans/pipeline/evidence')
from source_grades import grade_file

if __name__ == "__main__":
    grade_file('/Users/yht/Study/scans/daily/2026-09-15/NEE/evidence_shadow.json')
    print("Evidence shadow grading complete.")
