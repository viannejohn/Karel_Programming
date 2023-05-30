from stanfordkarel import *


def main():
    turn_left()
    beeper_removal_movement()

    turn_left()
    space_movement()
    turn_left()
    beeper_removal_movement()

    turn_right()
    space_movement()
    turn_right()
    beeper_removal_movement()

    turn_left()
    space_movement()

    turn_left()
    beeper_removal_movement()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def beeper_removal_movement():
    while front_is_clear():  # while loop to check if there is space for movement and no obstacles
        if beepers_present():  # if function to pick beepers if present
            pick_beeper()
        move()
    if beepers_present():   # checks if beepers present after an obstacle is met and picks
        pick_beeper()


def space_movement():
    for i in range(4):  # moves four times in the direction the beeper is facing
        move()


if __name__ == "__main__":
    run_karel_program()
