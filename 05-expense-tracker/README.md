CLI Expense Tracker

A command-line Expense Tracker built with Python. It allows users to record daily expenses, view spending history, calculate total spending, and generate category-wise expense summaries. Expense data is stored in a JSON file for persistent storage.

Features

- Add Expenses: Record an expense amount and its category.
- View Expenses: Display all previously recorded expenses.
- Expense Summary: Calculate total spending across all recorded expenses.
- Category-wise Breakdown: View spending totals for individual categories.
- Persistent Storage: Save expense records in an "expense.json" file.
- Load Existing Data: Automatically load previously saved expenses when the program starts.
- Input Validation: Handle invalid menu choices.
- Error Handling: Handle corrupted or invalid JSON data.

Technologies Used

- Python 3
- "json" module
- "os" module

Python Concepts Practiced

- Functions and function calls
- Dictionaries and nested dictionaries
- Global variables
- File handling ("open()")
- JSON serialization and deserialization
- Exception handling ("try", "except")
- "ValueError" and "JSONDecodeError"
- Conditional statements ("if", "elif", "else")
- "while" and "for" loops
- Dictionary methods ("keys()", "values()", "items()", "get()")
- Dictionary operations
- "max()" function
- String methods ("strip()", "capitalize()")
- Input validation
- Accumulators and running totals
- f-strings

How to Run

1. Make sure Python 3 is installed on your computer.

2. Clone this repository:
   
   git clone https://github.com/sami-naeem-pk/python-learning.git

3. Navigate to the project directory:
   
   cd python-projects/05-expense-tracker

4. Run the program:
   
   python main.py

Data Storage

The application uses a JSON file named "expense.json" to store expense records.

Example structure:

{
    "1": {
        "expense": 500,
        "category": "Food"
    },
    "2": {
        "expense": 1200,
        "category": "Transport"
    },
    "3": {
        "expense": 800,
        "category": "Food"
    }
}

The application loads existing expense records when it starts and saves updated data when the user exits.

Note: The "expense.json" file is created automatically when the application saves expenses for the first time.

Example Usage

-----Expense Tracker-----
1. Add Expense
2. View Expense
3. View summary
4. Exit

Enter 1, 2, 3 or 4: 1

Enter expense amount: 500
Enter expense category: Food

✓ Expense has been added!

Example Expense Summary

----- Expense Summary -----
Total Spending: 2500

By Category:
- Food: 1300
- Transport: 1200
---------------------------

Current Limitations

- Expense amounts must be entered as whole numbers.
- Expense categories are entered manually.
- Users cannot edit or delete existing expenses.
- Expenses are saved when the user exits the application.
- The application does not track expense dates.
- Data is stored locally in a JSON file rather than a database.

Future Improvements

- Add expense date tracking.
- Allow users to edit and delete expense records.
- Implement input validation for expense amounts.
- Introduce monthly and weekly spending summaries.
- Add budget limits and spending alerts.
- Introduce data visualization using Matplotlib.
- Use SQLite for more structured data storage.

Author

Sami Naeem

ICS Physics Student | Exploring Computer Science, Programming, Mathematics & Technology.

---

This project is part of my Python learning journey, focused on strengthening programming fundamentals through practical projects.
