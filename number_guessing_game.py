#!/usr/bin/env python3
"""
Number Guessing Game

A simple interactive number guessing game where the user attempts to guess
a randomly generated number within a specified range.

Author: AI Assistant
Date: 2025
"""

import random
from typing import Tuple


# Game configuration constants
MIN_NUMBER: int = 1
MAX_NUMBER: int = 100
MAX_ATTEMPTS: int = 10  # Optional limit for difficulty adjustment


class NumberGuessingGame:
    """
    A class representing the number guessing game.
    
    This class encapsulates the game logic for a number guessing game where
    the player attempts to guess a randomly generated number within a range.
    
    Attributes:
        min_number (int): The minimum value for the random number
        max_number (int): The maximum value for the random number
        target_number (int): The randomly generated number to guess
        attempts (int): Number of attempts made by the player
    """
    
    def __init__(self, min_number: int = MIN_NUMBER, max_number: int = MAX_NUMBER) -> None:
        """
        Initialize a new game instance.
        
        Args:
            min_number: The minimum value for the random number (default: 1)
            max_number: The maximum value for the random number (default: 100)
            
        Raises:
            ValueError: If min_number is greater than max_number
        """
        if min_number > max_number:
            raise ValueError(f"min_number ({min_number}) must be less than or equal to max_number ({max_number})")
        
        self.min_number: int = min_number
        self.max_number: int = max_number
        self.target_number: int = self._generate_random_number()
        self.attempts: int = 0
    
    def _generate_random_number(self) -> int:
        """
        Generate a random number within the specified range.
        
        Returns:
            A random integer between min_number and max_number (inclusive)
        """
        return random.randint(self.min_number, self.max_number)
    
    def get_range(self) -> Tuple[int, int]:
        """
        Get the current number range.
        
        Returns:
            A tuple containing (min_number, max_number)
        """
        return (self.min_number, self.max_number)
    
    def make_guess(self, guess: str) -> Tuple[bool, str]:
        """
        Process a player's guess.
        
        Args:
            guess: The player's guess as a string
            
        Returns:
            A tuple containing (is_correct: bool, message: str)
            
        Raises:
            ValueError: If the input is not a valid integer
        """
        try:
            guess_number = int(guess.strip())
        except ValueError:
            raise ValueError("Please enter a valid integer.")
        
        if not (self.min_number <= guess_number <= self.max_number):
            raise ValueError(
                f"Please enter a number between {self.min_number} and {self.max_number}."
            )
        
        self.attempts += 1
        
        if guess_number < self.target_number:
            return False, f"Too low! Try a higher number."
        elif guess_number > self.target_number:
            return False, f"Too high! Try a lower number."
        else:
            return True, f"Congratulations! You guessed the number in {self.attempts} attempts!"


def get_user_input(prompt: str) -> str:
    """
    Get user input with error handling.
    
    Args:
        prompt: The prompt message to display
        
    Returns:
        The user's input as a string
    """
    while True:
        try:
            return input(prompt)
        except (KeyboardInterrupt, EOFError):
            print("\nGame interrupted. Goodbye!")
            exit(0)


def display_welcome_message(game: NumberGuessingGame) -> None:
    """
    Display the welcome message and game instructions.
    
    Args:
        game: The NumberGuessingGame instance
    """
    min_num, max_num = game.get_range()
    print("=" * 50)
    print("🎯 NUMBER GUESSING GAME 🎯")
    print("=" * 50)
    print(f"I'm thinking of a number between {min_num} and {max_num}.")
    print("Can you guess what it is?")
    print("-" * 50)


def play_game() -> None:
    """
    Main game loop for the number guessing game.
    
    This function orchestrates the entire game flow from initialization
    to completion.
    """
    game = NumberGuessingGame()
    display_welcome_message(game)
    
    while True:
        try:
            guess = get_user_input("\nEnter your guess: ")
            is_correct, message = game.make_guess(guess)
            print(message)
            
            if is_correct:
                break
                
        except ValueError as e:
            print(f"❌ Error: {e}")
        except KeyboardInterrupt:
            print("\n\nGame interrupted. Thanks for playing!")
            break
    
    print("\nThanks for playing! 🎮")


def main() -> None:
    """
    Entry point for the number guessing game application.
    
    This function handles the main execution flow and provides
    a clean interface for starting the game.
    """
    try:
        play_game()
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        print("Please restart the game.")


if __name__ == "__main__":
    main()
