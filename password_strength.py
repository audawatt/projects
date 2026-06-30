import string
from collections import Counter
import random

def strength_checker():
    password = input(str("Enter your password: "))

    upper = any(c.isupper() for c in password)
    lower = any(c.islower() for c in password)
    digit = any(c.isdigit() for c in password)
    special = any(c in string.punctuation for c in password)
    length = len(password) >= 10
    repetition = all(count <= 2 for count in Counter(password).values())

    strong = (upper and lower and digit and special and length and repetition)

    return strong

def generator():
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digit = string.digits 
    special = string.punctuation

    password = (random.choices(upper, k=2) + random.choices(lower, k=4) + random.choices(digit, k=2) + random.choices(special, k=2))

    random.shuffle(password)

    return ''.join(password)
    
while True:
    option = input("Enter 1 for password strength checker, 2 for password generator, and 3 to quit: ")

    if option == "1":
        print(strength_checker())
    elif option == "2":
        print(generator())
    elif option == "3":
        break
    else:
        print("Please enter 1, 2, or 3.")


