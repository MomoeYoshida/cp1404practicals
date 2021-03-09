"""
Files
"""
# 1. Write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it.
name = input("What is you name? ")
out_file = open("name.txt", "w")
out_file.write(name)
out_file.close()

# 2. Write code that opens "name.txt" and reads the name (as above) then prints,
# "Your name is Bob" (or whatever the name is in the file).
in_file = open("name.txt", "r")
name = in_file.read().strip()  # can we use str(in_file.read()) instead?
in_file.close()
print("Your name is", name)

# 3. Create a text file called numbers.txt and save it in your prac_02 directory. Put the following three numbers (
# 17, 42, 400) on separate lines in the file and save it. Write code that opens "numbers.txt", reads only the first
# two numbers and adds them together then prints the result, which should be... 59.
in_file = open("numbers.txt", "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
in_file.close()
print(number1 + number2)

# 4. Now write a fourth block of code that prints the total for all lines in numbers.txt
# or a file with any number of numbers.
in_file = open("numbers.txt", "r")
total = 0
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(total)
