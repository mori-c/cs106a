from karel.stanfordkarel import *

"""
File: TripleKarel.py
--------------------
When you finish writing this file, TripleKarel should be
able to paint the exterior of three buildings in a given
world, as described in the Assignment 1 handout. You
should make sure that your program works for all of the 
Triple sample worlds supplied in the starter folder.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """

    # building one
    for i in range(3):
        fencepost()
    turn_left()

    # building two
    for i in range(4):
        fencepost()
    back_into_postion()

    # building three
    for i in range(3):
        fencepost()
    back_into_postion()
    turn_left()

'''
Helper Functions
'''
# put beepers against current line and move around corner
def fencepost():
    while left_is_blocked():
        half_turn()
        put_beeper()
        half_turn()
        move()
    if left_is_clear():
        turn_left()
        move()

# reposition karel ready for fenceposting
def back_into_postion():
    half_turn()
    move()

def half_turn():
    turn_left()
    turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
