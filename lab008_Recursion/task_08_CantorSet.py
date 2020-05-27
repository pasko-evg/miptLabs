# Нарисуйте Канторово множество. Канторово множество нулевого порядка - горизонтальный отрезок.
# Удалив среднюю треть получим множество первого порядка. Повторяя данную процедуру получим остальные множества.

from turtle import Screen, Turtle


def set_draw(iter: int, letngth: int, turtle: Turtle):
    if iter == 0:
        turtle.pendown()
        turtle.forward(letngth)
        turtle.penup()
        turtle.goto(-letngth, -10)


def main():
    turtle = Turtle()
    turtle.speed(0)
    set_draw(0, 100, turtle)
    input()


if __name__ == '__main__':
    main()
