from kivy.app import App
from kivy.graphics import Color, Line
from kivy.properties import *
from kivy.uix.widget import Widget


class MainWidget(Widget):
    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)

    V_NB_LINES = 10
    V_LINES_SPACING = 0.2  # pourcentage sur la largeru de l'écran
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
        offset = -int(self.V_NB_LINES / 2) + 0.5
        for i in range(0, self.V_NB_LINES):
            line_x = int(centrale_line_x + offset * spacing)
            x1, y1 = self.transform(line_x, 0)
            x2, y2 = self.transform(line_x, self.height)
            self.vertical_lines[i].points = [x1, y1, x2, y2]
            offset += 1

    def transform_perspective(self, pt_x, pt_y):
        tr_y = pt_y * self.perspective_point_y / self.height
        if tr_y > self.perspective_point_y:
            tr_y = self.perspective_point_y

        diff_x = pt_x - self.perspective_point_x
        diff_y = self.perspective_point_y - tr_y
        factor_y = diff_y / self.perspective_point_y
        offset_x = diff_x * factor_y

        tr_x = self.perspective_point_x + offset_x

        return tr_x, tr_y

    def transform(self, pt_x, pt_y):
        # return self.transform_2d(pt_x, pt_y)
        return self.transform_perspective(pt_x, pt_y)

    def transform_2d(self, pt_x, pt_y):
        return pt_x, pt_y


class GalaxyApp(App):
    pass


GalaxyApp().run()
