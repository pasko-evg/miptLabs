# Нарисуйте кривую Леви. Она получается, если взять половину квадрата вида /\,
# а затем каждую сторону заменить таким же фрагментом и так далее.

from turtle import Screen, Turtle


def dragon_build(turtle_string, n):
    """ Recursively builds a draw string. """
    """ defining f, +, -, as additional rules that don't do anything """
    rules = {'x': 'x+yf', 'y': 'fx-y', 'f': 'f', '-': '-', '+': '+'}
    turtle_string = ''.join([rules[x] for x in turtle_string])
    if n > 1:
        return dragon_build(turtle_string, n-1)
    else:
        return turtle_string


def dragon_draw(size, turtle):
    """ Draws a Dragon Curve of length 'size'. """
    turtle_string = dragon_build('fx', size)
    # print(turtle_string)
    for x in turtle_string:
        if x == 'f':
            turtle.forward(5)
        elif x == '+':
            turtle.right(90)
        elif x == '-':
            turtle.left(90)


def main():
    # n = input("Size of Dragon Curve (int): ")
    turtle = Turtle()
    turtle.speed(0)
    dragon_draw(10, turtle)
    input()


if __name__ == '__main__':
    main()
