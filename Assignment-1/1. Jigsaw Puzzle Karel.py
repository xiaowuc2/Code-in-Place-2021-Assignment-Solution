
from karel.stanfordkarel import *
def main():
    move()
    move()
    pick_beeper()
    move()
    turn_left()
    for i in range(2):
        move()
    put_beeper()
    for i in range(2):
        turn_left()
    move()
    move()
    turn_right()
    for i in range(3):
        move()
    for i in range(2):
        turn_right()



def turn_right():
  for i in range(3):
    turn_left()
    
if __name__ == '__main__':
    run_karel_program('Puzzle.w')
