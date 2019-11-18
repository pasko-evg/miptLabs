#!/usr/bin/python3
# Закрасить отмеченные клетки.

from pyrob.api import *


def check_bottom_border():
    move_down(1)
    if wall_is_beneath():
        move_up()
        return True
    else:
        move_up()
        return False


def fill_line():
    move_right()
    i = 0
    while not wall_is_on_the_right():
        fill_cell()
        move_right()
        i += 1
    move_left(i + 1)
    move_down()


@task(delay=0.05)
def task_4_3():
    while True:
        if not check_bottom_border():
            fill_line()
        else:
            move_right()
            break


if __name__ == '__main__':
    run_tasks()
