#!/usr/bin/python3

# Перейти на вторую закрашенную клетку. Клетка может быть как справа, так и слева.

from pyrob.api import *


@task
def task_8_27():
    while not cell_is_filled():
        move_up()
    while True:
        if move_right() or cell_is_filled():
            break
        else:
            move_left()
        if move_left() or cell_is_filled():
            break
        else:
            move_right()


if __name__ == '__main__':
    run_tasks()
