from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty


class DynamicButtonsApp(App):
    """DynamicButtonsApp is a dynamically generated GUI with a button for each
    person found in a file."""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.name_to_age = {"Bill Gates": "72", "Bob Brown": "23", "Cat Cyan": "46", "Oren Ochre": "3"}

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Buttons"
        self.root = Builder.load_file('dynamic_buttons.kv')
        self.create_buttons()
        return self.root

    def create_buttons(self):
        """Create buttons from dictionary entries and add them to the GUI."""
        for name in self.name_to_age:
            temp_button = Button(text=name)
            temp_button.bind(on_release=self.press_entry)
            self.root.ids.entries_box.add_widget(temp_button)

    def press_entry(self, instance):
        """Handle pressing entry buttons."""
        name = instance.text
        self.status_text = "{}'s age is {}".format(name, self.name_to_age[name])


DynamicButtonsApp().run()
