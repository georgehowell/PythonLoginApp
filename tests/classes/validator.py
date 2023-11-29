import re

min_pw_len = 10

class Validator:
    def username_is_valid(self, username):
        if len(username) < 10:
            return False
        
        if ' ' in username:
            return False
        
        if username.isupper():
            return False
         
        return True
    
    def password_validator(self, password):    
        if not re.search(r'[@#$%^&+=]', password):
            return False
        if not re.search(r'[A-Z]', password):
            return False
        if not re.search(r'[0-9]', password):
            return False
        if len(password) < min_pw_len:
            return False
        return True