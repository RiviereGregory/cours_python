from kivy.app import App
from kivy.lang import Builder
from kivy.properties import *
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
# il faut la mettre pour avoir l'image en cover
from kivy.uix.behaviors import CoverBehavior

from http_client import HttpClient
from models import Pizza


class PizzaWidget(BoxLayout):
    nom = StringProperty()
    ingredients = StringProperty()
    prix = NumericProperty()
    vegetarienne = BooleanProperty()


class MainWidget(FloatLayout):
    recycleView = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        HttpClient.get_pizzas(self, self.on_server_data)

    def on_server_data(self, pizzas_dict):
        self.recycleView.data = pizzas_dict


with open("pizzascr.kv", encoding='utf8') as f:
    Builder.load_string(f.read())


class PizzaApp(App):
    def build(self):
        return MainWidget()


PizzaApp().run()
