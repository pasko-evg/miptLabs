#!/usr/bin/python3

# Обойти стену. Размеры стены и расстояние до неё неизвестны. Стена одна.

from pyrob.api import *


@task
def task_5_4():
    while not wall_is_beneath():
        move_down()
    while wall_is_beneath():
        move_right()
    move_down()
    move_left()
    while wall_is_above():
        if not wall_is_on_the_left():
            move_left()
        else:
            break


if __name__ == '__main__':
    run_tasks()
