#!/usr/bin/python3

# Дойти до конца тупика. Тупик имеет форму буквы Г (влево или вправо). Размеры тупика не известны.

from pyrob.api import *


@task
def task_8_22():
    while not wall_is_above():
        move_up()
    if wall_is_on_the_right():
        while not wall_is_on_the_left():
            move_left()
    elif wall_is_on_the_left():
        while not wall_is_on_the_right():
            move_right()


if __name__ == '__main__':
    run_tasks()
