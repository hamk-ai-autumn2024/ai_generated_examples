# Number Guessing Game 🎯

A comprehensive, elegant Python implementation of the classic number guessing game with robust error handling and clean architecture.

## Features

- **Random number generation** between configurable range (default: 1-100)
- **Comprehensive error handling** for all user inputs
- **Clear feedback** for too high/too low guesses
- **Attempt tracking** with final count displayed upon success
- **Clean, object-oriented design** with separation of concerns
- **Type hints** for better code clarity
- **Extensive documentation** with docstrings
- **Easy configuration** through constants
- **Test suite** included for validation

## Quick Start

### Basic Usage
```bash
python number_guessing_game.py
```

### Run Tests
```bash
python test_number_guessing_game.py
```

## Game Configuration

The game uses constants that can be easily modified:

```python
# Game configuration constants
MIN_NUMBER: int = 1      # Minimum value for random number
MAX_NUMBER: int = 100    # Maximum value for random number
MAX_ATTEMPTS: int = 10   # Optional limit for difficulty
```

## Architecture

### Classes

#### `NumberGuessingGame`
Main game class that encapsulates all game logic.

**Key Methods:**
- `__init__(min_number=1, max_number=100)` - Initialize new game
- `make_guess(guess: str) -> Tuple[bool, str]` - Process user guess
- `get_range() -> Tuple[int, int]` - Get current number range

### Functions

- `get_user_input(prompt: str) -> str` - Safe user input handling
- `display_welcome_message(game: NumberGuessingGame)` - Show game intro
- `play_game()` - Main game loop
- `main()` - Entry point with error handling

## Error Handling

The game handles all common error scenarios:
- ❌ Non-integer inputs
- ❌ Out of range numbers
- ❌ Invalid range initialization
- ❌ Keyboard interrupts (Ctrl+C)
- ❌ EOF errors (Ctrl+D)

## Example Usage

```python
from number_guessing_game import NumberGuessingGame

# Create custom game
game = NumberGuessingGame(1, 50)  # Range 1-50

# Make guesses
is_correct, message = game.make_guess("25")
print(message)  # "Too low! Try a higher number."

is_correct, message = game.make_guess("30")
print(message)  # "Congratulations! You guessed the number in 2 attempts!"
```

## Design Principles

- **Elegant & Short**: Minimal, clean code
- **Constants**: No magic values, easy configuration
- **Type Safety**: Full type hints
- **Documentation**: Comprehensive docstrings
- **Error Handling**: Graceful handling of all edge cases
- **Testing**: Complete test suite included
- **Modern Python**: Uses latest Python features (f-strings, type hints)

## Requirements

- Python 3.7+ (for type hints support)
- No external dependencies

## License

Open source - feel free to use and modify!
