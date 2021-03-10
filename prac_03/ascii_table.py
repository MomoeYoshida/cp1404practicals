"""
ASCII table
"""

LOWER = 33
UPPER = 127

char = input("Enter a character: ")
print("The ASCII code for {} is {}".format(char, ord(char)))  # ord() to convert characters to ASCII integer values
number = int(input("Enter a number between {} and {}: ".format(LOWER, UPPER)))
while not LOWER <= number <= UPPER:
    number = int(input("Enter a number between {} and {}: ".format(LOWER, UPPER)))
print("The character for {} is {}".format(number, chr(number))) # chr() to convert ASCII integer values to characters

# 3. Add on to this program by writing code that displays a table with two columns, one for the numeric ASCII value and
# the other for the character itself. Use the string format() method to align the text nicely in two columns.
# Print the values between LOWER and UPPER.
for value in range(LOWER, UPPER + 1):
    print("{:3} {:>3}".format(value, chr(value)))

"""
Extension
"""
# ASCII Columns Challenge
# Ask the user for how many columns to print.
MAX_COLUMNS = 8
MIN_COLUMNS = 2

columns = int(input("Enter number of columns: "))
while not MIN_COLUMNS <= columns <= MAX_COLUMNS:
    print("Please use a value between {} and {}".format(MIN_COLUMNS, MAX_COLUMNS))
    columns = int(input("Enter number of columns: "))

number_of_values = UPPER - LOWER + 1
rows = number_of_values // columns  # floor division (//) is a normal division operation
# except that it returns the largest possible integer, which is <= the normal division result.

print("Version 1: Horizontal then vertical ordering")
value = LOWER
for row in range(rows):
    for column in range(columns):
        print("{:6} {:>2}".format(value, chr(value)), end="")
        value += 1
    print()

# last row is special as it may not have all columns
# start where we left off and only print up to UPPER
starting_value = value
for value in range(starting_value, UPPER + 1):
    print("{:6} {:>2}".format(value, chr(value)), end="")
print("\n")
