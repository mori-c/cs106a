from karel.stanfordkarel import *

def main():
	move()
	move()
	turn_left_down()
	move()
	turn_left()
	move()
	pick_beeper()

def turn_left_down():
	for i in range(3):
		turn_left()
	# turn_left()
	# turn_left()
	# turn_left()

if __name__ == "__main__":
	run_karel_program()