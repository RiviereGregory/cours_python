import os

from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget

# Utile pour le pb d'openGL 1.1 pas 2.0
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'


class WidgetsExemple(GridLayout):
    compteur = 1
    # utilisation de StringProperty , BooleanProperty, ... pour pouvoir les utiliser
    # dans le fichier kv avec root.mon_texte, root.compteur_actif, ...
    mon_texte = StringProperty(str(compteur))
    compteur_actif = BooleanProperty(False)

    def on_button_click(self):
        print("Button click")
        if self.compteur_actif:
            self.compteur += 1
            self.mon_texte = str(self.compteur)

    def on_toggle_button_state(self, widget):
        print("Toggle state: " + widget.state)
        if widget.state == "normal":
            print("OFF")
            widget.text = "OFF"
            self.compteur_actif = False
        else:
            print("ON")
            widget.text = "ON"
            self.compteur_actif = True

    def on_switch_active(self, widget):
        print("Switch active: " + str(widget.active))


class MainWidget(Widget):
    pass


class StackLayoutExemple(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(0, 100):
            b = Button(text=str(i + 1), size_hint=(None, None), size=(dp(100), dp(100)))
            self.add_widget(b)


# class GridLayoutExemple(GridLayout):
#     pass

class AnchorLayoutExemple(AnchorLayout):
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
