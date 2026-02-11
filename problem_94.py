#Password Validator: Write a Python program that takes a password as input and checks if it meets the following criteria: at least 8 characters long, contains both uppercase and lowercase letters, and has at least one digit. If the password is valid, print “Password accepted.” If not, use `continue` to prompt the user to enter a valid password.
while True:
    password = input("Enter password: ")

    # Check length
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
        continue

    # Check uppercase
    if not any(char.isupper() for char in password):
        print("Password must contain at least one uppercase letter.")
        continue

    # Check lowercase
    if not any(char.islower() for char in password):
        print("Password must contain at least one lowercase letter.")
        continue

    # Check digit
    if not any(char.isdigit() for char in password):
        print("Password must contain at least one digit.")
        continue

    print("Password accepted.")
    break
