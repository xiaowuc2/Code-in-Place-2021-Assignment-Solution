from karel.stanfordkarel import *

def main():
    for i in range(7):
        if beepers_present():
            pick_beeper()
        else:
            move()

if __name__ == '__main__':
    run_karel_program('Cleanup1.w')
