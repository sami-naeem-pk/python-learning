import random  # Import the random module to generate a random secret number

def play():
    """
    Handles the core logic of the Number Guessing Game.
    """
    t_guess = 0  # Counter to track the total number of attempts
    n = random.randint(1, 10)  # Generate a random secret number between 1 and 10
    
    while True:
        # Prompt the user for a guess and convert the input string to an integer
        guess = int(input("Make a guess from 1-10: "))
        t_guess = t_guess + 1  # Increment the attempt counter
        
        # Check if the guess matches the target number
        if guess == n:
            print(f"You guessed right in {t_guess} attempt(s)!")
            break  # Exit the guessing loop once correct
        elif guess > n:
            print("Think of a smaller number.")  # Hint: guess is too high
        else:
            print("Think of a larger number.")   # Hint: guess is too low

# Main program loop to display the menu and handle user choices
while True:
    print("\n----- Number Guessing Game -----")
    print("1. Play")
    print("2. Exit")
    
    # Get the menu option from the user
    c = int(input("Enter 1 or 2: "))
    
    if c == 1:
        play()  # Call the play function to start a new game
    elif c == 2:
        print("Thanks for playing! Goodbye.")
        break   # Exit the main program loop and end the script
    else:
        print("Invalid choice. Please enter 1 or 2.")
        continue  # Repeat the menu loop for invalid input
