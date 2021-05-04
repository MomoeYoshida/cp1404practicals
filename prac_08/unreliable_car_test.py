"""
CP1404 Practical - Client code to verify each method in the UnreliableCar class.
"""
from prac_08.unreliable_car import UnreliableCar


def main():
    """Demo test code to test the UnreliableCar class."""
    high_reliability_car = UnreliableCar("Good Car", 100, 96.9)
    low_reliability_car = UnreliableCar("Bad Car", 100, 8.5)
    print("Initial state:", high_reliability_car)
    print("Initial state:", low_reliability_car)
    for i in range(1, 15):
        print("{:8} drove {:2}km.".format(high_reliability_car.name, high_reliability_car.drive(i)))
        print("{:8} drove {:2}km.".format(low_reliability_car.name, low_reliability_car.drive(i)))
    print("Final state:", high_reliability_car)
    print("Final state:", low_reliability_car)


main()
