import random
import string

def generate_password(length=12, use_digits=True, use_special=True):
    characters = string.ascii_letters  # Includes both lowercase and uppercase

    if use_digits:
        characters += string.digits  # Adds numbers (0-9)
    
    if use_special:
        characters += string.punctuation  # Adds special characters (!@#$%^&*)

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

length = int(input("Enter password length: "))
use_digits = input("Include numbers? (y/n): ").lower() == 'y'
use_special = input("Include special characters? (y/n): ").lower() == 'y'

password = generate_password(length, use_digits, use_special)
print(f"Generated Password: {password}")

a=input()