import graphics as gr
from graphics import Point, color_rgb, GraphWin, Polygon


def get_isosceles_triangle(start_point: Point, length_base: int, height: int):
    point_a = start_point
    point_b = Point(point_a.getX() + length_base, point_a.getY())
    point_c = Point((point_a.getX() + point_b.getX()) / 2, point_a.getY() - height)
    return Polygon(point_a, point_b, point_c)


def get_rectangle(start_point: Point, length: int, height: int):
    point_a = start_point
    point_b = Point(start_point.getX(), start_point.getY() - height)
    point_c = Point(start_point.getX() + length, start_point.getY() - height)
    point_d = Point(start_point.getX() + length, start_point.getY())
    return Polygon(point_a, point_b, point_c, point_d)


def draw_background(palette: GraphWin):
    _height = palette.getHeight()
    _width = palette.getWidth()

    sky_percentage = 0.7

    sky = get_rectangle(gr.Point(0, _height * sky_percentage), _width, _height * sky_percentage)
    land = get_rectangle(gr.Point(0, _height), _width, _height * (1 - sky_percentage))
    sun = gr.Circle(gr.Point(_width * 0.85, _height * 0.15), _height * 0.1)

    sky.setFill(gr.color_rgb(0, 0, 200))
    land.setFill(gr.color_rgb(80, 240, 20))
    sun.setFill(gr.color_rgb(255, 255, 0))

    sky.draw(palette)
    land.draw(palette)
    sun.draw(palette)

    sky_shift = _height * 0.15
    for i in range(5):
        cloud = gr.Circle(gr.Point(0 + sky_shift, _height * 0.15), _height * 0.05)
        cloud.setFill(gr.color_rgb(255, 255, 255))
        cloud.draw(palette)
        sky_shift += _height * 0.1 / 2
    sky_shift = _height * 0.175
    for i in range(4):
        cloud = gr.Circle(gr.Point(0 + sky_shift, _height * 0.10), _height * 0.05)
        cloud.setFill(gr.color_rgb(255, 255, 255))
        cloud.draw(palette)
        sky_shift += _height * 0.1 / 2


def draw_house(start_point: Point, width: int, height: int, palette: GraphWin):
    house_body = get_rectangle(start_point, width, height)
    house_body.setFill(gr.color_rgb(192, 192, 192))
    house_body.draw(palette)
    house_roof = get_isosceles_triangle(Point(start_point.getX() - 20, start_point.getY() - height), width + 40, 100)
    house_roof.setFill(gr.color_rgb(128, 64, 0))
    house_roof.draw(palette)

    house_center_x = start_point.getX() + width / 2
    house_center_y = start_point.getY() - height / 2

    window_a = get_rectangle(Point(house_center_x, house_center_y), int(width / 4), int(height / 4))
    window_b = get_rectangle(Point(house_center_x, house_center_y), int(- width / 4), int(height / 4))
    window_c = get_rectangle(Point(house_center_x, house_center_y), int(width / 4), int(- height / 4))
    window_d = get_rectangle(Point(house_center_x, house_center_y), int(- width / 4), int(- height / 4))

    window_a.setFill(gr.color_rgb(0, 255, 255))
    window_b.setFill(gr.color_rgb(0, 255, 255))
    window_c.setFill(gr.color_rgb(0, 255, 255))
    window_d.setFill(gr.color_rgb(0, 255, 255))

    window_a.draw(palette)
    window_b.draw(palette)
    window_c.draw(palette)
    window_d.draw(palette)


def draw_christmas_tree(center_point: Point, width: int, height: int, palette: GraphWin):
    trunk = get_rectangle(Point(center_point.getX() - width * 0.05, center_point.getY()), int(width * 0.1),
                          int(height * 0.1))
    trunk.setFill(gr.color_rgb(128, 64, 0))
    trunk.draw(palette)

    tier_diff = height / 5
    tier_falloff = 0.8

    tier_a = get_isosceles_triangle(Point(center_point.getX() - width / 2, center_point.getY() - int(height * 0.1)),
                                    width, int(height * 0.5))
    tier_b = get_isosceles_triangle(
        Point(center_point.getX() - (width / 2) * tier_falloff, center_point.getY() - int(height * 0.1) - tier_diff),
        int(width * tier_falloff), int(height * 0.5 * tier_falloff))
    tier_c = get_isosceles_triangle(
        Point(center_point.getX() - width / 2 * tier_falloff ** 2,
              center_point.getY() - int(height * 0.1) - tier_diff * 2),
        int(width * tier_falloff ** 2), int(height * 0.5 * tier_falloff ** 2))
    tier_a.setFill(gr.color_rgb(0, 80, 0))
    tier_b.setFill(gr.color_rgb(0, 80, 0))
    tier_c.setFill(gr.color_rgb(0, 80, 0))

    tier_a.draw(palette)
    tier_b.draw(palette)
    tier_c.draw(palette)


if __name__ == '__main__':
    window = gr.GraphWin("Landscape", 640, 480)

    draw_background(window)
    draw_house(Point(150, 400), 150, 150, window)
    draw_christmas_tree(Point(500, 420), 150, 200, window)

    window.getMouse()

    window.close()
