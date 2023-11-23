import random
import string

def generate_password(length):
    # Define character sets for password complexity
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine character sets based on user preferences
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Ensure the password length is at least 8 characters
    length = max(length, 8)

    # Generate the password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

def password_generator():
    try:
        # Prompt user for password length
        length = int(input("Enter the desired length of the password: "))
        
        # Generate and display the password
        password = generate_password(length)
        print(f"Generated Password: {password}")

    except ValueError:
        print("Invalid input. Please enter a valid integer for the password length.")

if __name__ == "__main__":
    password_generator()
