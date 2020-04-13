from karel.stanfordkarel import *

def main():
    move()
    while beepers_present():
        pick_beeper()
        move()
        putBeeper()
        putBeeper()
        turn_around()
        move()
        turn_around()

    move()
    while beepers_present():
        pick_beeper()
        turn_around()
        move()
        turn_around()
        putBeeper()
        move()

    turn_around()
    move()
    turn_around()
    turn_around()
    move()
    turn_around()