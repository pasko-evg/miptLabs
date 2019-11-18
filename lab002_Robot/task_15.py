#!/usr/bin/python3

from pyrob.api import *


def move_to_wall(args):
    move_to_direct = args[0]
    check_wall = args[1]
    while not check_wall():
        move_to_direct()


@task
def task_8_21():
    angle = {
        "up": [move_up, wall_is_above],
        "down": [move_down, wall_is_beneath],
        "left": [move_left, wall_is_on_the_left],
        "right": [move_right, wall_is_on_the_right],
    }
    if wall_is_beneath() and wall_is_on_the_left():
        move_to_wall(angle['up'])
        move_to_wall(angle['right'])
    elif wall_is_beneath() and wall_is_on_the_right():
        move_to_wall(angle['up'])
        move_to_wall(angle['left'])
    elif wall_is_above() and wall_is_on_the_right():
        move_to_wall(angle['down'])
        move_to_wall(angle['left'])
    elif wall_is_above() and wall_is_on_the_left():
        move_to_wall(angle['down'])
        move_to_wall(angle['right'])


if __name__ == '__main__':
    run_tasks()
