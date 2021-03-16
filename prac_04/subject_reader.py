"""
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Read subject data and display it."""
    data = get_data()
    display_subjects(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    input_file = open(FILENAME)
    for line in input_file:
        print(line)
        print(repr(line))
        line = line.strip()
        parts = line.split(',')
        print(parts)
        parts[2] = int(parts[2])
        print(parts)
        data.append(parts)
    input_file.close()
    return data


def display_subjects(data):
    """Display subject details."""
    for subject_data in data:
        print("{} is taught by {:12} and has {:3} students".format(*subject_data))


main()
