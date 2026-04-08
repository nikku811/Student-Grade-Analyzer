## Author : Ram Narayan

# Student Grade Analyzer 📊

A Python-based command-line tool that automates the process of reading student marks from a CSV file, computing totals and percentages, assigning grades, determining Pass/Fail status, and producing a clean performance report — all in one run.

---

## 📁 Project Structure

```
student-grade-analyzer/
├── data/
│   ├── students.csv       # Input dataset (required)
│   └── report.csv         # Auto-generated output report
├── main.py                # Core Python logic
├── README.md              # Project documentation
└── requirements.txt       # Python dependencies (none beyond stdlib)
```

---

## ✨ Features

| Feature | Description |
|---|---|
| **Data Loading** | Reads any CSV with a `Name` column + subject columns |
| **Auto Calculation** | Computes Total and Percentage per student |
| **Grade Assignment** | A+ / A / B / C / D / E / F based on percentage |
| **Pass / Fail Logic** | 40% cutoff (configurable in `main.py`) |
| **Top 3 Scorers** | Highlights the top three performing students |
| **Grade Distribution** | Bar chart of grade spread across the class |
| **CSV Report Export** | Saves computed results to `data/report.csv` |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10 or later
- No third-party packages required (uses only Python standard library)

### Installation

```bash
git clone https://github.com/<your-username>/student-grade-analyzer.git
cd student-grade-analyzer
```

### Running the Analyzer

```bash
python main.py
```

---

## 📄 Input Format — `data/students.csv`

The CSV **must** include a `Name` column. Every other column is treated as a subject.  
All mark values must be integers between **0** and **100**.

```csv
Name,Math,Science,English,History,Computer
Alice Johnson,85,90,78,88,92
Bob Smith,42,38,55,40,35
...
```

---

## 📊 Grading Scale

| Percentage | Grade |
|---|---|
| ≥ 90% | A+ |
| ≥ 80% | A  |
| ≥ 70% | B  |
| ≥ 60% | C  |
| ≥ 50% | D  |
| ≥ 40% | E  |
| < 40% | F  |

> **Pass/Fail cutoff:** 40% (can be changed via `PASS_CUTOFF` in `main.py`)

---