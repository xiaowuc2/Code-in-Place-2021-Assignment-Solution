from karel.stanfordkarel import *
def main():
    for i in range(20):
        put_beeper()
    move()
    for i in range(21):
        put_beeper()
    move()


def turn_right():
  for i in range(3):
    turn_left()

if __name__ == '__main__':
    run_karel_program()
