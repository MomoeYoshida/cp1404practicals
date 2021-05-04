"""
CP1404/CP5632 Practical
File and class example - opens/reads a file, stores in objects of custom class
(contains multiple versions for demonstration: using csv and namedtuple)
"""

import csv
from collections import namedtuple

from prac_08.programming_language import ProgrammingLanguage


def main():
    """Read file of programming language details, save as objects, display."""
    languages = []
    # open the file for reading
    in_file = open('languages.csv', 'r')

    # file format is like: Language,Typing,Reflection,Year
    # 'consume' the first line (header) - we don't need its contents
    in_file.readline()

    # all other lines are language data
    for line in in_file:  # read the rest of the file
        # print(repr(line))  # debugging

        # strip newline from end and split it into parts (CSV)
        parts = line.strip().split(',')
        # print(parts)  # debugging

        # reflection is stored as a string (Yes/No) and we want a Boolean. reflection is stored in the file as a
        # string, but this client code converts it to a Boolean ready for the class.
        reflection = parts[2] == "Yes"
        pointer_arithmetic = parts[3] == "Yes"

        # construct a ProgrammingLanguage object using the elements
        # year should be an int
        language = ProgrammingLanguage(parts[0], parts[1], reflection, pointer_arithmetic,
                                       int(parts[4]))

        # add the language we've just constructed to the list
        languages.append(language)

    # close the file as soon as we've finished reading it
    in_file.close()

    # loop through and display all languages (using their str method)
    for language in languages:
        print(language)


main()