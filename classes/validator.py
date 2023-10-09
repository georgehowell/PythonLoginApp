class Validator:
    def username_is_valid(self, username):
        if len(username) < 10:
            return False
        
        if ' ' in username:
            return False
        
        if username.islower():
            return False
         
        return True
    
    def password_validator(self, password):
        if len(password) < 10:
            return False
        
        if ' ' in password:
            return False
        
        if password.islower():
            return False
         
        return True