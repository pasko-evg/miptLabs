# Нарисуйте кривую Минковского. Кривая Минковского нулевого порядка - горизонтальный отрезок.
# Затем на каждом шаге каждый из отрезков заменяется на ломанную, состоящую из 8 звеньев.

import sys
from turtle import Screen, Turtle


def draw(length, n, turtle):


    # при нулевом - рисуем прямую
    if n == 0:
        turtle.forward(length)
        return

    length = length / 4
    draw(length, n - 1, turtle)
    turtle.left(90)
    draw(length, n - 1, turtle)
    turtle.right(90)
    draw(length, n - 1, turtle)
    turtle.right(90)
    draw(length, n - 1, turtle)
    draw(length, n - 1, turtle)
    turtle.left(90)
    draw(length, n - 1, turtle)
    turtle.left(90)
    draw(length, n - 1, turtle)
    turtle.right(90)
    draw(length, n - 1, turtle)



if __name__ == "__main__":
    sys.setrecursionlimit(20)

    screen = Screen()
    turtle = Turtle()
    turtle.shape('turtle')
    turtle.penup()
    turtle.goto(-400, 0)
    turtle.pendown()
    turtle.speed('fastest')

    length = 800
    draw(length, 4, turtle)
    turtle.right(120)
    input()
    turtle.end_fill()

