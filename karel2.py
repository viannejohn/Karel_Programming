from stanfordkarel import *
from stanfordkarel import run_karel_program


def main():
    move()
    pick_beeper()
    move()
    turn_left()
    move()
    turn_right()
    move()
    put_beeper()
    move()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


if __name__ == "__main__":
    run_karel_program()
