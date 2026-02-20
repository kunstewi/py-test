"""
We’ll generate a strong password using:

string.ascii_letters

string.digits

string.punctuation

random module
"""

# basic random password
import string
import random

def generate_password(length=12):
    # All possible characters
    characters = string.ascii_letters + string.digits + string.punctuation
    
    password = ""
    
    for _ in range(length):
        password += random.choice(characters)
    
    return password


# Example
print(generate_password(12))

"""
string.ascii_letters → a-z + A-Z

string.digits → 0-9

string.punctuation → special symbols

random.choice() → picks one random character
"""

# pythonic version
import string
import random

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(characters) for _ in range(length))


print(generate_password(16))


# stronger version all character types included
import string
import random

def generate_strong_password(length=12):
    if length < 4:
        raise ValueError("Password length must be at least 4")

    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    characters = string.ascii_letters + string.digits + string.punctuation

    password += random.choices(characters, k=length - 4)

    random.shuffle(password)

    return "".join(password)


print(generate_strong_password(12))

"""
import secrets
secrets.choice()

in production use secrets because random isn't cryptographically secure
"""