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
    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ["Bob Brown", "Cat Cyan", "Oren Ochre", "Momoe Yoshida"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.display_names()
        return self.root

    def display_names(self):
        """Display each name as a separate Label."""
        for name in self.names:
            temp_label = Label(text=name)  # Create the widgets (labels) in Python code
            self.root.ids.entries_box.add_widget(temp_label)  # Add these new widgets using the add_widget method


DynamicLabelsApp().run()
