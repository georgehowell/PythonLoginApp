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
import questionary


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
    16: "Goodbye!"
          }
valid = False

# - - - - - - - - - - - - - -  classes:  - - - - - - - - - - - - - - -


# - - - - - - - - - - - - - - functions: - - - - - - - - - - - - - - -
# password_validator:
def password_validator(password):
    if len(password) < min_pw_len:
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
                                # print(password)  # W O R K S ! ! !
                                break
                        except ValueError:
                            print("Amount must be a number")
                            continue

                    # User wants to use their own password:
                    elif choice3 == "n" or choice3 == "N":
                        password = questionary.password(myDict[5], validate=password_validator).ask() # § use fn "password_validator()"
                        break

                    else:
                        print("Not a valid response")

                # 5. Input Firstname, Input Lastname. Then write to CSV file:
                firstname = input("Please enter your First name: ")
                lastname = input("Please enter your last name: ")

                List = [username, password, firstname, lastname]
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
                exit()

            # User doesn't want to SignUp (GoodBye)
            elif choice2 == "n" or choice2 == "N":
                print("Goodbye!")
                exit()
    else:
        valid = False
        print('This is not an option, please try again.')
        continue
