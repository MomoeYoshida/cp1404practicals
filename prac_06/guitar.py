"""CP1404 Practical - a Guitar class."""


class Guitar:
    """Represent fields/attributes of a Guitar."""
    YEAR = 2021

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of Guitar fields."""
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self, age):
        """Return the guitar age in years."""
        age = Guitar.YEAR - self.year

    def is_vintage(self):
        """Determine if the guitar is 50 or more years old."""
        return self.get_age() >= 50