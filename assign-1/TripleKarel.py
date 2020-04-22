from karel.stanfordkarel import *

def main():
    while front_is_clear():
        put_beeper()
        move()
    turn_ninety()

def fencepost():
    while front_is_clear():
        put_beeper()
        move()

def turn_ninety():
    for i in range(1):
        turn_left()
        move()

if __name__ == '__main__':
    run_karel_program()