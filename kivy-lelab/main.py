import os

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget

# Utile pour le pb d'openGL 1.1 pas 2.0
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'


class MainWidget(Widget):
    pass


class BoxLayoutExemple(BoxLayout):
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     self.orientation = "vertical"
    #     b1 = Button(text="A")
    #     b2 = Button(text="B")
    #     b3 = Button(text="C")
    #     self.add_widget(b1)
    #     self.add_widget(b2)
    #     self.add_widget(b3)
    pass


class LelabApp(App):
    pass


LelabApp().run()