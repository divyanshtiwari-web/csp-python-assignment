# Constraint Satisfaction Problems (CSP) Assignment

**Name:** Divyansh Tiwari
**Roll No:** SE24UCSE213 
**Course:** Artificial Intelligence  
**Assignment:** Project 4  

---

## 📌 Project Summary

This project contains Python implementations designed to resolve variations of **Constraint Satisfaction Problems (CSP)**. A CSP framework establishes rules for processing system variables within confined domains, searching for state configurations where all structural rules are successfully satisfied.

---

## 🧠 Problems Solved

### 1. Traditional Australia Map Coloring
- **Variables:** Regional territories including WA, NT, Q, SA, NSW, V, and T.
- **Goal:** Backtrack state color assignments to ensure bordering regions never maintain identical matching colors.

### 2. Multi-District Telangana Map Coloring
- Evaluates a graph modeled around the **33 individual districts of Telangana**.
- Employs a recursive checking matrix to map out and isolate local boundary constraints using 4 discrete colors.

### 3. Backtracking Sudoku Solver
- Solves a missing-value 9×9 Sudoku board grid structure.
- Progressively inserts legal options using depth-first tree validations.

### 4. Verbal Cryptarithmetic Riddle
- Evaluates the classic constraint expression puzzle: `SEND + MORE = MONEY`.
- Tracks mapping constraints so each alphabet letter translates to an exclusive numerical decimal.

---

## ⚙️ Model Configurations

| Problem Scenario | Variables Monitored | Domain Values | Operational Constraints |
| :--- | :--- | :--- | :--- |
| **Map Optimization** | State Nodes & Subdistricts | {Red, Green, Blue, Yellow} | Intersecting node boundaries cannot match colors |
| **Sudoku Grid** | Unassigned Cells | Integer options {1 through 9} | Values must be unique across rows, columns, and 3x3 blocks |
| **Cryptarithmetic** | String Alphabet Characters | Single Digits {0 through 9} | Distinct translation tokens satisfying mathematical totals |

---

## 🔄 Core Engine Design

All script problems utilize an optimized **Backtracking Search Strategy**. Rather than utilizing heavy brute-force loops, this codebase prunes branches early the moment an invalid state conflicts with active criteria constraints.

---

## 🚀 Execution Instructions

Run the script from your shell command prompt using python3:

```bash
python3 csp_assignment.py

## 📋 Expected Output Logs

```text
Australia Map Coloring:
{'WA': 'Red', 'NT': 'Green', 'Q': 'Red', 'SA': 'Blue', 'NSW': 'Green', 'V': 'Red', 'T': 'Red'}

Telangana Map Coloring (33 Districts):
{'Adilabad': 'Red', 'Bhadradri': 'Red', 'Hyderabad': 'Red', ...}

Solved Sudoku:
[5, 3, 4, 6, 7, 8, 9, 1, 2]
...

Crypt Arithmetic Solution:
{'S': 9, 'E': 5, 'N': 6, 'D': 7, 'M': 1, 'O': 0, 'R': 8, 'Y': 2}

📎 Project Takeaways
This suite highlights the adaptability of formal Constraint Satisfaction parameters across complex relational systems. By defining clean rulesets alongside modular backtracking, tasks like map coloring and cryptographic validation resolve efficiently without unnecessary branch calculations.
