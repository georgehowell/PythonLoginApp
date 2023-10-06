import pytest

from classes.validator import Validator

class TestValidator():

    def setUp(self):
        self.validator = Validator()
    
    def test_will_reject_username_if_too_long(self):
        # Assume
        username = 'InvalidTooLong'
        
        # Action
        result = self.validator.username_is_valid(username)
        
        # Assert
        self.assertFalse(result)
        
        
        
    def test_will_reject_username_has_whitespace(self):
        # Assume
        username = 'Invalid Space'
        
        # Action
        result = self.validator.username_is_valid(username)
        
        # Assert
        self.assertFalse(result)
        
        

    def test_will_reject_username_has_no_uppercase(self):
        # Assume
        username = 'invalid'
        
        # Action
        result = self.validator.username_is_valid(username)
        
        # Assert
        self.assertFalse(result)
        
    

    def test_will_accept_username_valid(self):
        # Assume
        username = 'ValidUser'
        
        # Action
        result = self.validator.username_is_valid(username)
        
        # Assert
        self.assertFalse(result)
