# 1. Import the necessary modules and classes for testing:

import pytest
from classes.validator import Validator
# from questionary import mock, Question
import mock

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
    6: ". Welcome to Gelos Software Design Website."
}
valid = False

username = "Testing123"

def password_validator(password):
    if len(password) < min_pw_len:
        return myDict[1]
    else:
        return True



# def password_function(input_func=None):
#    input_func = input_func or input

# @mock.patch('mymodule.os')
# def test_rm(self, mock_os):
#     Validator("any path")
#     # test that rm called os.remove with the right parameters
#     mock_os.remove.assert_called_with("any path")

# def username_function(input_func=None):
#    input_func = input_func or input
#    return username_function


def main_logic():
    # while True:
    # username = input("Please provide your username: ")
    # if username == username in data:
    #     break
    # else:
    #     print("That username does not exist. Please try again")
    #     continue

    while True:
        for x in range(1, 4):
            enterTotalTimes = 3
            triesLeftTimes = enterTotalTimes - x
            password = questionary.password(myDict[5], validate=password_validator).ask() # § use fn "password_validator()"
            if password in data[username]:
                # Welcome to Gelos Software Design Website
                print(myDict[0] + username + myDict[6])
                exit()
            if triesLeftTimes == 0:
                print("You have no more attempts! Goodbye.")
                exit()
            else:    
                print("Incorrect password. You have " + str(triesLeftTimes) + " attempts left.")
    


# 2. Define a fixture to mock the `questionary.password` function:
@pytest.fixture
def mock_password():
    with mock.patch('questionary.password') as mock_pw:
        yield mock_pw
        
        
# 3. Write test cases for the `Validator` class:
def test_username_is_valid():
    validator = Validator()
    assert validator.username_is_valid('Reval') == True
    assert validator.username_is_valid('') == False
    assert validator.username_is_valid('1234') == False

# Add more test cases for other methods in the Validator class if needed

# 4. Write test cases for the `password_validator` function:

def test_password_validator():
    assert password_validator('password') == myDict[1]
    assert password_validator('longpassword') == True
    assert password_validator('') == myDict[1]
    assert password_validator('123456789') == myDict[1]

# 5. Write test cases for the main logic using the mocked `questionary.password` function:

def test_main_logic(mock_password):
    mock_password.return_value.ask.return_value = 'password'
    assert main_logic() == myDict[0] + username + myDict[6]

    mock_password.return_value.ask.return_value = 'wrongpassword'
    assert main_logic() == "Incorrect password. You have 2 attempts left."
