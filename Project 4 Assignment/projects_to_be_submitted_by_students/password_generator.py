# Project 7: Password Generator Python Project

# 🔐 Project 7: Password Generator Python Project

import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("🔒 Welcome to the Password Generator!")
try:
    length = int(input("🧮 Enter the length of your desired password: "))
    password = generate_password(length)
    print("✅ Your generated password is:", password)
    print("🔑 Keep it safe and secure!")
except ValueError:
    print("⚠️ Please enter a valid number for password length.")

