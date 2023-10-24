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

# used to hide password and secret question answer:
import questionary
import re
import webbrowser


# - - - - - - - -  - - - - global variables: - - - - - - - - - - - - -
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
    19: "Password must contain a number"
}
valid = False

# - - - - - - - - - - - - - -  classes:  - - - - - - - - - - - - - - -


# - - - - - - - - - - - - - - functions: - - - - - - - - - - - - - - -
# password_validator:
def password_validator(password):
    if not re.search(r'[@#$%^&+=]', password):
        return myDict[17]
    elif not re.search(r'[A-Z]', password):
        return myDict[18]
    elif not re.search(r'[0-9]', password):
        return myDict[19]
    elif len(password) < min_pw_len:
        return myDict[1]
    else:
        return True

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
                password = questionary.password(myDict[5]).ask()
                
                if password == data[username][0]:
                    # Welcome to Gelos Software Design Website
                    print(myDict[0] + username + myDict[6])
                    webbrowser.open('https://georgehowell.art/gelos_python_demo/')
                    exit()
                if triesLeftTimes == 0:
                    new_password = questionary.password("You need to reset your password. Enter a new one now: ", validate=password_validator).ask() # § use fn "password_validator()" from the "Validator" class

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
                    exit()
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
                        password = questionary.password(myDict[5], validate=password_validator).ask() # § use fn "password_validator()" from the "Validator" class
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
                            choices=[
                                "In what city were you born?",
                                "What is the name of your favorite pet?",
                                "What is your mother's maiden name?",
                                "What high school did you attend?",
                                "What was the name of your favourite teacher?",
                                "What was the make and model of your first car?",
                                ],
                        ).ask()
                        or myDict[13]
                    ),
                    action2 = (
                        questionary.password("Type your answer: ").ask()
                )
                security_question = {action1, action2}


                List = [username, password, firstname, lastname, security_question]
                # Open our existing CSV file in append mode
                # Create a file object for this file
                with open(users_csv_file, 'a') as f_object:
               
                    # Pass this file object to csv.writer() and get a writer object
                    writer_object = writer(f_object)
               
                    # Pass the list as an argument into the writerow()
                    writer_object.writerow(List)
               
                    # Close the file object
                    f_object.close()
                # Welcome to Gelos Software Design Website
                print(myDict[0] + firstname + myDict[6])
                webbrowser.open('https://georgehowell.art/gelos_python_demo/')
                exit()

            # User doesn't want to SignUp (GoodBye)
            elif choice2 == "n" or choice2 == "N":
                print("Goodbye!")
                exit()
    else:
        valid = False
        print('This is not an option, please try again.')
        continue
