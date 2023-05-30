from stanfordkarel import *
from stanfordkarel import run_karel_program


def main():
    move_2()
    turn_right()
    move_2()
    put_beeper()
    turn_right_2()
    move_7()
    put_beeper()
    turn_left()
    move_7()
    put_beeper()
    turn_left()
    move_7()
    put_beeper()
    turn_left()
    move_7()
    # turn_left()
    # move_2()
    # turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()
    # for i in range(3):
    #     turn_left()


def turn_right_2():
    turn_right()
    turn_right()


def move_2():
    move()
    move()


def move_7():
    move()
    move()
    move()
    move()
    move()
    move()
    move()


def move_9():
    move()
    move()
    move()
    move()
    move()
    move()
    move()
    move()
    move()


if __name__ == "__main__":
    run_karel_program()
