# This tells PyCharm who Karel is
from karel.stanfordkarel import *

# this program executes in a special function called main
def main():
    # Commands in the run method are executed one at a time
    move()
    pick_beeper()
    move()
    turn_left()
    move()
    # this actually means turn_right
    turn_left()
    turn_left()
    turn_left()
    move()
    put_beeper()
    move()


# This is "boilerplate" code which launches your code
# when you type "python StepUp.py" in the terminal
if __name__ == "__main__":
    run_karel_program()
