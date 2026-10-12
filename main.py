from kivy.app import App
from kivy.uix.label import Label

class MiApp(App):
    def build(self):
        return Label(text="ya lo hicimoooooos", font_size=40)

MiApp().run()
