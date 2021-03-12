"""
Capitalist Conrad wants a stock price simulator for a volatile stock.
The price starts off at $10.00, and, at the end of every day there is
a 50% chance it increases by 0 to 10%, and
a 50% chance that it decreases by 0 to 5%.
If the price rises above $1000, or falls below $0.01, the program should end.
The price should be displayed to the nearest cent (e.g. $33.59, not $33.5918232901)
"""
# 1.
import random

MAX_INCREASE = 0.1  # 10%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 0.01
MAX_PRICE = 1000.0
INITIAL_PRICE = 10.0

price = INITIAL_PRICE
day = 0
print("Starting price: ${:,.2f}".format(price))

while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0
    day += 1
    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    print("On day {} price is: ${:,.2f}".format(day, price))

# 2. Try changing CONSTANTS so the allowed price range is $1 to $100 and the increase could be up to 17.5%.
import random

MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1
MAX_PRICE = 100
INITIAL_PRICE = 10.0

price = INITIAL_PRICE
day = 0
print("Starting price: ${:,.2f}".format(price))

while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0
    day += 1
    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    print("On day {} price is: ${:,.2f}".format(day, price))

# 3. Update your program (1.) so that it prints (writes) the output to a file.
import random
# using the same CONSTANTS as program 1
MAX_INCREASE = 0.1  # 10%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 0.01
MAX_PRICE = 1000.0
INITIAL_PRICE = 10.0
OUTPUT_FILE = "output.txt"

out_file = open(OUTPUT_FILE, "w")

price = INITIAL_PRICE
day = 0
print("Starting price: ${:,.2f}".format(price))

while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0
    day += 1
    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    print("On day {} price is: ${:,.2f}".format(day, price), file=out_file)

out_file.close()
