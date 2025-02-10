import random
import tkinter as tk
from tkinter import messagebox

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        
        # Constants
        self.MIN_NUMBER = 1
        self.MAX_NUMBER = 100
        
        # Generate random number
        self.target_number = random.randint(self.MIN_NUMBER, self.MAX_NUMBER)
        self.attempts = 0
        
        # Create GUI elements
        self.label = tk.Label(root, text=f"I'm thinking of a number between {self.MIN_NUMBER} and {self.MAX_NUMBER}.")
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)
        
        self.button = tk.Button(root, text="Guess", command=self.check_guess)
        self.button.pack(pady=5)
        
        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)
    
    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1
            
            # Validate input range
            if guess < self.MIN_NUMBER or guess > self.MAX_NUMBER:
                self.result_label.config(text=f"Please enter a number between {self.MIN_NUMBER} and {self.MAX_NUMBER}.")
                return
            
            # Check guess
            if guess < self.target_number:
                self.result_label.config(text="Too low! Try again.")
            elif guess > self.target_number:
                self.result_label.config(text="Too high! Try again.")
            else:
                messagebox.showinfo("Congratulations!", f"You guessed the number in {self.attempts} attempts!")
                self.reset_game()
                
        except ValueError:
            self.result_label.config(text="Please enter a valid number.")
    
    def reset_game(self):
        self.target_number = random.randint(self.MIN_NUMBER, self.MAX_NUMBER)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.label.config(text=f"I'm thinking of a number between {self.MIN_NUMBER} and {self.MAX_NUMBER}.")

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()