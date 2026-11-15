"""
CLI Expense Tracker
------------------
A simple command-line application to track daily expenses, view spending history, 
calculate category-wise summaries, and persist data using JSON.
"""

import json
import os

# Global dictionary to store expenses in memory
# Format: { expense_id: {"expense": amount, "category": category_name} }
expenses = {}

def load():
    """Load existing expenses from 'expense.json' if the file exists."""
    global expenses
    if os.path.exists("expense.json"):
        try:
            with open("expense.json", "r") as file:
                data = json.load(file)
                # JSON converts dictionary keys to strings upon saving, 
                # so we convert them back to integers here.
                expenses = {int(k): v for k, v in data.items()}
        except json.JSONDecodeError:
            # Handle corrupted or empty JSON files gracefully
            expenses = {}

def add():
    """Prompt the user for expense details and add it to the expenses dictionary."""
    expense = int(input("Enter expense amount: "))
    category = input("Enter expense category: ")
 
    # Automatically generate a unique ID for the new expense
    expense_id = max(expenses.keys(), default=0) + 1
    expenses[expense_id] = {"expense": expense, "category": category}
    print("✓ Expense has been added!")

def view():
    """Display all recorded expenses in a formatted list."""
    if not expenses:
           print("\n--- No expense found! ---\n")
           return
           
    print("\n----- Expenses -----")
    for expense_id, info in expenses.items():
       print(f"{expense_id}. {info['expense']} [{info['category']}]")
    print("-------------------------\n")
    
def summary():
    """Calculate and display total spending and breakdown by category."""
    if not expenses:
        print("\n--- No expenses to summarize! ---\n")
        return

    total = 0
    category_totals = {}

    # Iterate through all expenses to calculate totals
    for info in expenses.values():
        amount = info["expense"]
        # Standardize category names (remove extra spaces and capitalize)
        category = info["category"].strip().capitalize()

        total += amount
        # Add to the running total for that specific category
        category_totals[category] = category_totals.get(category, 0) + amount

    print("\n----- Expense Summary -----")
    print(f"Total Spending: {total}")
    print("\nBy Category:")
    for category, cat_total in category_totals.items():
        print(f"- {category}: {cat_total}")
    print("---------------------------\n")

def save():
    """Save the current expenses dictionary to 'expense.json' for data persistence."""
    with open("expense.json", "w") as file:
        json.dump(expenses, file, indent=4)
        print("✓ Expenses saved to the file!")

# --- Main Program Execution ---

# Load saved data when the program starts
load()

while True:
    print(" -----Expense Tracker-----")
    print(" 1. Add Expense")
    print(" 2. View Expense")
    print(" 3. View summary")
    print(" 4. Exit")
    
    # Input validation to prevent crashes if the user types letters instead of numbers
    try:
        c = int(input("Enter 1, 2, 3 or 4 : "))
    except ValueError:
        print("❌ Invalid input! Please enter a number from 1 to 4.")
        continue
    
    # Route user choice to the corresponding function
    if c == 1:
        add()
    elif c == 2:
        view()
    elif c == 3:
        summary()
    elif c == 4:
        save()            
        break
