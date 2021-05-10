from kivy.app import App
from kivy.lang import Builder
from kivy.properties import *
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
# il faut la mettre pour avoir l'image en cover
from kivy.uix.behaviors import CoverBehavior

from http_client import HttpClient
from storage_manager import StorageManager


# il faut la mettre pour avoir l'image en cover


class PizzaWidget(BoxLayout):
    nom = StringProperty()
    ingredients = StringProperty()
    prix = NumericProperty()
    vegetarienne = BooleanProperty()


class MainWidget(FloatLayout):
    recycleView = ObjectProperty(None)
    error_str = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        HttpClient.get_pizzas(self, self.on_server_data, self.on_server_error)

    def on_parent(self, widget, parent):
        load_data = StorageManager().load_data("pizzas")
        if load_data:
            self.recycleView.data = load_data

    def on_server_data(self, pizzas_dict):
        self.recycleView.data = pizzas_dict
        StorageManager().save_data("pizzas", pizzas_dict)

    def on_server_error(self, error):
        self.error_str = "ERROR: " + error
        print(self.error_str)


with open("pizzascr.kv", encoding='utf8') as f:
    Builder.load_string(f.read())


class PizzaApp(App):
    def build(self):
        return MainWidget()


PizzaApp().run()
