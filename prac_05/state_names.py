"""
This is a program that uses a 'constant' (name is ALL_CAPS) dictionary to store
the Australian state abbreviations and names.
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

state_code = input("Enter short state: ").upper()
while state_code != "":
    if state_code in CODE_TO_NAME:
        print(state_code, "is", CODE_TO_NAME[state_code])
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()

# 4. Write a loop that prints all of the states and names neatly lined up with string formatting
for state_code, CODE_TO_NAME[state_code] in CODE_TO_NAME.items():
    print("{:3} is {}".format(state_code, CODE_TO_NAME[state_code]))
