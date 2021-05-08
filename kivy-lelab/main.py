import os

from kivy.app import App
# Utile pour le pb d'openGL 1.1 pas 2.0
from kivy.properties import ObjectProperty

from navigation_screen_manager import NavigationScreenManager

os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'


class MyScreenManager(NavigationScreenManager):
    pass


class LelabApp(App):
    manager = ObjectProperty(None)

    def build(self):
        self.manager = MyScreenManager()
        return self.manager


LelabApp().run()
