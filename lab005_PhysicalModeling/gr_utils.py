import graphics as gr


def add(point_1: gr.Point, point_2: gr.Point):
    new_point = gr.Point(point_1.x + point_2.x, point_1.y + point_2.y)
    return new_point


def sub(point_1: gr.Point, point_2: gr.Point):
    new_point = gr.Point(point_1.x - point_2.x, point_1.y - point_2.y)
    return new_point


def update_velocity(_velocity, _acceleration):
    return add(_velocity, _acceleration)


def update_coords(_coords, _velocity):
    return add(_coords, _velocity)


def update_acceleration(_ball_coords, _center_coords):
    diff = sub(_ball_coords, _center_coords)
    distance_2 = (diff.x ** 2 + diff.y ** 2) ** (3 / 2)
    G = 2000

    return gr.Point(-diff.x * G / distance_2, -diff.y * G / distance_2)

