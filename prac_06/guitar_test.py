"""CP1404 Practical - Tests for the Guitar class."""

from prac_06.guitar import Guitar
from datetime import date

CURRENT_YEAR = date.today().year


def run_tests():
    """Test a Guitar class."""
    name = "Gibson L-5 CES"
    year = 1922
    guitar = Guitar(name, year)
    another = Guitar("Another Guitar", 2013)
    # Test that the get_age() method works
    print("{} get_age() - Expected {}. Got {}".format(guitar.name, 99, guitar.get_age()))
    print("{} get_age() - Expected {}. Got {}".format(another.name, 8, another.get_age()))
    # Test that the is_vintage() method works
    print("{} is_vintage() - Expected {}. Got {}".format(guitar.name, True, guitar.is_vintage()))
    print("{} is_vintage() - Expected {}. Got {}".format(another.name, False, guitar.is_vintage()))


if __name__ == '__main__':
    run_tests()
