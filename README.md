# 🗄️ Mini SQL Database Engine in Python

---

## 📌 Overview

This project is a simplified **in-memory SQL query engine** built from scratch using **Python**. It allows users to execute basic SQL queries on CSV files through a **command-line interface (CLI)**.

The project demonstrates how SQL queries such as **SELECT**, **WHERE**, and **COUNT** are parsed and executed internally without using any database system, ORM, or SQL parsing library. All data processing is done in memory using Python data structures.

---

## 🎯 Objective

The objective of this project is to:
- Understand how SQL queries are processed internally
- Learn how data is loaded, filtered, selected, and aggregated
- Practice algorithmic thinking using Python lists and dictionaries
- Build a basic SQL parser and execution engine from scratch
- Gain foundational skills useful for data engineering roles

---

## ✨ Features

- Loads CSV files into memory as a **list of dictionaries**
- Interactive SQL **Command-Line Interface (REPL)**
- Supports:
  - `SELECT *`
  - `SELECT column1, column2`
  - `WHERE` clause with a single condition
  - Comparison operators: `=`, `!=`, `>`, `<`, `>=`, `<=`
  - `COUNT(*)`
  - `COUNT(column_name)`
- Clear and user-friendly error messages
- Clean, modular, and readable Python code

---

## 🗂️ Project Structure

mini-sql-engine/
├── cli.py
├── parser.py
├── engine.py
├── loader.py
├── data/
│ ├── people.csv
│ └── products.csv
└── README.md


---

## ⚙️ Prerequisites

- Python 3.x installed
- Command Prompt / Terminal

---

## ▶️ How to Run and Test the Project

Open Command Prompt, navigate to the project directory, and run the following commands.  
All valid queries and error test queries are shown below in **one place**.

python cli.py

SELECT * FROM people;
SELECT name, age FROM people;
SELECT * FROM people WHERE age > 30;
SELECT * FROM people WHERE country = 'India';
SELECT product, price FROM products WHERE price >= 200;
SELECT COUNT(*) FROM people;
SELECT COUNT(age) FROM people;
SELECT COUNT(price) FROM products;

SELCT * FROM people;
SELECT salary FROM people;
SELECT * FROM people WHERE age >> 30;
SELECT * FROM employees;

exit

---

### Expected Startup Output

Mini SQL Engine
Type 'exit' to quit
SQL>

---

### Example Output

{'id': '1', 'name': 'Alice', 'age': '30', 'country': 'USA'}
{'id': '2', 'name': 'Bob', 'age': '25', 'country': 'India'}
Result: 5


