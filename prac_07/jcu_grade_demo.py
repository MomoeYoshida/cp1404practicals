from kivy.app import App
from kivy.lang import Builder


class JCUGradeDemo(App):
    def build(self):
        self.title = "JCU Grade"
        self.root = Builder.load_file('jcu_grade_layout.kv')
        return self.root

    def handle_enter(self):
        print('test')
        score = float(self.root.ids.input_score.text)
        if score >= 85:
            self.root.ids.output_label.text = "HD - Pass with High Distinction"
        elif score >= 75:
            self.root.ids.output_label.text = "D - Pass with Distinction"
        elif score >= 65:
            self.root.ids.output_label.text = "C - Pass with Credit"
        elif score >= 50:
            self.root.ids.output_label.text = "P - Pass"
        else:
            self.root.ids.output_label.text = "F - Fail"

    def handle_clear(self):
        """Clear both the text field and the output label."""
        self.root.ids.input_score.text = ""
        self.root.ids.output_label.text = ""


JCUGradeDemo().run()
