"""
Write a program that stores user's emails (unique keys) and
names (values) in a dictionary.
Ask the user for their email until they enter a blank one.
Use a separate function to get the name from the email. You
should find the following methods useful: split, join, title.
Notice the prompt to check if the name is correct: Y/n.
"""
email_to_name = {}
email = input("Email: ")
while email != "":
    name = email.split('@')[0]
    name = name.split('.')
    name = " ".join(name).title()
    confirmation = input("Is your name {}? (Y/n) ".format(name))
    if confirmation.upper() != "Y" and confirmation != "":
        name = input("Name: ")
    email_to_name[email] = name
    email = input("Email: ")

for email, name in email_to_name.items():
    print("{} ({})".format(name, email))

