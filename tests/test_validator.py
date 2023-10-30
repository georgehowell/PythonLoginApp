# 1. Import the necessary modules and classes for testing:
import pytest
from classes.validator import Validator
from classes.userinput import UserInput  # un-comment this @stage2
from unittest import mock
# import requests
import csv
import questionary


users_csv_file = 'users.csv'
data = {i[0]:i[1:] for i in csv.reader(open(users_csv_file))}
min_pw_len = 10
myDict = {
    0: "Hello ",
    1: "Password must be at least 10 characters",
    2: 'Are you a Registered User ("y" or "n")',
    3: "Please provide your username: ",
    4: "That username does not exist. Please try again",
    5: "Please provide your password: ",
    6: ". Welcome to Gelos Software Design Website.",
}

username = "Testing1234"  # comment this stage2


# def main_logic(user_input):
#     data = {
#         "username1": ["password1"],
#         "username2": ["password2"],
#     }

#     while True:
#         username = user_input.input("Please provide your username: ")
#         if username in data:
#             return None
#         else:
#             print("That username does not exist. Please try again")
#             return None

def main_logic():    
    while True:
        for x in range(1, 4):
            enterTotalTimes = 3
            triesLeftTimes = enterTotalTimes - x
            password = questionary.password(myDict[5]).ask()
            
            if password == data[username][0]:
                # Welcome to Gelos Software Design Website
                print(myDict[0] + username + myDict[6])
                return None
            if triesLeftTimes == 0:
                new_password = questionary.password("You need to reset your password. Enter a new one now: ", validate=Validator.password_validator).ask() # § use fn "password_validator()" from the "Validator" class

                with open(users_csv_file, 'r') as file:
                    csv_reader = csv.reader(file)
                    rows = list(csv_reader)
                    for row in rows:
                        if row[0] == username:
                            row[1] = new_password

                with open(users_csv_file, 'w', newline='') as file:
                    csv_writer = csv.writer(file)
                    csv_writer.writerows(rows)

                print(myDict[0] + username + myDict[6])
                return None
            else:    
                print("Incorrect password. You have " + str(triesLeftTimes) + " attempts left.")


# 2. Define a fixture to mock the `questionary.password` function:
@pytest.fixture
def mock_password():
    with mock.patch('questionary.password') as mock_pw:
        yield mock_pw

# @pytest.fixture
# def mock_user_input():
#     with mock.patch('questionary.password') as mock_pw, \
#             mock.patch('main_logic.UserInput') as mock_usr:
#         mock_usr.return_value.input.side_effect = ['username1', 'password1']
#         yield mock_pw, mock_usr
        
        
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
    assert validator.password_validator('Testing@1234') == True
    assert validator.password_validator('LongPa$$Word1234') == True
    assert validator.password_validator(' ') == False
    assert validator.password_validator('1234567') == False
    assert validator.password_validator('abcdefghijk') == False


# 5a. Write test cases for the main logic using the mocked `user_input.input` function:
'''def test_main_logic(mock_user_input):
    mock_pw = mock_user_input
    mock_usr = mock_user_input
    assert main_logic(mock_usr.return_value) == None

    mock_usr.return_value.input.side_effect = ['wrongusername', 'password1']
    assert main_logic(mock_usr.return_value) == None

    mock_usr.return_value.input.side_effect = ['username1', 'wrongpassword']
    assert main_logic(mock_usr.return_value) == None

    mock_usr.return_value.input.side_effect = ['wrongusername', 'wrongpassword']
    assert main_logic(mock_usr.return_value) == None
    '''

# 5b. Write test cases for the main logic using the mocked `questionary.password` function:
def test_main_logic(mock_password):
    mock_password.return_value.ask.return_value = 'Testing@1234'
    assert main_logic() == None

    mock_password.return_value.ask.return_value = 'wrongpassword'
    assert main_logic() == None
