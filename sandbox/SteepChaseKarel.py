from karel.stanfordkarel import *

"""
let's have karel do hurel jumps while moving forward
do one steeple at a time
- ascend_hurdle()
- descend_hurdle()

"""
def main():
	for i in range(8):
		if front_is_clear():
			move()
		else: # front_is_not_clear
			jump hurdle()

# helper functions ----------------------------------

# karel does jumping
def jump_hurdle():
	ascend_hurdle()
	move()
	descend_hurdle()

# karel goes up
def ascend_hurdle():
	turn_left()
	while right_is_blocked():
		move()
	turn_right()

def right_is_blocked():
	pass

# karel turns back into neural position
def turn_right():
	for i in range(3):
		turn_left()

# karel does down
def descend_hurdle():
	turn_right()
	move_to_wall()
	turn_left()


def move_to_wall():
	while front_is_clear():
		move


if __name__ == '__main__':
	run_karel_program()
