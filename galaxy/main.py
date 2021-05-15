from kivy.app import App
from kivy.config import Config
from kivy.graphics import Color, Line
from kivy.properties import *
from kivy.properties import Clock
from kivy.uix.widget import Widget

Config.set('graphics', 'width', '900')
Config.set('graphics', 'height', '400')


class MainWidget(Widget):
    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)

    V_NB_LINES = 10
    V_LINES_SPACING = 0.25  # pourcentage sur la largeur de l'écran
    vertical_lines = []

    H_NB_LINES = 15
    H_LINES_SPACING = 0.1  # pourcentage sur la hauteur de l'écran
    horizontal_lines = []

    SPEED = 4
    current_offset_y = 0

    SPEED_X = 12
    current_speed_x = 0
    current_offset_x = 0

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        self.init_vertical_lines()
        self.init_horizontal_lines()
        Clock.schedule_interval(self.update, 1.0 / 60.0)

    def on_parent(self, widget, parent):
        pass

    def on_size(self, *args):
        pass

    def on_perspective_point_x(self, widget, value):
        pass

    def on_perspective_point_y(self, widget, value):
        pass

    def init_horizontal_lines(self):
        with self.canvas:
            Color(1, 1, 1)
            for i in range(0, self.H_NB_LINES):
                self.horizontal_lines.append(Line())

    def update_horizontal_lines(self):
        centrale_line_x = self.width / 2 + self.current_offset_x
        spacing = self.V_LINES_SPACING * self.width
        offset = -int(self.V_NB_LINES / 2) + 0.5

        xmin = centrale_line_x + offset * spacing
        xmax = centrale_line_x - offset * spacing
        spacing_y = self.H_LINES_SPACING * self.height
        for i in range(0, self.H_NB_LINES):
            line_y = i * spacing_y - self.current_offset_y
            x1, y1 = self.transform(xmin, line_y)
            x2, y2 = self.transform(xmax, line_y)
            self.horizontal_lines[i].points = [x1, y1, x2, y2]

    def init_vertical_lines(self):
        with self.canvas:
            Color(1, 1, 1)
            for i in range(0, self.V_NB_LINES):
                self.vertical_lines.append(Line())

    def update_vertical_lines(self):
        centrale_line_x = self.width / 2 + self.current_offset_x
        spacing = self.V_LINES_SPACING * self.width
        offset = -int(self.V_NB_LINES / 2) + 0.5
        for i in range(0, self.V_NB_LINES):
            line_x = centrale_line_x + offset * spacing
            x1, y1 = self.transform(line_x, 0)
            x2, y2 = self.transform(line_x, self.height)
            self.vertical_lines[i].points = [x1, y1, x2, y2]
            offset += 1

    def transform_perspective(self, pt_x, pt_y):
        lin_y = pt_y * self.perspective_point_y / self.height
        if lin_y > self.perspective_point_y:
            lin_y = self.perspective_point_y

        diff_x = pt_x - self.perspective_point_x
        diff_y = self.perspective_point_y - lin_y
        factor_y = diff_y / self.perspective_point_y
        factor_y = pow(factor_y, 4)
        offset_x = diff_x * factor_y

        tr_x = self.perspective_point_x + offset_x
        tr_y = self.perspective_point_y - factor_y * self.perspective_point_y

        return int(tr_x), int(tr_y)

    def transform(self, pt_x, pt_y):
        # return self.transform_2d(pt_x, pt_y)
        return self.transform_perspective(pt_x, pt_y)

    def transform_2d(self, pt_x, pt_y):
        return int(pt_x), int(pt_y)

    def on_touch_down(self, touch):
        if touch.x < self.width/2:
            # print("<-")
            self.current_speed_x = self.SPEED_X
        else:
            # print("->")
            self.current_speed_x = -self.SPEED_X

    def on_touch_up(self, touch):
        # print("UP")
        self.current_speed_x = 0

    def update(self, dt):
        time_factor = dt * 60  # = 1 si on a bien 1.0/60.0
        self.update_vertical_lines()
        self.update_horizontal_lines()
        self.current_offset_y += self.SPEED * time_factor
        self.current_offset_x += self.current_speed_x * time_factor

        spacing_y = self.H_LINES_SPACING * self.height
        if self.current_offset_y >= spacing_y:
            self.current_offset_y -= spacing_y


class GalaxyApp(App):
    pass


GalaxyApp().run()
