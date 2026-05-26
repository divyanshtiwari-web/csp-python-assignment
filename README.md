# csp-python-assignment
Constraint Satisfaction Problems (CSP) Assignment
Name: Shiven Sethi
Roll No: SE24UCSE227
Course: Artificial Intelligence
Assignment: Project 4

📌 Project Summary
This project contains Python implementations designed to resolve variations of Constraint Satisfaction Problems (CSP). A CSP framework establishes rules for processing system variables within confined domains, searching for state configurations where all structural rules are successfully satisfied.

🧠 Problems Solved
1. Traditional Australia Map Coloring
Variables: Regional territories including WA, NT, Q, SA, NSW, V, and T.
Goal: Backtrack state color assignments to ensure bordering regions never maintain identical matching colors.
2. Multi-District Telangana Map Coloring
Evaluates a graph modeled around the 33 individual districts of Telangana.
Employs a recursive checking matrix to map out and isolate local boundary constraints using 4 discrete colors.
3. Backtracking Sudoku Solver
Solves a missing-value 9×9 Sudoku board grid structure.
Progressively inserts legal options using depth-first tree validations.
4. Verbal Cryptarithmetic Riddle
Evaluates the classic constraint expression puzzle: SEND + MORE = MONEY.
Tracks mapping constraints so each alphabet letter translates to an exclusive numerical decimal.
⚙️ Model Configurations
Problem Scenario	Variables Monitored	Domain Values	Operational Constraints
Map Optimization	State Nodes & Subdistricts	{Red, Green, Blue, Yellow}	Intersecting node boundaries cannot match colors
Sudoku Grid	Unassigned Cells	Integer options {1 through 9}	Values must be unique across rows, columns, and 3x3 blocks
Cryptarithmetic	String Alphabet Characters	Single Digits {0 through 9}	Distinct translation tokens satisfying mathematical totals
🔄 Core Engine Design
All script problems utilize an optimized Backtracking Search Strategy. Rather than utilizing heavy brute-force loops, this codebase prunes branches early the moment an invalid state conflicts with active criteria constraints.
