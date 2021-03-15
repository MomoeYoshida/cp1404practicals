"""
What values do the following expressions have?
Without running the code, write down your answers to
these questions in your Python file as a comment, then
use Python to see if you were correct.
"""
numbers = ["ten", 1, 4, 1, 5, 9, 1]

print(numbers[-1])  # 2
print(numbers[3])  # 1
print(numbers[:-1])  # [3, 1, 4, 1, 5, 9]
print(numbers[3:4])  # [1]
print(5 in numbers)  # True
print(7 in numbers)  # False
print("3" in numbers)  # False
print(numbers + [6, 5, 3])  # [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Get all the elements from numbers except the first two
print(numbers[2:])
# Check if 9 is an element of numbers
print(9 in numbers)

