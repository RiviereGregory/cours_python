from kivy.app import App
from kivy.properties import *
from kivy.uix.boxlayout import BoxLayout

from models import Pizza


class PizzaWidget(BoxLayout):
    nom = StringProperty()
    ingredients = StringProperty()
    prix = NumericProperty()
    vegetarienne = BooleanProperty()


class MainWidget(BoxLayout):
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


class PizzaApp(App):
    pass


PizzaApp().run()
