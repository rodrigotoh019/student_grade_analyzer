# Student Grade Analyzer (SGA)

This Python project collects student names and scores, then analyzes and displays:
- Highest scorer
- Lowest scorer
- Average score
- List of students who passed (score ≥ 70)
- List of students who failed
- Count of failed students

## 💡 Features

- Clean input collection with validation
- Organized logic using functions
- Results presented using a readable dictionary
- Uses Python concepts like:
  - List comprehensions
  - Lambda functions
  - Dictionary returns
  - Unpacking tuples

## 📂 Files

- `student_grade_analyzer.py` — Main program
- `README.md` — Project description and guide

## 🧠 How It Works

1. User inputs the number of students.
2. For each student:
   - Input name and score.
   - Score is validated to be a float between 0 and 100.
3. The program analyzes the data:
   - Uses `min()`, `max()`, `sum()` with `lambda` and comprehensions.
4. Outputs summary with statistics and list of passed/failed students.

## ✅ Requirements

- Python 3.x

## 🚀 How to Run

```bash
python student_grade_analyzer.py

👨‍💻 Author
Rodrigo Toh (https://github.com/rodrigotoh019)
