from kivy.app import App
from kivy.graphics import Color, Line
from kivy.properties import *
from kivy.uix.widget import Widget


class MainWidget(Widget):
    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)

    V_NB_LINES = 7
    V_LINES_SPACING = 0.1  # pourcentage sur la largeru de l'écran
    vertical_lines = []

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        self.init_vertical_lines()

    def on_parent(self, widget, parent):
        pass

    def on_size(self, *args):
        self.update_vertical_lines()
        pass

    def on_perspective_point_x(self, widget, value):
        pass

    def on_perspective_point_y(self, widget, value):
        pass

    def init_vertical_lines(self):
        with self.canvas:
            Color(1, 1, 1)
            for i in range(0, self.V_NB_LINES):
                self.vertical_lines.append(Line())

    def update_vertical_lines(self):
        centrale_line_x = self.width / 2
        spacing = self.V_LINES_SPACING * self.width
        offset = -int(self.V_NB_LINES / 2)
        for i in range(0, self.V_NB_LINES):
            x1 = int(centrale_line_x + offset * spacing)
            y1 = 0
            x2 = x1
            y2 = self.height
            self.vertical_lines[i].points = [x1, y1, x2, y2]
            offset += 1


class GalaxyApp(App):
    pass


GalaxyApp().run()
