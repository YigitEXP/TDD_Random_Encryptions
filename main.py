import string
import random

random_number = random.randint(0,12)

def encrypt(message):
    
    abc = string.ascii_letters + string.punctuation + string.digits + " "
    encrypted_message = "".join([abc[abc.find(char) + random_number] if len(abc) > (abc.find(char) + random_number) else abc[0] for index, char in enumerate(message)])
    return encrypted_message