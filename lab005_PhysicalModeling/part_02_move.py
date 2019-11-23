import graphics as gr
from lab005_PhysicalModeling.gr_utils import add, sub, update_velocity, update_coords, update_acceleration

SIZE_X = 800
SIZE_Y = 800

window = gr.GraphWin("Model", SIZE_X, SIZE_Y)

# Параметры мира
coords = gr.Point(400, 700)
velocity = gr.Point(2, 0)
acceleration = gr.Point(0, 0)

rectangle = gr.Rectangle(gr.Point(0, 0), gr.Point(SIZE_X, SIZE_Y))
rectangle.setFill('green')
rectangle.draw(window)

circle = gr.Circle(coords, 10)
circle.setFill('red')
circle.draw(window)

sun = gr.Circle(gr.Point(400, 400), 50)
sun.setFill('yellow')
sun.draw(window)


def check_coords(_coords: gr.Point, _velocity):
    if _coords.x < 0 or _coords.x > SIZE_X:
        _velocity.x = - _velocity.x
    if _coords.y < 0 or _coords.y > SIZE_Y:
        _velocity.y = - _velocity.y


while True:
    circle.move(velocity.x, velocity.y)
    acceleration = update_acceleration(circle.getCenter(), gr.Point(400, 400))
    velocity = update_velocity(velocity, acceleration)

    check_coords(circle.getCenter(), velocity)
    gr.time.sleep(0.01)
