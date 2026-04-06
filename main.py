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


# ─────────────────────────────────────────────
#  HELPERS
# ─────────────────────────────────────────────
def load_students(filepath: Path) -> tuple[list[str], list[dict]]:
    """Load student records from a CSV file.

    Returns
    -------
    subjects : list[str]
        Names of the subject columns found in the CSV header.
    students : list[dict]
        Raw student records as dictionaries.
    """
    if not filepath.exists():
        raise FileNotFoundError(
            f"Dataset not found: {filepath}\n"
            "Please ensure 'data/students.csv' exists."
        )

    with open(filepath, newline="", encoding="utf-8") as fh:
        reader    = csv.DictReader(fh)
        fieldnames = reader.fieldnames or []
        subjects  = [f for f in fieldnames if f != "Name"]
        students  = [row for row in reader]

    if not students:
        raise ValueError("The CSV file is empty – no student records found.")

    return subjects, students
