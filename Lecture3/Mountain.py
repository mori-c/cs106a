from karel.stanfordkarel import *

"""
File: Mountain.py
----------------------------
Karel climbs a mountain of any size
and plants a beeper at the top

ascend
    step_up
top_point
descent

"""
def main():
    ascend_mountain()
    put_beeper()
    descend_mountain()

"""
Helper Functions
"""
#
def ascend_mountain():
    while front_is_blocked():
        step_up()

def step_up():
    turn_left()
    move()
    turn_right()
    move()

def turn_right():
    for i in range(3):
        turn_left()

def descend_mountain():
    while front_is_clear():
        step_down()

def step_down():
    move()
    turn_right()
    move()
    turn_left()




if __name__ == "__main__":
    run_karel_program()