#!/usr/bin/python3

# from pyrob.api import *
from lab002_Robot.pyrob.api import *


@task
def task_1_2():
    for i in range(2):
        move_right()
        move_down()
    fill_cell()
    move_right()
    move_right()
    move_down()


if __name__ == '__main__':
    run_tasks()
