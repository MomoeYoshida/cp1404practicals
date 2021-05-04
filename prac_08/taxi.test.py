"""
CP1404 Practical - Client code to test the Taxi class.
"""
from prac_08.taxi import Taxi


def main():
    """Demo test code to test the Taxi class."""
    # 1. Create a new taxi with name "Prius 1", 100 units of fuel and price of $1.23/km
    prius_1 = Taxi("Prius 1", 100, 1.23)
    # 2. Drive the taxi 40km
    prius_1.drive(40)
    # 3. Print the taxi's details and the current fare
    print(prius_1)
    # 4. Restart the meter (start a new fare) and then drive the car 100km
    prius_1.start_fare()
    prius_1.drive(100)
    # 5. Print the details and the current fare
    print(prius_1)


main()
