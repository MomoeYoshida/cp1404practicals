"""
Write a program that prompts the user for 5 numbers and
then stores each of these in a list called numbers.
The program should then output various interesting things.
Note that you can use the functions min, max, sum and len,
and you can use the append method to add a number to a list.
"""
# 1. Basic list operations
numbers = []
for i in range(5):
    number = int(input("Number: "))
    numbers.append(number)
print("The first number is {}".format(numbers[0]))
print("The last number is {}".format(numbers[4]))
print("The smallest number is {}".format(min(numbers)))
print("The largest number is {}".format(max(numbers)))
print("The average of the numbers is {}".format(sum(numbers) / len(numbers)))

# 2. Woefully inadequate security checker
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = str(input("Enter username: "))
if username in usernames:
    print("Access granted")
else:
    print("Access denied")
