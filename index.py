# - - - - - - - - - - - - -"Login or Signup"  - - - - - - - - - - - - -
#                            George Howell
#                              367907258
#      
# Login System with 'Register', validation, and password generator

# - - - - - - - - - - - - - - -Libraries - - - - - - - - - - - - - - -
import csv
from csv import writer
import string
import random
import re
import ast

# used to hide password and secret question answer:
import questionary


# - - - - - - - -  - - - - global variables: - - - - - - - - - - - - -
users_csv_file = 'Accounts.csv'
#open the users.csv file, excluding the header:
data = {i[0]:i[1:] for i in csv.reader(open(users_csv_file))}
min_pw_len = 8
# replace error messages, input text, warning messages, and other text with dictionary values, so as to "d.r.y.""
myDict = {
    0: "Hello ",
    1: "Password must be at least 10 characters",
    2: 'Are you a Registered User ("y" or "n")',
    3: "Please provide your username: ",
    4: "That username does not exist. Please try again",
    5: "Please provide your password: ",
    6: ". Welcome to Gelos Software Design Website.",
    7: "You have no more attempts! Goodbye.",
    8: "Incorrect password.",
    9: 'Do you wish to Sign Up ("y" or "n")',
    10: "That username is taken. Please try again.",
    11: 'Would you like the system to generate a password for you ("y" or "n")',
    12: "Enter your new password length: ",
    13: "Not a valid response",
    14: "Please enter your first name: ",
    15: "Please enter your last name: ",
    16: "Goodbye!",
    17: "Password must have at least one special character",
    18: "Password must have at least one capital letter",
    19: "Password must contain a number",
    20: "In what city were you born?",
    21: "What is the name of your favorite pet?",
    22: "What is your mother's maiden name?",
    23: "What high school did you attend?",
    24: "What was the name of your favourite teacher?",
    25: "What was the make and model of your first car?"
}
valid = False

# - - - - - - - - - - - - - -  classes:  - - - - - - - - - - - - - - -


# - - - - - - - - - - - - - - functions: - - - - - - - - - - - - - - -
# password_validator:
def password_validator(password):
    criteria_count = 0

    if re.search(r'[@#$%^&+=]', password):
        criteria_count += 1
    if re.search(r'[A-Z]', password):
        criteria_count += 1
    if re.search(r'[0-9]', password):
        criteria_count += 1
    if len(password) >= min_pw_len:
        criteria_count += 1

    if criteria_count >= 3:
        return True
    else:
        return "Password must meet at least 3 out of 4 criteria"



