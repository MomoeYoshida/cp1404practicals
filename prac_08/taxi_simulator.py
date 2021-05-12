"""
CP1404 Practical
Taxi Simulator Program that uses the Taxi and SilverServiceTaxi classes
"""
from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi
MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Write a Taxi Simulator Program that uses the Taxi and SilverServiceTaxi classes."""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    bill_to_date = 0
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available:")
            display_taxis(taxis)
            chosen_taxi_number = int(input("Choose taxi: "))
            taxi_chosen = taxis[chosen_taxi_number]
        elif choice == "d":
            taxi_chosen.start_fare()
            distance_to_drive = int(input("Drive how far? "))
            taxi_chosen.drive(distance_to_drive)
            trip_cost = taxi_chosen.get_fare()
            print("Your {} trip cost you ${:.2f}".format(taxi_chosen.name, trip_cost))
            bill_to_date += trip_cost
        else:
            print("Invalid option")
        print("Bill to date: ${:.2f}".format(bill_to_date))
        print(MENU)
        choice = input(">>> ").lower()
    print("Total trip cost: ${:.2f}".format(bill_to_date))
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display available taxis."""
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


main()
