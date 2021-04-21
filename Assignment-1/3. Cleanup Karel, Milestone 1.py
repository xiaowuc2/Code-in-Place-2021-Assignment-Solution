from karel.stanfordkarel import *

def main():
       if beepers_present():
           pick_beeper()

if __name__ == '__main__':
    run_karel_program('SafePickup1.w')
