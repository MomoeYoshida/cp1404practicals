"""
Broken program to determine score status
"""

# the most efficient if-elif-else 'ladder'
score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score")
elif score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
else:
    print("Bad")
score = float(input("Enter score: "))

# the other way to answer the question by using if-elif-else with 'while'
score = float(input("Enter score: "))
while 0 <= score <= 100:
    if score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")
    score = float(input("Enter score: "))
print("Invalid score")
