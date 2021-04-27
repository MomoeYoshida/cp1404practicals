from kivy.app import App
from kivy.lang import Builder


class GreeterProgram(App):
    def build(self):
        self.title = "Greeter Program"
        self.root = Builder.load_file('greeter_program_layout.kv')
        return self.root

    def handle_greet(self):
        print('test')
        self.root.ids.output_label.text = "Hello " + self.root.ids.input_name.text

    def handle_clear(self):
        """Clear both the text field and the output label."""
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = ""


GreeterProgram().run()
