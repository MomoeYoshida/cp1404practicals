"""
CP1404 Practical
Kivy GUI program to convert miles to kilometres
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty

__author__ = 'Momoe Yoshida'

FACTOR_MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    """MilesConverterApp is a Kivy App for the conversion of miles into kilometres."""
    output_km = StringProperty()  # Use a StringProperty for the text on the output (km) label.

    def build(self):
        """Build the Kivy App from the Kv file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        """Handle the conversion from miles to kilometres."""
        value = self.get_valid_miles()
        result = value * FACTOR_MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        """Handle pressing "Up"/"Down" buttons."""
        value = self.get_valid_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()  # make the result appear immediately when the up/down buttons are pressed

    def get_valid_miles(self):
        """Handle invalid inputs."""
        try:
            value = float(self.root.ids.input_miles.text)   # convert to float
            return value
        except ValueError:  # If the text entered is not a valid number, just set the output result to 0.0.
            return 0


MilesConverterApp().run()
