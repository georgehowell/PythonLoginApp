import unittest
from unittest.mock import patch
import questionary
import csv
import string

from classes.userinput import UserInput

users_csv_file = './tests/testdata.csv'
data = {i[0]: i[1:] for i in csv.reader(open(users_csv_file))}
username = "Testing123"
password = "Testing123"


def get_three_attempts():
    while True:
        for x in range(1, 4):
            enterTotalTimes = 3
            triesLeftTimes = enterTotalTimes - x
            password = input("Please provide your password: ")

            if password == data[username][0]:
                print("Hello, " + username + " Welcome to our website!")
                exit()
            if triesLeftTimes == 0:
                answer = data[username][3]
                input_answer = input("Please enter the answer to your security question: ")
                clean_answer = ""
                for char in input_answer:
                    if char not in string.punctuation:
                        clean_answer += char
                if input_answer == clean_answer:
                    new_password = questionary.password("You need to reset your password. Enter a new one now: ").ask()

                    with open(users_csv_file, 'r') as file:
                        csv_reader = csv.reader(file)
                        rows = list(csv_reader)
                        for row in rows:
                            if row[0] == username:
                                row[1] = new_password

                    with open(users_csv_file, 'w', newline='') as file:
                        csv_writer = csv.writer(file)
                        csv_writer.writerows(rows)

                    print("Hello, " + username + " Welcome to our website!")
                    exit()
                else:
                    print("Incorrect Answer! Try again later.")
            else:
                print("Incorrect password. You have " + str(triesLeftTimes) + " attempts left.")


class TestGetThreeAttempts(unittest.TestCase):

    @patch('questionary.password', side_effect=['wrong_pass', 'wrong_pass', 'correct_pass'])
    @patch('builtins.input', return_value='security_answer')
    def test_successful_login(self, mock_input, mock_password):
        with patch('builtins.print') as mock_print:
            get_three_attempts()
            mock_print.assert_called_with("Hello, Testing123 Welcome to our website!")

    @patch('questionary.password', side_effect=['wrong_pass', 'wrong_pass', 'correct_pass'])
    @patch('builtins.input', return_value='incorrect_security_answer')
    def test_incorrect_security_answer(self, mock_input, mock_password):
        with patch('builtins.print') as mock_print:
            get_three_attempts()
            mock_print.assert_called_with("Incorrect Answer! Try again later.")

    @patch('questionary.password', side_effect=['wrong_pass'] * 3)
    @patch('builtins.input', return_value='security_answer')
    def test_password_reset(self, mock_input, mock_password):
        with patch('builtins.print') as mock_print:
            get_three_attempts()
            mock_print.assert_called_with("Hello, Testing123 Welcome to our website!")

if __name__ == '__main__':
    unittest.main()
