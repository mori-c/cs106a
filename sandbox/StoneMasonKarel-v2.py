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

    # Excute if pillar has no beeper
    # pillar 1

    # ascend
    turn_left()

    while no_beepers_present():
        put_beeper()
        move()
        if beepers_present():
            move()
        while front_is_blocked():
            turn_left()
            turn_left()

    # descend
    while front_is_clear():
        move()

    if front_is_blocked():
        turn_left()
        for i in range(4):
            move()

    # pillar 2
    turn_left()

    while beepers_present():
        move()
        if no_beepers_present():
            put_beeper()
            while front_is_blocked():
                turn_left()
                turn_left()
        while front_is_blocked():
            turn_left()
            for i in range(4):
                move()

    # pillar 3
    turn_left()

    # ascend
    while no_beepers_present():
        put_beeper()
        move()
        if front_is_blocked():
            turn_left()
            turn_left()
        else:
            while beepers_present():
                move()

    # descend
    while front_is_clear():
        move()

    if front_is_blocked():
        turn_left()
        for i in range(4):
            move()

    # pillar 4
    turn_left()

    while front_is_clear():
        if beepers_present():
            move()
        if no_beepers_present():
            put_beeper()

    if front_is_blocked():
        turn_left()
        turn_left()
        while front_is_clear():
            move()

            # while beepers_present():
    #     move()
    #     if no_beepers_present():
    #         put_beeper()
    #     else:
    #         if front_is_blocked():
    #             turn_left()
    #             # turn_left()

    # if front_is_blocked():
    #     turn_left()
    #     while front_is_blocked():
    #         move()

'''
Helper Functions
'''








# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
