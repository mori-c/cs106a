from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should 
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """

    # ascent
    turn_left()
    # while front_is_clear():
    #     put_beeper()
    #     move()
    #     if beepers_present():
    #         move()

    while no_beepers_present():
        put_beeper()
        move()
        if beepers_present():
            move()
    #         # while front_is_blocked():
    #         #     move()

    # turn around
    turn_left()
    turn_left()

    # descend
    while front_is_clear():
        move()
    turn_left()

    # to next pillar
    for i in range(4):
        move()

    # ascend
    turn_left()
    # while front_is_clear():
    # # while no_beepers_present():
    #     put_beeper()
    #     move()
    #     if beepers_present():
    #         move()
    while no_beepers_present():
        put_beeper()
        move()
        if beepers_present():
            move()




# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
