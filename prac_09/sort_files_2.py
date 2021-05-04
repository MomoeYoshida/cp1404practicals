"""
Version 2
Write code to sort files in the FilesToSort.zip file
into subdirectories for each extension.

Let the user categorise different extensions as the program encounters these,
then move them all into those subdirectories.
"""
import os
import shutil


def main():
    """Sort files in the FilesToSort.zip file into subdirectories for each extension."""
    os.chdir('FilesToSort')
    extension_to_category = {}
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        extension = filename.split('.')[-1]
        make_subdirectories(extension, extension_to_category)
        shutil.move(filename, extension_to_category[extension])


def make_subdirectories(extension, extension_to_category):
    """Make the subdirectories in which different extensions are categorised by the user."""
    if extension not in extension_to_category:
        category = input("What category would you like to sort {} files into? ".format(extension))
        extension_to_category[extension] = category
        try:
            os.mkdir(category)
        except FileExistsError:
            pass


main()
