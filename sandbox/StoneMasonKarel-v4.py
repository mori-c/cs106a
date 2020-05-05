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

    # pillar 1
    odd_pillar()
    # turn_left()
    # ascend_with_no_beeper()
    # descend_with_no_beeper()
    move_to_next_pillar()

    # pillar 2
    even_pillar()
    # turn_left()
    # ascend_with_starter_beeper()
    # descend_with_no_beeper()
    move_to_next_pillar()

    # pillar 3
    odd_pillar()
    # turn_left()
    # ascend_with_no_beeper()
    # descend_with_no_beeper()
    move_to_next_pillar()

    # pillar 4
    even_pillar()
    # turn_left()
    # ascend_with_starter_beeper()
    # descend_with_starter_beeper()



'''
Helper Functions
'''


# odd - pillar 1
def odd_pillar():
    turn_left()
    ascend_with_no_beeper()
    descend_with_no_beeper()

# even - pillar 2
def even_pillar():
    turn_left()
    ascend_with_starter_beeper()
    descend_with_no_beeper()

# For odd positioned pillars
# Excute if pillar has no beeper to start with, but ends with a beeper

def ascend_with_no_beeper():
    while front_is_clear():
        if no_beepers_present():
            put_beeper()
        if beepers_present():
            move()

def descend_with_starter_beeper():
    if front_is_blocked():
        turn_left()
        turn_left()
        while front_is_clear():
            move()

# For even positioned pillars
# Excute if pillar has no beeper to start with, but ends with a beeper

def ascend_with_starter_beeper():
    while front_is_clear():
        if beepers_present():
            move()
        if no_beepers_present():
            put_beeper()

def descend_with_no_beeper():
    if front_is_blocked():
        if no_beepers_present():
            put_beeper()
        turn_left()
        turn_left()
        while front_is_clear():
            move()

# other helper functions

def move_to_next_pillar():
    if front_is_blocked():
        turn_left()
        for i in range(4):
            move()






# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
