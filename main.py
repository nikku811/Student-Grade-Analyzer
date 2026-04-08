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


# ---------------------------------------------
#  DISPLAY
# ---------------------------------------------
def print_banner() -> None:
    """Print a styled header banner."""
    print("\n" + "=" * 75)
    print(" " * 22 + "[*]  STUDENT GRADE ANALYZER  [*]")
    print("=" * 75)


def print_table(subjects: list[str], results: list[dict]) -> None:
    """Render all results in a clean, aligned tabular format."""
    col_name   = 18
    col_sub    = 9
    col_total  = 8
    col_pct    = 12
    col_grade  = 7
    col_status = 12

    # -- header ------------------------------
    header  = f"{'No.':<4} {'Name':<{col_name}}"
    header += "".join(f"{sub:^{col_sub}}" for sub in subjects)
    header += f"{'Total':>{col_total}}  {'Percentage':>{col_pct}}  {'Grade':^{col_grade}}  {'Status':<{col_status}}"

    sep = "-" * len(header)
    print(f"\n{sep}")
    print(header)
    print(sep)

    # -- rows --------------------------------
    for idx, r in enumerate(results, start=1):
        row  = f"{idx:<4} {r['Name']:<{col_name}}"
        row += "".join(f"{r[sub]:^{col_sub}}" for sub in subjects)
        row += (
            f"{r['Total']:>{col_total}}"
            f"  {r['Percentage']:>{col_pct - 1}.2f}%"
            f"  {r['Grade']:^{col_grade}}"
            f"  {r['Status']:<{col_status}}"
        )
        print(row)

    print(sep)


def print_summary(subjects: list[str], results: list[dict]) -> None:
    """Print class-level performance summary."""
    total_students = len(results)
    passed  = sum(1 for r in results if "PASS" in r["Status"])
    failed  = total_students - passed
    avg_pct = sum(r["Percentage"] for r in results) / total_students

    top_scorers = sorted(results, key=lambda r: r["Percentage"], reverse=True)[:3]

    grade_dist: dict[str, int] = {}
    for r in results:
        grade_dist[r["Grade"]] = grade_dist.get(r["Grade"], 0) + 1

    print("\n" + "=" * 75)
    print(" " * 27 + "CLASS SUMMARY")
    print("=" * 75)
    print(f"  {'Total Students':<25}: {total_students}")
    print(f"  {'Passed':<25}: {passed}  ({(passed/total_students)*100:.1f}%)")
    print(f"  {'Failed':<25}: {failed}  ({(failed/total_students)*100:.1f}%)")
    print(f"  {'Class Average':<25}: {avg_pct:.2f}%")
    if top_scorers:
        print(f"  {'Highest Percentage':<25}: {top_scorers[0]['Percentage']}%")

    print("\n" + "-" * 75)
    print("  [TROPHY]  TOP SCORERS")
    print("-" * 75)
    for i, scorer in enumerate(top_scorers, 1):
        print(f"  {i}. {scorer['Name']} ({scorer['Percentage']}%)")
        subject_details = " | ".join(
            f"{sub}: {scorer[sub]}" for sub in subjects
        )
        print(f"     Marks : {subject_details}")
        print(f"     Total : {scorer['Total']} / {MAX_PER_SUB * len(subjects)}  |  Grade: {scorer['Grade']}  |  Status: {'PASS' if 'PASS' in scorer['Status'] else 'FAIL'}")
        if i < len(top_scorers):
            print()

    print("\n" + "-" * 75)
    print("  GRADE DISTRIBUTION")
    print("-" * 75)
    for grade_letter in ["A+", "A", "B", "C", "D", "E", "F"]:
        count = grade_dist.get(grade_letter, 0)
        bar   = "#" * count
        print(f"  {grade_letter:^3} | {bar:<20} {count} student(s)")

    print("=" * 75 + "\n")


def save_report(subjects: list[str], results: list[dict]) -> None:
    """Optionally save the results to a CSV report file."""
    out_path = BASE_DIR / "data" / "report.csv"
    fieldnames = ["Name"] + subjects + ["Total", "Percentage", "Grade", "Status"]

    with open(out_path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    # Remove emoji from Status for plain CSV
    print(f"  [SAVED]  Report saved to: {out_path}")


# ─────────────────────────────────────────────
#  MAIN
# ─────────────────────────────────────────────
def main() -> None:
    print_banner()

    # 1. Load data
    print(f"\n  [>>]  Loading data from: {DATA_FILE}")
    subjects, raw_students = load_students(DATA_FILE)
    print(f"  [OK]  {len(raw_students)} student record(s) loaded.")
    print(f"  [OK]  Subjects detected: {', '.join(subjects)}")

    # 2. Calculate
    results = calculate_results(subjects, raw_students)

    # 3. Display table
    print_table(subjects, results)

    # 4. Summary & insights
    print_summary(subjects, results)

    # 5. Save CSV report
    save_report(subjects, results)


if __name__ == "__main__":
    main()
