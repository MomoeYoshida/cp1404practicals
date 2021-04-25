"""
CP1404 Practical
Taxi class extends the Car class
"""
from prac_08.car import Car


class Taxi(Car):
    """Specialised version of a Car that includes fare costs."""

    def __init__(self, name, fuel, price_per_km):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)  # Override methods to take account of the characteristics of a Taxi
        self.price_per_km = price_per_km  # Add new attributes
        self.current_fare_distance = 0

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return "{}, {}km on current fare, ${:.2f}/km".format(super().__str__(),
                                                             self.current_fare_distance,
                                                             self.price_per_km)

    def get_fare(self):  # Add new methods
        """Return the price for the taxi trip."""
        return self.price_per_km * self.current_fare_distance

    def start_fare(self):
        """Begin a new fare."""
        self.current_fare_distance = 0

    def drive(self, distance):  # polymorphism
        """Drive like parent Car but calculate fare distance as well."""
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven