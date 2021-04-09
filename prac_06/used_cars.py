"""CP1404 Practical - Client code to use the Car class."""

from prac_06.car import Car


def main():
    """Demo test code to show how to use the Car class."""
    # 7. Add names (literals) to the constructors where you create Car objects.
    my_car = Car("My car", 180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)  # fuel = 150 (output)
    print("odo =", my_car.odometer)  # odo = 30 (output)
    print(my_car)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))

    # 1. Create a new Car object called "limo" that is initialised with 100 units of fuel.
    limo = Car("Limo", 100)
    # 2. Add 20 more units of fuel to this new car object using the add method.
    limo.add_fuel(20)
    # 3. Print the amount of fuel in the car.
    print(limo.fuel)
    # 4. Attempt to drive the car 115km using the drive method.
    limo.drive(115)
    # 5. Print the car's odometer reading.
    print(limo.odometer)


main()
