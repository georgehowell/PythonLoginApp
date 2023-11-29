# 1. Import the necessary modules and classes for testing:
import pytest
import unittest
from unittest.mock import Mock, patch, MagicMock
import os
# import requests
from requests import patch
from users_database import UsersDatabase

# from contextlib import contextmanager

from classes.validator import Validator

class UserInput:
    def __init__(self, inputs):
        self.inputs = inputs
        self.index = 0

    def __enter__(self):
        self.data: main_logic.data = self.UserInput
        return self.clone

    def input(self, prompt):
        value = self.inputs[self.index]
        self.index += 1
        return value
    
    def __exit__(self, inputs):
        if inputs is None:
            self.original[:] = self.clone
        else:
            print('@ListProtect: Error occurred while processing the list. The changes are discarded.')
        return True
UserInput(inputs=True)
        
def main_logic(UserInput):
    data = {
        "username1": ["password1"],
        "username2": ["password2"],
    }
    valid = False

    while(valid == False):
        username = UserInput.input("Please provide your username: ")
        if username == data:
            valid = False
            print("That username is taken. Please try again.")
            return username
        else:
            valid = True
            return username


# 2. Define a fixture to mock the `questionary.password` function:
        
# @contextmanager
# def managed_resource(*args, **kwds):
#     # Code to acquire resource, e.g.:
#     mock_usr = UserInput.data(*args, **kwds)
#     try:
#         yield mock_usr
#     finally:
#         # Code to release resource, e.g.:
#         release_resource(mock_usr)

@pytest.fixture
def mock_user_input():
    validator = Validator()
    with Mock(validator.username_is_valid) as mock_usr:
        mock_usr.return_value.input.side_effect = ['username1', 'password1']
        yield mock_usr

# 3. Write test cases for the `Validator` class:
def test_username_is_valid():
    validator = Validator()
    assert validator.username_is_valid('Testing1234') == True
    assert validator.username_is_valid(' ') == False
    assert validator.username_is_valid('1234') == False


# 4. Write test cases for the main logic using the mocked `user_input.input` function:
def test_main_logic(mock_user_input):
    assert main_logic(mock_user_input.return_value) == None

    mock_user_input.return_value.input.side_effect = ['wrongusername', 'password1']
    assert main_logic(mock_user_input.return_value) == None

    mock_user_input.return_value.input.side_effect = ['username1', 'wrongpassword']
    assert main_logic(mock_user_input.return_value) == None

    mock_user_input.return_value.input.side_effect = ['wrongusername', 'wrongpassword']
    assert main_logic(mock_user_input.return_value) == None


def test_can_get_entry_from_users():
    print("can get row from Accounts.csv")
    users_database = UsersDatabase()
    
    def mock_get_row(username: str, password: str):
        if username == "Testing1234":
            return True
        if password == "Testing1234":
            return True
        users_database.get = Mock(side_effect=mock_get_row)
        assert mock_user_input.get_row(users_database) == True