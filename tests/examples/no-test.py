from classes.validator import Validator

class TestValidator():

    def valid_username(username):
        if not username.isalpha():
            reason = 'Username can only contain alpha characters'
            return reason

        if not any(x.isupper() for x in username):
            reason = 'Username must contain at least one uppercase character'
            return reason

        return "Username is good!"
    
    def valid_username_using_exceptions(foo):
        if not foo.isalpha():
            raise ValueError('Username can only contain alpha characters')
        return True


    failing_username = 'this_will_raise_an_exception_***'
    try:
        if valid_username_using_exceptions(failing_username):
            print('All good')
    except ValueError:
        print("Failed!")

    print(valid_username('FrankWorks'))
    print(valid_username('frankfails'))
