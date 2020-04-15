# Нарисуйте кривую Коха. Процесс её построения выглядит следующим образом:
# берём единичный отрезок, разделяем на три равные части и заменяем средний интервал равносторонним треугольником без этого сегмента.
# В результате образуется ломаная, состоящая из четырёх звеньев длины 1/3.
# На следующем шаге повторяем операцию для каждого из четырёх получившихся звеньев и т. д… Предельная кривая и есть кривая Коха.


from turtle import Screen, Turtle


def draw(length, n, turtle):

    # при нулевом - разворот
    if n == 0:
        turtle.left(180)
        return

    if n == 1:
        length = length / 3
        turtle.forward(length)
        turtle.left(60)
        turtle.forward(length)
        turtle.right(120)
        turtle.forward(length)
        turtle.left(60)
        turtle.forward(length)
        return

    # x = l / (n + 1)
    # for i in range(n):
    #     turtle.forward(x)
    #     turtle.left(45)
    #     draw(0.5 * x * (n - i - 1), n - i - 1, turtle)
    #     turtle.left(90)
    #     draw(0.5 * x * (n - i - 1), n - i - 1, turtle)
    #     turtle.right(135)

    # turtle.forward(x)
    # turtle.left(180)
    # turtle.forward(l)


if __name__ == "__main__":
    screen = Screen()
    turtle = Turtle()
    turtle.speed('fastest')

    draw(300, 1, turtle)
    input()
    turtle.end_fill()

