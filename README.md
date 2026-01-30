# 💰 Monthly Expense Tracker (Python)

A simple Python-based command-line application that helps users track their monthly expenses, categorize spending, and monitor their budget effectively.  
All expenses are stored in a CSV file, making the data persistent and easy to analyze later.

---

## 📌 Features
- Add expenses with name, amount, and category
- Choose categories using an interactive menu
- Store expense data in a CSV file
- View total spending grouped by category
- Track total monthly spending
- Calculate remaining budget
- Estimate daily budget based on remaining days in the month

---

## 🛠 Technologies Used
- Python
- CSV file handling
- `datetime` and `calendar` modules

---

## 📂 Project Structure
```text
tracker/
│── expense_tracker.py   # Main application logic
│── expense.py           # Expense class
│── expenses.csv         # Stores expense data
│── .gitignore
│── README.md
 ```
---

# ▶️ How to Run
Clone the repository:

git clone https://github.com/ArnavS-maker/tracker.git

Navigate into the project directory:
```
cd tracker
```
Run the application:
```
python expense_tracker.py
```
---

# 🧾 How the Application Works
The program prompts the user to enter an expense name and amount.

The user selects an expense category from an interactive menu.

The expense is saved to a CSV file (expenses.csv).

The program reads all stored expenses from the CSV file.

Expenses are grouped by category and summarized.

The program calculates:

Total monthly spending

Remaining budget

Daily budget based on remaining days in the month

All results are displayed in the terminal.

---

# 💡 Expense Categories
🍌 Food

🏠 Home

🏢 Work

🎉 Fun

❓ Others

---

# 🎯 Purpose of This Project
This project was created to practice and improve:

Python fundamentals

Object-Oriented Programming (OOP)

File handling using CSV files

Working with dates using datetime and calendar

Writing clean and modular Python code

Using Git and GitHub for version control

---

# 🚀 Future Improvements
Input validation for negative or invalid amounts

Monthly expense summaries

Category-wise visualizations

Exporting reports

GUI or web-based version

---

# 👤 Author:

Arnav Srivastava

---
