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
