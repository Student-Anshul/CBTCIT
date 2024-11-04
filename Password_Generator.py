import random
import string

def generate_password(length, include_uppercase=True, include_numbers=True, include_special=True):
    
    char_set = string.ascii_lowercase
    
    if include_uppercase:
        char_set += string.ascii_uppercase
    if include_numbers:
        char_set += string.digits
    if include_special:
        char_set += string.punctuation

    password = []
    if include_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if include_numbers:
        password.append(random.choice(string.digits))
    if include_special:
        password.append(random.choice(string.punctuation))

    password += random.choices(char_set, k=length - len(password))
    
    random.shuffle(password)

    return ''.join(password)

def main():
    print("Welcome to the Password Generator!")

    try:
        length = int(input("Enter the password length (minimum 6): "))
        if length < 6:
            raise ValueError("Password length should be at least 6 characters.")

        include_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
        include_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
        include_special = input("Include special characters? (yes/no): ").lower() == 'yes'
    
        password = generate_password(length, include_uppercase, include_numbers, include_special)
        print(f"Generated password: {password}")
    
    except ValueError as e:
        print(f"Error: {e}")

main()