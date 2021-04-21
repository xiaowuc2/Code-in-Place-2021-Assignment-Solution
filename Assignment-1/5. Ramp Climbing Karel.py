from karel.stanfordkarel import *

def main():
    for i in range(4):
        put_beeper()
        move()
        move()
        turn_left()
        move()
        turn_right()


def turn_right():
    for i in range(3):
        turn_left()

if __name__ == '__main__':
    run_karel_program('RampKarel1.w')
