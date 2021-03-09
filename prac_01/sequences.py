"""Menu-driven number sequence generator"""

x = int(input("Enter the value for x: "))
y = int(input("Enter the value for y: "))

# i. Show the even numbers from x to y
if x % 2 == 0:
    for i in range(x, y, 2):
        print(i, end='')
    print()
else:
    for i in range(x, y, 1):
        print(i, end='')
    print()
# ii. Show the odd numbers from x to y
if x % 2 == 1:
    for i in range(x, y, 2):
        print(i, end='')
    print()
else:
    for i in range(x, y, 1):
        print(i, end='')
    print()
# iii. Show the squares from x to uy

# iv. Exit the program
print("Exit.")
