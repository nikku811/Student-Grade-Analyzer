"""
====================================================
  Student Grade Analyzer
  Author  : Student Grade Analyzer Tool
  Version : 1.0.0
  Python  : 3.x
====================================================
Automatically reads student data from a CSV file,
computes totals, percentages, assigns grades,
determines Pass/Fail status, and identifies top scorer.
"""




# stdlib
import csv
import os
from pathlib import Path

# ─────────────────────────────────────────────
#  CONFIGURATION
# ─────────────────────────────────────────────
BASE_DIR     = Path(__file__).parent
DATA_FILE    = BASE_DIR / "data" / "students.csv"
PASS_CUTOFF  = 40          # Minimum percentage to PASS
MAX_PER_SUB  = 100         # Maximum marks per subject


# Grade boundaries (percentage)
GRADE_SCALE = [
    (90, "A+"),
    (80, "A"),
    (70, "B"),
    (60, "C"),
    (50, "D"),
     (40, "E"),
    (0,  "F"),
]