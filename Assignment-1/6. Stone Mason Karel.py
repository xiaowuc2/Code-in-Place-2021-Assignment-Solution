from karel.stanfordkarel import *

def main():
    while front_is_clear():
        turn_left()
        while front_is_clear():
            if no_beepers_present():
                put_beeper()
            move()
        if no_beepers_present():
            put_beeper()
        turn_right()
        turn_right()
        while front_is_clear():
            move()
        turn_left()
        if front_is_clear():
            for i in range(4):
                   move()
    turn_left()
    while front_is_clear():
        if no_beepers_present():
                put_beeper()
        move()
    turn_right()


def turn_right():
    for i in range(3):
        turn_left()



if __name__ == '__main__':
    run_karel_program('SampleQuad3.w')
