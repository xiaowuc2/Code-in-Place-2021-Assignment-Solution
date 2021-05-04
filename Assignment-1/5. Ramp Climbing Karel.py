from karel.stanfordkarel import *

def main():
    while front_is_clear():
        put_beeper()
        move()
        move()
        turn_left()
        move()
        turn_right()
    put_beeper()


def turn_right():
    for i in range(3):
        turn_left()

if __name__ == '__main__':
    run_karel_program('RampKarel1.w')

    
