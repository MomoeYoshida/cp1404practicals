from kivy.app import App
from kivy.lang import Builder

__author__ = 'Momoe Yoshida'


class TemperatureConverterApp(App):
    """TemperatureConverterApp is a Kivy App to convert temperatures."""

    def build(self):
        """Build the Kivy App from the Kv file."""
        self.title = "Temperature Converter"
        self.root = Builder.load_file('temperature_converter.kv')
        return self.root

    def convert_celsius_to_fahrenheit(self):
        """Convert celsius to fahrenheit."""
        value = self.get_valid_temperatures()
        fahrenheit = value * 9.0 / 5 + 32
        self.root.ids.output_label.text = str(fahrenheit)

    def convert_fahrenheit_to_celsius(self):
        """Convert fahrenheit to celsius."""
        value = self.get_valid_temperatures()
        celsius = 5 / 9 * (value - 32)
        self.root.ids.output_label.text = str(celsius)

    def get_valid_temperatures(self):
        """Handle invalid inputs."""
        try:
            value = float(self.root.ids.input_temperatures.text)
            return value
        except ValueError:
            return 0

    def handle_quit(self):
        """Clear both the text field and the output label."""
        self.root.ids.input_temperatures.text = ''
        self.root.ids.output_label.text = 'Enter Temperature\nC - Convert Celsius to Fahrenheit\nF - Convert ' \
                                          'Fahrenheit to Celsius\nQ - Quit '


TemperatureConverterApp().run()
