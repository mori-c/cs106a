from karel.stanfordkarel import *

"""
File: RhoombaKarel.py
----------------------------
Pick up all the beepers in the world.
"""

def main():
    # karel zig-zags to pick beepers up
    while front_is_clear():
        move()
        pickup_beepers_eastbound()
        pickup_beepers_westbound()
        turn_around()

'''
Helper Functions
'''
# pre: karel is at the being of row that could have beepers ahead going eastbound
# post: karel is at the end of the row and turned around ready for the next row (westbound)
def pickup_beepers_eastbound():
    while facing_east():
        if beepers_present():
            pick_beeper()
        else:
            move()
        east_to_west_turnaround()

# pre: karel is at the being of row that could have beepers ahead going westbound
# post: karel is at the end of the row and turned around ready for the next row (eastbound)
def pickup_beepers_westbound():
    while facing_west():
        if beepers_present():
            pick_beeper()
        else:
            move()
        west_to_east_turnaround()

# pre: karel is on the eastbound edge
# post: karel moved up, ready to head westbound
def east_to_west_turnaround():
    while front_is_blocked():
        safe_pick()
        turn_left()
        move()
        safe_pick()
        turn_left()

# pre: karel is on the westbound edge
# post: karel moved up, ready to head eastbound
def west_to_east_turnaround():
    while front_is_blocked():
        safe_pick()
        turn_around()
        safe_pick()

# pick up, but only if there is a beeper
def safe_pick():
    if beepers_present():
        pick_beeper()

def turn_around():
    for i in range(3):
        turn_left()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
