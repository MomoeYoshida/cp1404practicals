"""CP1404 Practical - This program should use a list to store all of the
user's guitars (keep inputting until they enter a blank name), then print
their details."""

from prac_06.guitar import Guitar


def main():
    """Store all guitars and print their details."""
    guitars = []
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(guitar_to_add, "added.")
        name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 1635.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.90))

    print("There are my guitars:")
    for i, guitar in enumerate(guitars, 1):  # i starts at 1 instead of 0
        vintage_string = ""
        if guitar.is_vintage():
            vintage_string = "(vintage)"
        print("Guitar {0}: {1.name} ({1.year}), worth $ {1.cost} {2}".format(i, guitar, vintage_string))


main()
