import graphics as gr
from lab005_PhysicalModeling.gr_utils import add, sub, update_velocity, update_coords, update_acceleration

SIZE_X = 800
SIZE_Y = 800

window = gr.GraphWin("Model", SIZE_X, SIZE_Y)

# Начальное положение шарика
coords = gr.Point(200, 200)

# Скорость
velocity = gr.Point(1, -2)
acceleration = gr.Point(0, 0)


def draw_circle(_coords: gr.Point):
    circle = gr.Circle(_coords, 10)
    circle.setFill('red')
    circle.draw(window)


def clear_window():
    rectangle = gr.Rectangle(gr.Point(0, 0), gr.Point(SIZE_X, SIZE_Y))
    rectangle.setFill('green')
    rectangle.draw(window)


def check_coords(_coords: gr.Point, _velocity):
    if _coords.x < 0 or _coords.x > SIZE_X:
        _velocity.x = - _velocity.x
    if _coords.y < 0 or _coords.y > SIZE_Y:
        _velocity.y = - _velocity.y


while True:
    clear_window()
    draw_circle(coords)
    acceleration = update_acceleration(coords, gr.Point(400, 400))
    coords = update_coords(coords, velocity)
    velocity = update_velocity(velocity, acceleration)
    check_coords(coords, velocity)
    gr.time.sleep(0.01)
