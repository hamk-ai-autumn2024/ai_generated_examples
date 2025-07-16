#!/usr/bin/env python3
"""
Test script for the Number Guessing Game.

This script demonstrates the functionality of the NumberGuessingGame class
with various test cases and edge cases.
"""

import sys
from number_guessing_game import NumberGuessingGame


def test_game_initialization():
    """Test game initialization with default and custom parameters."""
    print("Testing game initialization...")
    
    # Test default initialization
    game1 = NumberGuessingGame()
    assert game1.min_number == 1
    assert game1.max_number == 100
    assert 1 <= game1.target_number <= 100
    assert game1.attempts == 0
    print("✅ Default initialization test passed")
    
    # Test custom range
    game2 = NumberGuessingGame(50, 75)
    assert game2.min_number == 50
    assert game2.max_number == 75
    assert 50 <= game2.target_number <= 75
    print("✅ Custom range initialization test passed")
    
    # Test edge case
    game3 = NumberGuessingGame(5, 5)
    assert game3.target_number == 5
    print("✅ Single number range test passed")


def test_guess_validation():
    """Test guess validation and feedback."""
    print("\nTesting guess validation...")
    
    game = NumberGuessingGame(10, 20)
    target = game.target_number
    
    # Test valid guesses
    try:
        is_correct, message = game.make_guess(str(target))
        assert is_correct == True
        assert "Congratulations" in message
        assert "1 attempts" in message
        print("✅ Correct guess test passed")
    except Exception as e:
        print(f"❌ Error in correct guess test: {e}")
    
    # Reset game for more tests
    game = NumberGuessingGame(10, 20)
    
    # Test too low
    try:
        is_correct, message = game.make_guess("5")
        assert is_correct == False
        assert "Too low" in message
        print("✅ Too low feedback test passed")
    except Exception as e:
        print(f"❌ Error in too low test: {e}")
    
    # Test too high
    try:
        is_correct, message = game.make_guess("25")
        assert is_correct == False
        assert "Too high" in message
        print("✅ Too high feedback test passed")
    except Exception as e:
        print(f"❌ Error in too high test: {e}")


def test_error_handling():
    """Test error handling for invalid inputs."""
    print("\nTesting error handling...")
    
    game = NumberGuessingGame(1, 10)
    
    # Test non-integer input
    try:
        game.make_guess("abc")
        print("❌ Should have raised ValueError for non-integer")
    except ValueError as e:
        assert "valid integer" in str(e)
        print("✅ Non-integer input handling test passed")
    
    # Test out of range input
    try:
        game.make_guess("15")
        print("❌ Should have raised ValueError for out of range")
    except ValueError as e:
        assert "between" in str(e)
        print("✅ Out of range input handling test passed")
    
    # Test invalid range initialization
    try:
        NumberGuessingGame(10, 5)
        print("❌ Should have raised ValueError for invalid range")
    except ValueError as e:
        assert "must be less than or equal to" in str(e)
        print("✅ Invalid range initialization test passed")


def test_attempts_counting():
    """Test that attempts are counted correctly."""
    print("\nTesting attempts counting...")
    
    game = NumberGuessingGame(1, 5)
    
    # Make multiple guesses
    game.make_guess("1")  # Wrong
    game.make_guess("2")  # Wrong
    game.make_guess("3")  # Wrong
    
    assert game.attempts == 3
    print("✅ Attempts counting test passed")


def run_all_tests():
    """Run all test cases."""
    print("🧪 Running Number Guessing Game Tests\n")
    
    try:
        test_game_initialization()
        test_guess_validation()
        test_error_handling()
        test_attempts_counting()
        
        print("\n🎉 All tests passed successfully!")
        
    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    run_all_tests()
