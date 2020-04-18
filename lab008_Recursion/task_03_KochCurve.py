# Нарисуйте кривую Коха. Процесс её построения выглядит следующим образом:
# берём единичный отрезок, разделяем на три равные части и заменяем средний интервал равносторонним треугольником без этого сегмента.
# В результате образуется ломаная, состоящая из четырёх звеньев длины 1/3.
# На следующем шаге повторяем операцию для каждого из четырёх получившихся звеньев и т. д… Предельная кривая и есть кривая Коха.

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
    turtle.goto(-400, 0)
    turtle.pendown()
    turtle.speed('fastest')

    draw(800, 5, turtle)
    input()
    turtle.end_fill()

