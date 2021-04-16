"""CP1404 Practical - Client code to use the ProgrammingLanguage class.
Import the ProgrammingLanguage class and copy 3 lines."""

from prac_06.programming_language import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    # Check if my __str__ function is working properly.
    print(ruby)
    print(python)
    print(visual_basic)

    # Create a new list that contains these three existing ProgrammingLanguage objects.
    languages = [ruby, python, visual_basic]
    # Loop through and print the names of all of the languages with dynamic typing.
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()
