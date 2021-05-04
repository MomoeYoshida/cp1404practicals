"""
CP1404 Practical - Client code to see the SilverServiceTaxi class calculates
fares correctly.
"""
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    """Demo test code to test the SilverServiceTaxi class."""
    # 4. E.g. for a Hummer with a fanciness of 4
    hummer = SilverServiceTaxi("Hummer", 200, 4)
    print(hummer)
    # 5. See SilverServiceTaxi class calculates fares correctly
    taxi = SilverServiceTaxi("Taxi", 100, 2)
    taxi.drive(18)
    print(taxi)
    print("For an {}km trip with fanciness of {}, the fare = ${:.2f}".format(taxi.current_fare_distance, taxi.fanciness, taxi.get_fare()))


main()
