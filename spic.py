import re

def check_password_strength(password):
    # Minimum length of the password
    min_length = 8

    # Regular expressions for checking various conditions
    contains_uppercase = re.compile(r'[A-Z]')
    contains_lowercase = re.compile(r'[a-z]')
    contains_digit = re.compile(r'\d')
    contains_special_char = re.compile(r'[!@#$%^&*()_+{}[\]:;<>,.?~\\/-]')

    # Check minimum length
    if len(password) < min_length:
        return "Weak (Minimum length should be {})".format(min_length)

    # Check for uppercase letters
    if not contains_uppercase.search(password):
        return "Weak (Should contain at least one uppercase letter)"

    # Check for lowercase letters
    if not contains_lowercase.search(password):
        return "Weak (Should contain at least one lowercase letter)"

    # Check for digits
    if not contains_digit.search(password):
        return "Weak (Should contain at least one digit)"

    # Check for special characters
    if not contains_special_char.search(password):
        return "Weak (Should contain at least one special character)"

    # If all conditions are met, the password is strong
    return "Strong"

if __name__ == "__main__":
    user_password = input("Enter your password: ")
    strength_result = check_password_strength(user_password)
    print("Password Strength: {}".format(strength_result))
