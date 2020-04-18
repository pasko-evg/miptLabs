# Три копии кривой Коха, построенные (остриями наружу) на сторонах правильного треугольника,
# образуют замкнутую кривую бесконечной длины, называемую снежинкой Коха. Нарисуйте ee.

import sys
from turtle import Screen, Turtle


def draw(length, n, turtle):


    # при нулевом - рисуем прямую
    if n == 0:
        turtle.forward(length)
        return

    length = length / 3
    draw(length, n - 1, turtle)
    turtle.left(60)
    draw(length, n - 1, turtle)
    turtle.right(120)
    draw(length, n - 1, turtle)
    turtle.left(60)
    draw(length, n - 1, turtle)



if __name__ == "__main__":
    sys.setrecursionlimit(20)

    screen = Screen()
    turtle = Turtle()
    turtle.shape('turtle')
    turtle.penup()
    turtle.goto(-250, 150)
    turtle.pendown()
    turtle.speed('fastest')

    length = 500
    for i in range(3):
        draw(length, 4, turtle)
        turtle.right(120)
    input()
    turtle.end_fill()

