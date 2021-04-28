import os

from kivy.app import App
from kivy.uix.widget import Widget

# Utile pour le pb d'openGL 1.1 pas 2.0
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'


class MainWidget(Widget):
    pass


class LelabApp(App):
    pass


LelabApp().run()
