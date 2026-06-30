import string
from collections import Counter
import random

option = input(str("Enter 1 for password strength checker and 2 for password generator: "))

characters = string.ascii_letters + string.digits + string.punctuation
char_dict = dict.fromkeys(characters, 0)

def strength_checker():
    password = input(str("Enter your password: "))
    upper = any(c.isupper() for c in password)
    lower = any(c.islower() for c in password)
    digit = any(c.isdigit() for c in password)
    special = any(c in string.punctuation for c in password)
    length = len(password) >= 10
    repetition = all(count <= 2 for count in Counter(password).values())
    strong = (upper and lower and digit and special and length and repetition)
    
    print(strong)

def generator():
    pass

if option == "1":
    strength_checker()
elif option == "2":
    generator()
else:
    print("Please enter 1 or 2")


