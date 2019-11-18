#!/usr/bin/python3

# Выйти из ловушки. Выход может находиться как справа, так и слева.
# Выхода может не быть, в этом случае остановиться в правом тупике.

from pyrob.api import *


def escape():
    while not wall_is_above():
        move_up()
    while not wall_is_on_the_left():
        move_left()
    return False


@task
def task_8_29():
    in_trap = True
    if not wall_is_above():
        in_trap = escape()

    while not wall_is_on_the_left() and in_trap:
        move_left()
        if not wall_is_above():
            in_trap = escape()

    while not wall_is_on_the_right() and in_trap:
        move_right()
        if not wall_is_above():
            in_trap = escape()


if __name__ == '__main__':
    run_tasks()
