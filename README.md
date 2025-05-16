# Student Grade Analyzer (SGA)

## 📌 Overview
The **Student Grade Analyzer (SGA)** is Rodrigo Toh's first major Python project focused on developing a CLI-based student management system. It allows users to input student names and scores, evaluate performance, sort data, and eventually manage student records using a simple CLI tool.

---

## ✅ Current Features

- Input student names and validate formatting (excludes most special characters, allows names like O'Connor and Peña).
- Accepts only numerical scores between **1 and 100**.
- Filters students into **Passed** (score ≥ 75) and **Failed** categories.
- Calculates **overall class average score**.
- Identifies **highest and lowest scoring students**.
- Displays results in clean, formatted outputs.
- Supports **sorted output by name** (ascending).

---

## 🛠️ In Progress

### 🔹 Input Validation Fixes
- Strengthened filtering of special characters in names.
- Handled rare score loopholes like `-0`.

### 🔹 CLI Tool (Command-Line Interface)
- Interactive menu for users to:
  1. View all students
  2. Add student
  3. Edit student
  4. Remove student
  5. Sort student data
  6. Exit

### 🔹 CRUD Operations
- Functions to **Create**, **Read**, **Update**, and **Delete** student entries.

---

## 🧪 Planned Features (v2: Multi-Score Version)

- Each student will have **4 scores**: `1st Quarter`, `2nd Quarter`, `3rd Quarter`, and `4th Quarter`.
- Compute **average per student**.
- Integrate a **letter grading system** (A, B, C, D, F) based on averaged score.
- Possible display of data using `tabulate` for clean table-like CLI output.

---

## 📂 GitHub Strategy

- The current version remains in `main` branch.
- A new development branch (e.g., `multi-score-version`) will be created for the upcoming v2 overhaul.
- All major rewrites will be documented in future commits and README updates.

---

## 👨‍💻 Author

**Rodrigo Toh**  
- Future AI/ML Developer  
- GitHub: [https://github.com/yourprofile](https://github.com/yourprofile)

---

> This project reflects Rodrigo's structured and deep learning process as he transitions from fundamentals to real-world Python applications. It's a living project that evolves as he grows.