# ==========================================
# PYTHON CLI QUIZ GAME
# A simple interactive trivia game to test Python basics.
# ==========================================

# Define the questions, options, and correct answers using a nested dictionary.
# Outer keys are question IDs ("q1", "q2", etc.).
# Inner dictionaries contain the question string, a list of options, 
# and the index of the correct option as a string.
questions = {
    "q1": {
        "question": "1. What is the correct file extension for Python files?",
        "options": [".pt", ".py", ".python", ".txt"],
        "correct": "1"  # Index 1 corresponds to '.py'
    },
    "q2": {
        "question": "2. Which keyword is used to define a function in Python?",
        "options": ["function", "f", "def", "define"],
        "correct": "2"  # Index 2 corresponds to 'def'
    },
    "q3": {
        "question": "3. Which built-in Python data structure is ordered and mutable (changeable)?",
        "options": ["Tuple", "List", "Dictionary", "Set"],
        "correct": "1"  # Index 1 corresponds to 'List'
    },
    "q4": {
        "question": "4. How do you start a for loop that iterates over a list named numbers?",
        "options": [
            "for numbers in item:",
            "for item inside numbers:",
            "for item in numbers:",
            "loop item through numbers:"
        ],
        "correct": "2"  # Index 2 corresponds to 'for item in numbers:'
    },
    "q5": {
        "question": "5. Which function is used to get the number of items in a list?",
        "options": ["size()", "count()", "length()", "len()"],
        "correct": "3"  # Index 3 corresponds to 'len()'
    },
    "q6": {
        "question": "6. How do you correctly create an empty dictionary in Python?",
        "options": ["my_dict = {}", "my_dict = []", "my_dict = ()", "my_dict = dict()"],
        "correct": "0"  # Index 0 corresponds to 'my_dict = {}'
    },
    "q7": {
        "question": "7. Which list method is used to add a new item to the very end of the list?",
        "options": ["add()", "append()", "insert()", "push()"],
        "correct": "1"  # Index 1 corresponds to 'append()'
    },
    "q8": {
        "question": "8. How do you write a single-line comment in Python?",
        "options": [
            "// This is a comment",
            "/* This is a comment */",
            "# This is a comment",
            "<!-- This is a comment -->"
        ],
        "correct": "2"  # Index 2 corresponds to '# This is a comment'
    },
    "q9": {
        "question": "9. Which keyword is used to check if a key exists inside a dictionary?",
        "options": ["exists", "in", "has", "contains"],
        "correct": "1"  # Index 1 corresponds to 'in'
    },
    "q10": {
        "question": "10. What is the output of len([10, 20, 30, 40])?",
        "options": ["3", "4", "5", "30"],
        "correct": "1"  # Index 1 corresponds to '4'
    }
}

# Initialize the user's score to 0 before the game starts
score = 0

# Loop through each question in the dictionary using .items() to get both key and value
for q_id, q_data in questions.items():
    # Print the question text with a leading newline for better spacing
    print("\n" + q_data["question"])

    # Loop through the options list, using enumerate() to get both the index (0, 1, 2...) and the option text
    for index, option in enumerate(q_data["options"]):
        print(f"  {index}. {option}")

    # Prompt the user to type their answer (returns a string)
    user_answer = input("Enter the option number: ")

    # Check if the user's input matches the correct option index
    if user_answer == q_data["correct"]:
        print("Correct!")
        score += 1  # Increment the score by 1 for a correct answer
    else:
        print(f"Wrong! The correct option was {q_data['correct']}.")

# Game over message displaying the final score out of total questions
print(f"\nGame over! Your final score is {score}/{len(questions)}.")
