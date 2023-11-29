import unittest
from unittest.mock import patch
# these are third-party libraries we're using:
import questionary
import csv
from csv import writer

users_csv_file = 'Accounts.csv'
data = {i[0]:i[1:] for i in csv.reader(open(users_csv_file))}


# Import the function or method you want to test
def get_security_question():
    if __name__ == "__main__":
        action1 = (
            questionary.select(
                "Select a security question: ",
                choices=[
                    "In what city were you born?",
                    "What is the name of your favorite pet?",
                    "What is your mother's maiden name?",
                    "What high school did you attend?",
                    "What was the name of your favourite teacher?",
                    "What was the make and model of your first car?",
                    ],
            ).ask()
            or "Not a valid response"
        ),
        action2 = (
            questionary.password("Type your answer: ").ask()
        )
        security_question = {action1, action2}

        List = [security_question]
        with open('../Accounts.csv', 'a') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(List)
            f_object.close()


class TestSecurityQuestion(unittest.TestCase):
    @patch('questionary.select', return_value='What is the name of your favorite pet?')
    @patch('questionary.password', return_value='answer123')
    def test_get_security_question(self, mock_select, mock_password):
        expected_result = {'What is the name of your favorite pet?', 'answer123'}
        result = get_security_question()

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
