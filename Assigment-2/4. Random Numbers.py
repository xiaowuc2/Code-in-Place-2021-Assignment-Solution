"""
Write a program in the file random_numbers.py that prints 10 random integers (each random integer should have a value between 0 and 100, inclusive).

Your program should use a constant named NUM_RANDOM, which determines the number of random numbers to print (with a value of 10).

It should also use constants named MIN_RANDOM and MAX_RANDOM to determine the minimal and maximal values of the random numbers generated (with respective values 0 and 100).

To generate random numbers, you should use the function random.randint() from Python’s random library.

Here's a sample run of the program:

$ python random_numbers.py
35
10
45
59
45
100
8
31
48
6
"""

import random
NUM_RANDOM=10
MIN_RANDOM=0
MAX_RANDOM=100
def main():
    NUM_RANDOM=0
    for i in range(10):
        print(random.randint(MIN_RANDOM,MAX_RANDOM))

if __name__ == '__main__':
    main()
