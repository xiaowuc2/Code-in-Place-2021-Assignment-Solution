from karel.stanfordkarel import *

def main():
    while front_is_clear():
        if beepers_present():
            pick_beeper()
        else:
            move()
    pick_beeper()

if __name__ == '__main__':
    run_karel_program('Cleanup1.w')
