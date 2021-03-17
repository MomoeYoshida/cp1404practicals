"""
Write a program that asks the user how many "quick picks"
they wish to generate. The program then generates that many
lines of output. Each line consists of 6 random numbers
between 1 and 45. These values should be stored as CONSTANTS.
"""
import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    """Get the number of quick picks and generate that many lines of output."""
    number_of_quick_picks = int(input("How many quick picks? "))
    while number_of_quick_picks < 0:
        print("Invalid number!")
        number_of_quick_picks =int(input("How many quick picks? "))

    for i in range(number_of_quick_picks):
        quick_pick = []
        for j in range(NUMBERS_PER_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            # Each line (quick pick) should not contain any repeated number
            while number in quick_pick:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_pick.append(number)
        # Each line of numbers should be displayed in sorted order
        quick_pick.sort()
        output = ' '.join('{:2}'.format(number) for number in quick_pick)
        print(output)


main()
