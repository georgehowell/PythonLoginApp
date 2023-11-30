# 1. Import the necessary modules and classes for testing:
import pytest
from classes.validator import Validator

# 3. Write test cases for the `Validator` class:
def test_username_is_valid():
    validator = Validator()
    assert validator.username_is_valid('Testing1234') == True
    assert validator.username_is_valid(' ') == False
    assert validator.username_is_valid('1234') == False

# 4. Write test cases for the `password_validator` function:
def test_password_validator():
    validator = Validator()
    assert validator.password_validator('Testing@1234') == True
    assert validator.password_validator('LongPa$$Word1234') == True
    assert validator.password_validator(' ') == False
    assert validator.password_validator('1234567') == False
    assert validator.password_validator('abcdefghijk') == False

