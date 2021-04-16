"""CP1404 Practical - ProgrammingLanguage class."""


class ProgrammingLanguage:
    """Represent information about a programming language."""

    def __init__(self, name, typing, reflection, year):
        """Initialise a ProgrammingLanguage instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return a string representation of a ProgrammingLanguage information."""
        return "{}, {} Typing, Reflection={}, First appeared in {}" \
            .format(self.name, self.typing, self.reflection, self.year)

    def is_dynamic(self):
        """Determine if a language is dynamically typed."""
        return self.typing == "Dynamic"

