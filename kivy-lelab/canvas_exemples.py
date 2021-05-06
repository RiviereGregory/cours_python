from kivy.graphics import Line, Color, Rectangle, Ellipse
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import Clock
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
        w, h = self.rect.size
        inc = dp(10)
        if (x + inc + w) < self.width:
            x += inc
        else:
            x = self.width - w

        self.rect.pos = (x, y)


class CanvasExemple5(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size = dp(50)
        with self.canvas:
            self.ball = Ellipse(pos=(100, 100), size=(self.ball_size, self.ball_size))
        Clock.schedule_interval(self.update, 1 / 60)

    def on_size(self, *args):
        print("on size:" + str(self.width) + ", " + str(self.height))
        self.ball.pos = (self.center_x - self.ball_size / 2, self.center_y - self.ball_size / 2)

    def update(self, dt):
        print("update")
        x, y = self.ball.pos
        w, h = self.ball.size
        inc = dp(10)
        if (x + inc + w) < self.width:
            x += inc
        else:
            x = self.width - w
        self.ball.pos = (x, y)
