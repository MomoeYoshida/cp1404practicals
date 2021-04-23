"""
A very simple App that has a list of names (strings) and displays each one
as a separate Label
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """DynamicLabelsApp is a very simple App that has a list of names (strings) and displays each one
as a separate Label."""
    def __init__(self):
        """Construct main app."""
        self.names = ["Bob Brown", "Cat Cyan", "Oren Ochre", "Momoe Yoshida"]

    def build(self):
        """"""
        self.title = "Dynamic Labels"
        self.display_names()

    def display_names(self):
        """Display each name as a separate Label."""
        for name in self.names:
            temp_label = Label(text=name)


DynamicLabelsApp().run()
