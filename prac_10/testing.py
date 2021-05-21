"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    # 1. Fix this function so that it passes the assert test.
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    # 4. Fix the failing is_long_word function.
    return len(word) >= length


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    # assert test with custom message - used to see if Car's init method sets the odometer correctly
    test_car = Car()
    assert test_car.odometer == 0, "Car does not set odometer correctly"

    # 2. Write assert statements to show if Car sets the fuel correctly.
    # Note that Car's __init__ function sets the fuel in one of two ways:
    # using the value passed in or the default
    # You should test both of these
    test_car = Car()
    assert test_car.fuel == 0  # Test the default
    test_car = Car(fuel=10)
    assert test_car.fuel == 10  # Test the value passed in


def format_phrase_to_sentence(phrase):
    # 5. Write and test (using doctest) a function to format a phrase as a sentence,
    # starting with a capital and ending with a single full stop.
    """
    Format a phrase as a sentence - starting with a capital and ending with a single full stop.
    >>> format_phrase_to_sentence('hello')
    'Hello.'
    >>> format_phrase_to_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> format_phrase_to_sentence('see you later')
    'See you later.'
    """
    sentence = phrase.capitalize()
    if sentence[-1] != '.':
        sentence += '.'
    return sentence


run_tests()
# 3. Uncomment the following line and run the doctests
doctest.testmod()
