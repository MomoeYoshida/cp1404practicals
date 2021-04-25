"""
CP1404 Practical
UnreliableCar class that inherits from the Car class
"""
from random import randint
from prac_08.car import Car


class UnreliableCar(Car):
    """Specialised version of a Car."""

    def __init__(self, name, fuel, reliability):
        """Initialise a UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)  # Call the Car's version of __init__
        self.reliability = reliability

    def __str__(self):
        """Return a string like a Car but with car's reliability."""
        return "{}, reliability={:.2f}".format(super().__str__(), self.reliability)

    def drive(self, distance):
        """Drive the car if a random number (0-100) is less than reliability."""
        random_number = randint(0, 100)
        if random_number < self.reliability:
            distance_driven = super().drive(distance)
            return distance_driven
        else:
            return 0

