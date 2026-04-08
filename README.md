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