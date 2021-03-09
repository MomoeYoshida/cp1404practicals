"""
Write a program that asks the user for a password, with
error-checking to repeat if the password doesn't meet a
minimum length set by a variable. The program should then
print asterisks (*) as long as the word.
"""

MINIMUM_LENGTH = 6


def get_password():
    """Get a password of valid length and print asterisks."""
    password = input("Enter password of at least {} characters: ".format(MINIMUM_LENGTH))
    while len(password) < MINIMUM_LENGTH:
        password = input("Enter password of at least {} characters: ".format(MINIMUM_LENGTH))

    print('*' * len(password))
