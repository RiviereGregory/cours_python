from kivy.app import App
from kivy.lang import Builder
from kivy.properties import *
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
# il faut la mettre pour avoir l'image en cover
from kivy.uix.behaviors import CoverBehavior

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
        self.pizzas = [
            Pizza("4 fromages", "chèvre, emmentale, brie, comté", 9.5, True),
            Pizza("Chorizo", "tomate, chorizo, parmesan", 12.2, False),
            Pizza("Calsone", "emmentale, jambon, champignons", 10, False),
            Pizza("Dolcetta", "creme, emmentale, jambon, champignons", 12, False)

        ]

    def on_parent(self, widget, parent):
        self.recycleView.data = [pizza.get_dictionary() for pizza in self.pizzas]


with open("pizzascr.kv", encoding='utf8') as f:
    Builder.load_string(f.read())


class PizzaApp(App):
    def build(self):
        return MainWidget()


PizzaApp().run()
