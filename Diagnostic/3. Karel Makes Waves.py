from karel.stanfordkarel import *

def main():
    for i in range(4):
        put_beeper()
        move()
        turn_left()
        put_beeper()
        move()
        put_beeper()
        turn_around()
        move()
        turn_left()
        if front_is_clear():
            move()
            move()


def turn_around():
    for i in range(2):
        turn_left()


if __name__ == "__main__":
    run_karel_program()
