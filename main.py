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


def calculate_results(subjects: list[str], students: list[dict]) -> list[dict]:
    """Compute Total, Percentage, Grade, and Status for every student."""
    max_total = MAX_PER_SUB * len(subjects)
    results   = []

    for s in students:
        try:
            marks      = [int(s[sub]) for sub in subjects]
        except (ValueError, KeyError) as exc:
            raise ValueError(
                f"Invalid marks for student '{s.get('Name', '?')}': {exc}"
            )

        total      = sum(marks)
        percentage = (total / max_total) * 100
        grade      = assign_grade(percentage)
        status     = "PASS" if percentage >= PASS_CUTOFF else "FAIL"

        results.append({
            "Name"      : s["Name"],
            **{sub: marks[i] for i, sub in enumerate(subjects)},
            "Total"     : total,
            "Percentage": round(percentage, 2),
            "Grade"     : grade,
            "Status"    : status,
        })

    return results


def assign_grade(percentage: float) -> str:
    """Return letter grade based on percentage."""
    for threshold, letter in GRADE_SCALE:
        if percentage >= threshold:
            return letter
    return "F"
