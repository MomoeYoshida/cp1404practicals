"""
Refactor the broken program determining score status in prac_01 to use functions
"""

import random


def main():
    """Get a score and print its status."""
    score = float(input("Enter score: "))
    # score = generate_random_score()
    # print("Random score: {}".format(score))
    print(determine_status(score))


# def generate_random_score():
#     """Generate a random score."""
#     return int(random.randint(0, 100))


def determine_status(score):
    """Determine the status of a given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
