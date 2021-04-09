"""CP1404 Practical - a Guitar class."""
# Get the current year from the system clock by using "datetime" module.
from datetime import date

CURRENT_YEAR = date.today().year
VINTAGE_AGE = 50


class Guitar:
    """Represent fields/attributes of a Guitar."""
    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of Guitar fields."""
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Get the guitar age based on the CURRENT_YEAR."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if the guitar is vintage or not based on age."""
        return self.get_age() >= VINTAGE_AGE

