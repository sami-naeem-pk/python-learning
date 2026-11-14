Number Guessing Game

A simple command-line Number Guessing Game built with Python. The program generates a random secret number between 1 and 10, and the player tries to guess it using hints provided by the game.

Features

- Generates a random secret number between 1 and 10.
- Provides hints when the guess is too high or too low.
- Counts the total number of attempts.
- Displays the number of attempts when the player guesses correctly.
- Offers a menu to play again or exit the game.

Technologies Used

- Python 3
- "random" module

Python Concepts Practiced

- Functions and function calls
- Importing and using modules
- Random number generation
- Variables and assignment
- "while" loops
- Conditional statements ("if", "elif", "else")
- User input and type conversion
- Counters and basic program logic
- "break" and "continue" statements
- f-strings

How to Run

1. Make sure Python 3 is installed on your computer.

2. Clone this repository:
   
   git clone https://github.com/sami-naeem-pk/python-learning.git

3. Navigate to the project directory:
   
   cd python-projects/02-guess-the-number

4. Run the program:
   
   python main.py

Example Gameplay

----- Number Guessing Game -----
1. Play
2. Exit

Enter 1 or 2: 1
Make a guess from 1-10: 5
Think of a larger number.
Make a guess from 1-10: 8
Think of a smaller number.
Make a guess from 1-10: 7
You guessed right in 3 attempt(s)!

Current Limitations

- The secret number is always between 1 and 10.
- The program does not currently validate non-numeric guesses.
- There is no maximum attempt limit.

Future Improvements

- Add input validation and error handling.
- Allow users to select difficulty levels.
- Introduce a maximum number of attempts.
- Track the best score across multiple games.

Author

Sami Naeem

ICS Physics Student | Exploring Computer Science, Programming, Mathematics & Technology.

---

This project is part of my Python learning journey, focused on strengthening programming fundamentals through practical projects.
