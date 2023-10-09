# 1. Import the necessary modules and classes for testing:
import pytest
from classes.validator import Validator
import mock
# import requests
import csv
import questionary


users_csv_file = 'users.csv'
data = {i[0]:i[1:] for i in csv.reader(open(users_csv_file))}
min_pw_len = 10

def password_validator(password):
    if len(password) < min_pw_len:
        return "Password must be at least 10 characters"
    else:
        return True

class UserInput:
    def __init__(self, inputs):
        self.inputs = inputs
        self.index = 0

    def input(self, prompt):
        value = self.inputs[self.index]
        self.index += 1
        return value

def main_logic(user_input):
    data = {
        "username1": ["password1"],
        "username2": ["password2"],
    }

    while True:
        username = user_input.input("Please provide your username: ")
        if username in data:
            break
        else:
            print("That username does not exist. Please try again")
            continue

    while True:
        for x in range(1, 4):
            enterTotalTimes = 3
            triesLeftTimes = enterTotalTimes - x
            password = questionary.password("Please provide your password: ", validate=password_validator).ask() 
            if password in data[username]:
                print( "Hello " + username + ". Welcome to Gelos Software Design Website.")
                return None

            if triesLeftTimes == 0:
                print("You have no more attempts! Goodbye.")
                return None
                    
            else:
                print("Incorrect password. You have " + str(triesLeftTimes) + " attempts left.")
    


# 2. Define a fixture to mock the `questionary.password` function:
@pytest.fixture
def mock_user_input():
    with mock.patch('questionary.password') as mock_pw, \
            mock.patch('main_logic.UserInput') as mock_usr:
        mock_usr.return_value.input.side_effect = ['username1', 'password1']
        yield mock_pw, mock_usr
        
        
# 3. Write test cases for the `Validator` class:
def test_username_is_valid():
    validator = Validator()
    assert validator.username_is_valid('Testing1234') == True
    assert validator.username_is_valid(' ') == False
    assert validator.username_is_valid('1234') == False

# Add more test cases for other methods in the Validator class if needed


# 4. Write test cases for the `password_validator` function:
def test_password_validator():
    validator = Validator()
    assert validator.password_validator('Testing1234') == True
    assert validator.password_validator('LongPassWord') == True
    assert validator.password_validator(' ') == False
    assert validator.password_validator('1234567') == False


# 5a. Write test cases for the main logic using the mocked `user_input.input` function:
def test_main_logic(mock_user_input):
    mock_pw = mock_user_input
    mock_usr = mock_user_input
    assert main_logic(mock_usr.return_value) == None

    mock_usr.return_value.input.side_effect = ['wrongusername', 'password1']
    assert main_logic(mock_usr.return_value) == None

    mock_usr.return_value.input.side_effect = ['username1', 'wrongpassword']
    assert main_logic(mock_usr.return_value) == None

    mock_usr.return_value.input.side_effect = ['wrongusername', 'wrongpassword']
    assert main_logic(mock_usr.return_value) == None
