"""
CP1404 Practical
Modify Existing GUI Program
"""

from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """BoxLayoutDemo is a Kivy App to greet the user."""
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):  # 5. Add a button handler function
        """Handle pressing Greet button."""
        print('test')
        # 6. Change the text of the label
        self.root.ids.output_label.text = "Hello " + self.root.ids.input_name.text
        # 9. Since this field has an id, we can now use the information in this
        # text entry field in our button handler function.

    # 10. Add a new event handler for the clear button
    def handle_clear(self):
        """Handle pressing Clear button."""
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = ""


BoxLayoutDemo().run()
