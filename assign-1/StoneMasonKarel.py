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

    # ascend
    turn_left()

    while no_beepers_present():
        put_beeper()
        move()
        while beepers_present():
            move()

    # turn around
    turn_left()
    turn_left()

    # descend
    while front_is_clear():
        move()


    # to next pillar
    while front_is_blocked():
        turn_left()
        for i in range(4):
            move()

    # ascend
    turn_left()

    while beepers_present():
        move()
        if no_beepers_present():
            put_beeper()
            move()

    # turn around
    turn_around()

    # descend


'''
Helper Functions
'''

def turn_around():
    for i in range(2):
        turn_left()
    move()






# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
