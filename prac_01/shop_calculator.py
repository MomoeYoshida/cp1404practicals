"""
Shop calculator program to determine total price (discounted)
"""
# 1. the message "Invalid number of items!" will be displayed if the number of items is less than zero
total = 0
number = int(input("Number of items: "))
while number < 0:
    print("Invalid number of items!")
    number = int(input("Number of items: "))
for i in range(number):
    price = float(input("Price of item: "))
    total += price
if total > 100:
    total *= 0.9
print("Total price for {} items is ${:.2f}".format(number, total))

# 2. in addition to 1., the message "Invalid price of items!" will be displayed if the price of items is less than zero
total = 0
number = int(input("Number of items: "))
while number < 0:
    print("Invalid number of items!")
    number = int(input("Number of items: "))
for i in range(number):
    price = float(input("Price of item: "))
    while price < 0:
        print("Invalid price of items!")
        price = float(input("Price of item: "))
    total += price
if total > 100:
    total *= 0.9
print("Total price for {} items is ${:.2f}".format(number, total))