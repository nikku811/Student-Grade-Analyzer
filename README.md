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

## 📤 Sample Output

```
===========================================================================
                      [*]  STUDENT GRADE ANALYZER  [*]
===========================================================================

  [>>]  Loading data from: e:\VAC_SJ\student-grade-analyzer\data\students.csv
  [OK]  50 student record(s) loaded.
  [OK]  Subjects detected: Math, Science, English, History, Computer

-------------------------------------------------------------------------------
No.  Name                Math     Science  English  History  Computer  Total  Percentage   Grade   Status
...
===========================================================================
                           CLASS SUMMARY
===========================================================================
  Total Students          : 50
  Passed                  : 35  (70.0%)
  Failed                  : 15  (30.0%)
  Class Average           : 68.42%

---------------------------------------------------------------------------
  [TROPHY]  TOP SCORERS
---------------------------------------------------------------------------
  1. Kiran Pande (96.0%)
     Marks : Math: 98 | Science: 96 | English: 95 | History: 92 | Computer: 99
     Total : 480 / 500  |  Grade: A+  |  Status: PASS

  2. Jyoti Sharma (96.0%)
     Marks : Math: 96 | Science: 94 | English: 98 | History: 95 | Computer: 97
     Total : 480 / 500  |  Grade: A+  |  Status: PASS

  3. Pooja Verma (94.4%)
     Marks : Math: 95 | Science: 98 | English: 92 | History: 90 | Computer: 97
     Total : 472 / 500  |  Grade: A+  |  Status: PASS
```

---

## ⚙️ Configuration

Open `main.py` and adjust these constants at the top:

```python
PASS_CUTOFF  = 40    # Minimum percentage to PASS
MAX_PER_SUB  = 100   # Maximum marks per subject
```

---

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Libraries:** `csv`, `os`, `pathlib` (all standard library)
- **Editor:** Visual Studio Code
- **Version Control:** Git & GitHub

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).
