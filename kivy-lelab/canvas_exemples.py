from kivy.graphics import Line, Color, Rectangle
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.widget import Widget

# permet de charger un fichier kv
Builder.load_file("canvas_exemples.kv")


class CanvasExemple1(Widget):
    pass


class CanvasExemple2(Widget):
    pass


class CanvasExemple3(Widget):
    pass


class CanvasExemple4(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Line(points=(100, 100, 400, 500), width=2)
            Color(0, 1, 0)
            Line(circle=(400, 200, 80), width=2)
            Line(rectangle=(100, 400, 150, 100), width=2)
            self.rect = Rectangle(pos=(100, 200), size=(150, 100))

    def on_button_a_click(self):
        x, y = self.rect.pos
        x += dp(10)
        self.rect.pos = (x, y)
