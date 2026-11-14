"""
Advanced Calculator Project
---------------------------
A command-line calculator written in Python to practice functions, 
error handling (ValueError, ZeroDivisionError), loops, and user input validation.
"""

def get_num():
    """
    Prompts the user to input two valid numbers.
    Continues to prompt until valid float inputs are provided.
    
    Returns:
        tuple: Two float numbers (n1, n2) entered by the user.
    """
    # Get and validate the first number
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            break 
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            
    # Get and validate the second number
    while True:
        try:
            num2 = float(input("Enter the second number: "))
            break  # Exit the loop if conversion to float succeeds
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    return num1, num2


def add(a, b):
    """Performs addition and prints the result."""
    print(f"{a} + {b} = {a + b}")
    
def subtract(a, b):
    """Performs subtraction and prints the result."""
    print(f"{a} - {b} = {a - b}")
    
def multiply(a, b):
    """Performs multiplication and prints the result."""
    print(f"{a} x {b} = {a * b}")
    
def divide(a, b):
    """
    Performs division and handles division by zero.
    Prints the result or an error message if b is zero.
    """
    try:
        print(f"{a} ÷ {b} = {a / b}")
    except ZeroDivisionError:
        print("Error: You cannot divide by zero.")


# Main program execution loop
while True:
    print("\n----- Calculator Menu -----")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    
    # Get and validate the menu choice input
    try:
        choice = int(input("Choose one from (1, 2, 3, 4, or 5): "))
    except ValueError:
        print("Invalid input. Please enter a number from 1 to 5.")
        continue        
    
    # Execute the appropriate function based on the user's choice
    if choice == 1:
        num1, num2 = get_num()
        add(num1, num2)
    elif choice == 2:
        num1, num2 = get_num()
        subtract(num1, num2)
    elif choice == 3:
        num1, num2 = get_num()
        multiply(num1, num2)
    elif choice == 4:
        num1, num2 = get_num()
        divide(num1, num2)
    elif choice == 5:
        print("Exiting calculator. Have a great day!")
        break
    else:
        print("Invalid choice. Please select an option between 1 and 5.")
        continue
