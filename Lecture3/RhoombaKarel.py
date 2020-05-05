from karel.stanfordkarel import *

"""
File: RhoombaKarel.py
----------------------------
Pick up all the beepers in the world.
"""

def main():
    while front_is_clear():
        move()
        pickup_beepers_eastbound()
        pickup_beepers_westbound()
        for i in range(3):
            turn_left()

    if front_is_blocked():
        while facing_north():
            turn_left()

'''
Helper Functions
'''

def pickup_beepers_eastbound():
    while facing_east():
        if beepers_present():
            pick_beeper()
        else:
            move()
        while front_is_blocked():
            if beepers_present():
                pick_beeper()
            turn_left()
            move()
            turn_left()
        if beepers_present():
            pick_beeper()
    # while facing_east():
    #     if beepers_present():
    #         pick_beeper()
    #     else:
    #         move()
    #     while front_is_blocked():
    #         if beepers_present():
    #             pick_beeper()
    #         turn_left()
    #         move()
    #         turn_left()

def pickup_beepers_westbound():
    while facing_west():
        if beepers_present():
            pick_beeper()
        else:
            move()
        while front_is_blocked():
            if beepers_present():
                pick_beeper()
            for i in range(3):
                turn_left()
            if beepers_present():
                pick_beeper()
    # while facing_west():
    #     if beepers_present():
    #         pick_beeper()
    #     else:
    #         move()
    #     while front_is_blocked():
    #         if beepers_present():
    #             pick_beeper()
    #         for i in range(3):
    #             turn_left()
    #         move()
    #         for i in range(3):
    #             turn_left()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
