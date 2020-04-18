# Нарисуйте кривую Леви. Она получается, если взять половину квадрата вида /\,
# а затем каждую сторону заменить таким же фрагментом и так далее.

from turtle import Screen, Turtle
from math import sqrt


def draw(length, n, turtle):

    # при нулевом - рисуем прямую
    if n == 0:
        turtle.forward(length)
        return

    length = length / sqrt(2)
    turtle.left(45)
    draw(length, n - 1, turtle)
    turtle.right(90)
    draw(length, n - 1, turtle)
    turtle.left(45)


if __name__ == "__main__":
    screen = Screen()
    turtle = Turtle()
    turtle.shape('turtle')
    turtle.penup()
    turtle.goto(-200, -100)
    turtle.pendown()
    turtle.speed('fastest')

    length = 400
    draw(length, 12, turtle)
    turtle.right(120)
    input()
    turtle.end_fill()
