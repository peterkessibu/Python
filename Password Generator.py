import random


def generate_password(length):
    num = "1234567890"
    u_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    l_case = "abcdefghijklmnopqrstuvwxyz"
    symbols = "%@\/#+=-&"
    characters = num + u_case + l_case + symbols
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def save_to_file(email, password, filename="passwords.txt"):
    with open(filename, "a") as file:
        file.write(f"Email: {email}, Password: {password}\n")

def passwdManager():
    try:
        password_length = int(input("Enter password length: "))
        if password_length <= 0:
            print("Password length should be a positive number. Setting to default length of 24.")
            password_length = 24
    except ValueError:
        print("Invalid input. Setting to default length of 24.")
        password_length = 24

    email = input("Enter your email: ")
    if '@' not in email and '.' not in email:
        print("Invalid email format. Please enter a valid email.")
        return
    
    password = generate_password(password_length)
    print(f"Generated Password: {password}")
    print(f"Email: {email}")
    
    save_to_file(email, password)
    print(f"Password and email have been saved to passwords.txt")
passwdManager()
