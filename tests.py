import unittest
import string
from main import encrypt, random_number


class TestEncryption(unittest.TestCase):
    def setUp(self):
        self.my_message = "Tony Stark is a superhero! 92"

    def test_inputExists(self):
        self.assertIsNotNone(self.my_message)

    def test_inputType(self):
        self.assertIsInstance(self.my_message,str)

    def test_functionReturnsEncryptedMessage(self):
        self.assertIsNotNone(encrypt(self.my_message))

    def test_lenInputOutput(self):
        self.assertEqual(len(self.my_message), len(encrypt(self.my_message)))

    def test_differentInputOutput(self):
        self.assertNotEqual(self.my_message, encrypt(self.my_message))

    def test_outputType(self):
        self.assertIsInstance(encrypt(self.my_message), str)
        
    def test_shiftedCypher(self):
        abc = string.ascii_letters + string.punctuation + string.digits + " "
        encrypted_message = "".join([abc[abc.find(char) + random_number] if len(abc) > (abc.find(char) + random_number) else abc[0] for index, char in enumerate(self.my_message)])
        print(f"{encrypted_message} ----Random: {random_number}----")
        self.assertEqual(encrypted_message, encrypt(self.my_message))
        
        

if __name__ == "__main__":
    unittest.main()