"""
More scores
"""

import random


def main():
    """Get a number of scores and write results to output file."""
    number_of_scores = int(input("Enter a number of scores: "))
    output_file = open("results.txt", "w")
    for score in range(number_of_scores):
        score = generate_random_scores(score)
        result = determine_status(score)
        print("{} is {}".format(score, result), file=output_file)
    output_file.close()


def generate_random_scores(score):
    """Generate random scores."""
    return int(random.randint(0, 100))


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
