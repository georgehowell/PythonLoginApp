# Import the necessary modules and classes for testing:
import pytest
from classes.userinput import UserInput

def test_user_input(monkeypatch):
    # Mock user inputs
    user_inputs = ['input_1', 'input_2', 'input_3']

    # Create an instance of UserInput
    user_input = UserInput(user_inputs)

    # Use monkeypatch to replace the built-in 'input' function
    monkeypatch.setattr('builtins.input', user_input.input)

    # Test the functionality that uses user input
    result_1 = input("prompt")
    result_2 = input("prompt")
    result_3 = input("prompt")

    # Assert the results
    assert result_1 == 'input_1'
    assert result_2 == 'input_2'
    assert result_3 == 'input_3'
