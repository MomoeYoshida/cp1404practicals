"""
An electricity bill estimator
"""
# 2. Create an electricity bill estimator
print("Electricity bill estimator")
price_per_kWh_in_cents = float(input("Enter cents per kWh: "))
while price_per_kWh_in_cents < 0:
    print("Invalid price!")
    price_per_kWh_in_cents = float(input("Enter cents per kWh: "))
price_per_kWh_in_dollars = price_per_kWh_in_cents * 0.01
daily_use_in_kWh = float(input("Enter daily use in kWh: "))
while daily_use_in_kWh < 0:
    print("Invalid kWh!")
    daily_use_in_kWh = float(input("Enter daily use in kWh: "))
number_of_billing_days = int(input("Enter number of billing days: "))
while number_of_billing_days < 0:
    print("Invalid number of days!")
    number_of_billing_days = int(input("Enter number of billing days: "))
estimated_bill = price_per_kWh_in_dollars * daily_use_in_kWh * number_of_billing_days
print("Estimated bill: $", estimated_bill)


# 3.
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
PRICE_PER_KWH_IN_CENTS = 35
PRICE_PER_KWH_IN_DOLLARS = PRICE_PER_KWH_IN_CENTS * 0.01

print("Electricity bill estimator 2.0")
choice = input("Which tariff? 11 or 31: ")

while choice != "Q":
    if choice == "11":
        daily_use_in_kWh = float(input("Enter daily use in kWh: "))
        while daily_use_in_kWh < 0:
            print("Invalid kWh!")
            daily_use_in_kWh = float(input("Enter daily use in kWh: "))
        number_of_billing_days = int(input("Enter number of billing days: "))
        while number_of_billing_days < 0:
            print("Invalid number of days!")
            number_of_billing_days = int(input("Enter number of billing days: "))
        estimated_bill = PRICE_PER_KWH_IN_DOLLARS * daily_use_in_kWh * number_of_billing_days * (1 + TARIFF_11)
        print("Estimated bill: $", estimated_bill)

    elif choice == "31":
        daily_use_in_kWh = float(input("Enter daily use in kWh: "))
        while daily_use_in_kWh < 0:
            print("Invalid kWh!")
            daily_use_in_kWh = float(input("Enter daily use in kWh: "))
        number_of_billing_days = int(input("Enter number of billing days: "))
        while number_of_billing_days < 0:
            print("Invalid number of days!")
            number_of_billing_days = int(input("Enter number of billing days: "))
        estimated_bill = PRICE_PER_KWH_IN_DOLLARS * daily_use_in_kWh * number_of_billing_days * (1 + TARIFF_31)
        print("Estimated bill: $", estimated_bill)

    else:
        print("Invalid option")
    print("Electricity bill estimator 2.0")
    choice = input("Which tariff? 11 or 31: ")
print("Finished!")
