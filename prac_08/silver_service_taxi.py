"""
CP1404 Practical
SilverServiceTaxi that inherits from the Taxi class
"""
from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi."""
    flagfall = 4.50  # 2. Add a flagfall class variable set to $4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness  # 1. Add a new attribute
        self.price_per_km = Taxi.price_per_km * self.fanciness

    def __str__(self):  # 4. Add the flagfall to the end
        """Return a string like a Taxi but with flagfall."""
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flagfall)

    def get_fare(self):  # 3. Add/override a method to calculate the fare
        """Calculate the fare."""
        return super().get_fare() + self.flagfall

