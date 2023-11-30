# Import the necessary modules for testing:
import unittest
import string

def generatePassword(password):
    abc = string.ascii_letters + string.punctuation + string.digits + " "
    generated_password = "".join([abc[abc.find(char) + 1] if len(abc) > (abc.find(char) + 1) else abc[0] for idx, char in enumerate(password)])
    print(generated_password)
    # return 0
    return generated_password

class TestRandomPassword(unittest.TestCase):
    def setUp(self) -> None:
        self.my_password = "Password9"

    # tests as follows:
    def test_inputExists(self):
        self.assertIsNotNone(self.my_password)
 
    def test_inputTypes(self):
        self.assertIsInstance(self.my_password, str)
        
    def test_functionReturnSomething(self):
        self.assertIsNotNone(generatePassword(self.my_password))
        
    def test_lenIsIdentical(self):
        self.assertEqual(len(self.my_password), len(generatePassword(self.my_password)))
        
    def test_differentIO(self):
        self.assertNotIn(self.my_password, generatePassword(self.my_password))
        
    def test_outputTypes(self):
        self.assertIsInstance(generatePassword(self.my_password), str)

if __name__ == "__main__":
    unittest.main()