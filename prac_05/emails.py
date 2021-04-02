"""
Write a program that stores user's emails (unique keys) and
names (values) in a dictionary.
Ask the user for their email until they enter a blank one.
Use a separate function to get the name from the email. You
should find the following methods useful: split, join, title.
Notice the prompt to check if the name is correct: Y/n.
"""


def main():
    """Store user's emails and names in a dictionary."""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        confirmation = input("Is your name {}? (Y/n) ".format(name))
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print("{} ({})".format(name, email))


def get_name_from_email(email):
    """Get expected name from email."""
    name = email.split('@')[0]
    name = name.split('.')
    name = " ".join(name).title()
    return name


main()
