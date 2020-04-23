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
    fencepost_bldg_one()			# fencepost around first building
    fencepost_bldg_two()			# fencepost around second building
    fencepost_bldg_three()		# fencepost around third building

"""
Helper Functions
"""
# fencepost around first building
def fencepost_bldg_one():
    horizontal_fencepost()
    corner_move()
    vertical_fencepost()
    corner_move()
    horizontal_fencepost()

# fencepost around second building
def fencepost_bldg_two():
	turn_right()
	for i in range(2):
		vertical_fencepost()
		corner_move()
	# vertical_fencepost()
	# corner_move()
	horizontal_fencepost()

# fencepost around third building
def fencepost_bldg_three():
	turn_right()
	vertical_two_fencepost()
	corner_move()
	vertical_fencepost()
	corner_move()
	vertical_two_fencepost()


def vertical_fencepost():
		for i in range(3):
				put_beeper()
				move()


def vertical_two_fencepost():
		for i in range(2):
			put_beeper()
			move()


def horizontal_fencepost():
		while front_is_clear():
				put_beeper()
				move()


def corner_move():
		turn_left()
		move()


# turn karel around to origin direction
def turn_right():
    for i in range(3):
        turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
