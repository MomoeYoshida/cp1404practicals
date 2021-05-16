"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os


def main():
    """Cleanup inconsistent song lyrics file names."""

    os.chdir('Lyrics')  # Change to desired directory
    for directory_name, subdirectories, filenames in os.walk('.'):
        # print("Directory:", directory_name)
        # print("\tcontains subdirectories:", subdirectories)
        # print("\tand files:", filenames)
        # print("(Current working directory is: {})".format(os.getcwd()))

        for filename in filenames:
            # Test just printing the names before renaming files.
            new_name = get_fixed_filename(filename)
            print("Renaming {} to {}".format(filename, new_name))
            # Rename files.
            full_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, get_fixed_filename(filename))
            os.rename(full_name, new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    filename = filename.replace(" ", "_").replace(".TXT", ".txt")
    new_name = ""  # Start with an empty string ""
    # Step through each character with its index with enumerate() and consider
    # how it relates to the character before or after it.
    for i, char in enumerate(filename):  # Step through each character with its index with enumerate()
        if i-1 == -1 or i+1 == len(filename):  # Add the very first and last character of a filename
            new_name += char
        if i-1 >= 0 and i+1 < len(filename):  # Avoid the "IndexError: string index out of range"
            previous_char = filename[i-1]
            current_char = char
            next_char = filename[i+1]
            if current_char.islower() and next_char.isupper():  # e.g. "tN" in "SilentNight.txt"
                new_name += current_char + '_'
            elif previous_char == '_' and current_char.islower():  # e.g. "_l" in "O_little_town_of_bethlehem.txt"
                new_name += current_char.upper()
            elif previous_char.isupper() and current_char.isupper():  # e.g. "OC" in "OComeAllYeFaithful.txt"
                new_name += '_' + current_char
            else:
                new_name += current_char
    return new_name


main()
