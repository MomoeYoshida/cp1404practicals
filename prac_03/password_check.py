"""
Modify the program below to use functions.
Write a program that asks the user for a password, with
error-checking to repeat if the password doesn't meet a
minimum length set by a variable. The program should then
print asterisks (*) as long as the word.
"""

MINIMUM_LENGTH = 6


def main():
    """Get and print password using functions."""
    password = get_password(MINIMUM_LENGTH)
    print_asterisks(password)


def get_password(minimum_length):
    """Get password (ensuring it meets the minimum_length requirement)."""
    password = input("Enter password of at least {} characters: ".format(minimum_length))
    while len(password) < minimum_length:
        print("Error - at least {} characters".format(minimum_length))
        password = input("Enter password of at least {} characters: ".format(minimum_length))
    return password


def print_asterisks(sequence):
    """Print asterisks (*) as long as the characters."""
    print('*' * len(sequence))


main()
