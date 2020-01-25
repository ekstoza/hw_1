#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_4():
    while(wall_is_on_the_left()):
        if(not wall_is_beneath()):
            move_down()
        elif(wall_is_beneath()):
            move_right()


if __name__ == '__main__':
    run_tasks()