# part 1a: store password, or, reset password:
def reset_pw():
    new_password = questionary.password("Enter a new password: ", validate=password_validator).ask()
    with open(users_csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        rows = list(csv_reader)
        for row in rows:
            if row[0] == username:
                row[1] = new_password
    with open(users_csv_file, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(rows)
    menu()

    
# part 1b: select a secret question and answer:
def secret_QandA():
    if __name__ == "__main__":
        action1 = (
            questionary.select(
                "Select a security question: ",
                choices=[myDict[20],myDict[21],myDict[22],myDict[23],myDict[24],myDict[25]],
            ).ask()
            or myDict[13]
        ),
        action2 = (
            questionary.password("Type your answer: ").ask()
                )
    security_question = {action1, action2}
    # return security_question
    with open(users_csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        rows = list(csv_reader)
    for row in rows:
        if row[0] == username:
            row[4] = security_question
    with open(users_csv_file, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(rows)
    menu()


# part 2: write to file:
def write_to_file_all():
    # Open our existing CSV file in append mode
    # Create a file object for this file
    with open(users_csv_file, 'a') as f_object:
        # Pass this file object to csv.writer() and get a writer object
        writer_object = writer(f_object)
        # Pass the list as an argument into the writerow()
        writer_object.writerow(List)
        # Close the file object
        f_object.close()



# Welcome Menu:
def menu():
    print("************ Welcome to Gelos Software Design Website **************")
    print()

    choice = input("""
                      A: Reset your password
                      B: Change your secret question + anwser
                      Q: Logout

                      Please enter your choice: """)

    if choice == "A" or choice =="a":
        reset_pw()
    elif choice == "B" or choice =="b":
        secret_QandA()
    elif choice=="Q" or choice=="q":
        exit()
    else:
        print("You must only select either A or B")
        print("Please try again")
        menu()



# - - - - - - - - - - - - - - - the code - - - - - - - - - - - - - - -
# 1. Login: is the user registered (Y(1) or N(1))
while(valid == False):
    choice1 = input('Are you a Registered User ("y" or "n")')
    if choice1 == "y" or choice1 == "Y":
        valid = True
        while True:
            username = input("Please provide your username: ")
            if username == username in data:
                break
            else:
                print("That username does not exist. Please try again")
                continue

        while True:
            for x in range(1, 4):
                enterTotalTimes = 3
                triesLeftTimes = enterTotalTimes - x
                password = questionary.password("Please provide your password: ",).ask()
                if password == data[username][0]:
                    menu()

                if triesLeftTimes == 0:
                    input_anwser = input("Please enter the answer to your security question: ")
                    with open(users_csv_file, 'r') as file:
                        # Create a CSV reader
                        csv_reader = csv.reader(file)
                        # Skip the header row
                        header = next(csv_reader)
                        # Read the data row
                        data_row = next(csv_reader)
                        # Extract the SecretQuestionAnswer value and convert it to a Python dictionary
                        secret_question_answer_str = data_row[4]
                        secret_question_answer_dict = ast.literal_eval(secret_question_answer_str)
                        # Extract the value
                        stored_answer = secret_question_answer_dict.pop()
                        print(stored_answer)
                        if(input_anwser == stored_answer):  
                            reset_pw()  
                        else:
                            print("Incorrect Answer! Try again later.")
                else:    
                    print("Incorrect password. You have " + str(triesLeftTimes) + " attempts left.")

    # 2. User is not registered:
    elif choice1 == "n" or choice1 == "N":
        # 3. Does User wish to SignUp (Y(2) or N(2)):
        while True:
            choice2 = input('Do you wish to Sign Up ("y" or "n")')
            if choice2 == "y" or choice2 == "Y":
                while(valid == False):
                    username = input("Please provide your username: ")
                    if username == username in data:
                        valid = False
                        print("That username is taken. Please try again.")
                        continue
                    else:
                        valid = True
                        break

                # 4. Does the User have their own password, or wants the System to generate one for them (Y(3) or N(3)):
                while True:
                    choice3 = input('Would you like the system to generate a password for you ("y" or "n")')
                    # User would like to enter their own password:
                    if choice3 == "y" or choice3 == "Y":

                        try:
                            # 5. User wants System to generate a password for them:
                            length = int(input("Enter your new password length: "))
                            if length < min_pw_len:
                                valid = False
                                print(myDict[1])
                                continue
                            elif length >= min_pw_len:
                                valid = True
                                lower = string.ascii_lowercase
                                upper = string.ascii_uppercase
                                num = string.digits
                                symbols = string.punctuation
                                all  = lower + upper + num + symbols
                                temp =  random.sample(all, length)
                                password = ''.join(temp)
                                break
                        except ValueError:
                            print("Amount must be a number")
                            continue

                    # User wants to use their own password:
                    elif choice3 == "n" or choice3 == "N":
                         # § use fn "password_validator()" from the "Validator" class
                        password = questionary.password(myDict[5], validate=password_validator).ask()
                        break

                    else:
                        print("Not a valid response")

                # 5. Input Firstname, Input Lastname. Then write to CSV file:
                firstname = input("Please enter your First name: ")
                lastname = input("Please enter your last name: ")
                if __name__ == "__main__":
                    action1 = (
                        questionary.select(
                            "Select a security question: ",
                            choices=[myDict[20],myDict[21],myDict[22],myDict[23],myDict[24],myDict[25]],
                        ).ask()
                        or myDict[13]
                    ),
                    action2 = (
                        questionary.password("Type your answer: ").ask()
                            )
                security_question = {action1, action2}

                List = [username, password, firstname, lastname, security_question]
                write_to_file_all()
                menu()

            # User doesn't want to SignUp (GoodBye)
            elif choice2 == "n" or choice2 == "N":
                print("Goodbye!")
                exit()
    else:
        valid = False
        print('This is not an option, please try again.')
        continue
