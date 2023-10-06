from classes.validator import Validator

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

username = 'Reval'
validator = Validator()

if validator.username_is_valid(username):
    print('Username is valid')
    
else:
    print('Username is invalid')
    
    
    
def password_validator(password):
    if len(password) < min_pw_len:
        return myDict[1]
    else:
        return True

    
    

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
