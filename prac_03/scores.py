"""
Ask the user for a number of scores
Generate that many random numbers (scores) between 0 and 100 inclusive
For each of those scores, write the "result" to a file called results.txt
"""

import random


def main():
    """Get a number of scores"""
    number_of_scores = int(input("Enter a number of scores: "))
    create_input_file(number_of_scores)
    input_file = open("results.txt", "w")
    input_file.close()


def create_input_file(quantity):
    """Write number (quantity) of scores to file."""
    scores_file = open("results.txt", "w")
    for i in range(quantity):
        score = random.randint(0, 100)
        print("{} is {}".format(score, status), file=scores_file)
    scores_file.close()


# def main():
#     """Get a score and print its status."""
#     score = float(input("Enter score: "))
#     print(determine_status(score))
#     output_file = open("results.txt", "w")
#     for result in results:
#
#
#
# def determine_status(score):
#     """Determine the status of a given score."""
#     if score < 0 or score > 100:
#         return "Invalid score"
#     elif score >= 90:
#         return "Excellent"
#     elif score >= 50:
#         return "Passable"
#     else:
#         return "Bad"


main()
