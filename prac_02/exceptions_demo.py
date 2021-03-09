"""
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator (non-zero number): "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# 1. It will occur when we do not enter a valid integer(number).
# For example, when we enter 2.5(float), a(character), ab,...etc, a ValueError will occur.

# 2. It will occur when we enter(type) '0' into a denominator.

# 3. To avoid the possibility of a ZeroDivisionError, I put '(non-zero number)' after 'Enter the denominator' as shown
# in the above code.
