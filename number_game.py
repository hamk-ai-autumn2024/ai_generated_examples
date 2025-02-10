import random

def number_guessing_game():
    # Constants
    MIN_NUMBER = 1
    MAX_NUMBER = 100
    
    # Generate random number
    target_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    attempts = 0
    
    print(f"Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {MIN_NUMBER} and {MAX_NUMBER}.")
    
    while True:
        try:
            # Get user input
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            # Validate input range
            if guess < MIN_NUMBER or guess > MAX_NUMBER:
                print(f"Please enter a number between {MIN_NUMBER} and {MAX_NUMBER}.")
                continue
            
            # Check guess
            if guess < target_number:
                print("Too low! Try again.")
            elif guess > target_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts!")
                break
                
        except ValueError:
            print("Please enter a valid number.")
            continue

if __name__ == "__main__":
    number_guessing_game()