"""
Version 1
Write code to sort files in the FilesToSort.zip file
into subdirectories for each extension.
"""
import os
import shutil


def main():
    """Sort files in the FilesToSort.zip file into subdirectories for each extension."""
    os.chdir('FilesToSort')
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        extension = filename.split('.')[-1]
        try:
            os.mkdir(extension)
        except FileExistsError:
            pass
        # Option 1 - use shutil.move()
        shutil.move(filename, extension)
        # Option 2 - use os.rename()
        # os.rename(filename, "{}/{}".format(extension, filename))


main()
