### Code in Place 2021 Diagnostic Solution
```
If this repository helped you please give a star ⭐ and encourage me to solve other problems too.
``` 

Video Explanation : https://youtu.be/u8uqTBNZvAY

<p align="center">
  <a href="https://youtu.be/0IURrcpNZmk">
    <img src="https://github.com/xiaowuc2/xiaowuc2/blob/master/source/ranger-1/youtube%20diagnostic.png" alt="Logo">
  </a>

  <h3 align="center">by @xiaowuc2</h3>

  <p align="center">
  </p>
</p>


- [Astronaut Height Test](https://github.com/xiaowuc2/Code-in-Place-2021-Assignment-Solution/blob/main/Diagnostic/1.%20Astronaut%20Height%20Test.py)
```
  Write a program which asks the user for their height in meters and prints whether or not they are the correct height to be a NASA astronaut.
  If their height is between 1.6 meters and 1.9 meters, print "Correct height to be an astronaut".
  If their height is less than 1.6 meters, print "Below minimum astronaut height".
  If their height is greater than 1.9 meters, print "Above maximum astronaut height".

  Here are a few examples. User input is bolded and italicized for clarity, but it doesn't need to be in your program:

  Enter your height in meters: 1.75
  Correct height to be an astronaut
  Enter your height in meters: 2.0
  Above maximum astronaut height
  Enter your height in meters: 1.6
  Correct height to be an astronaut
  Enter your height in meters: 1.0
  Below minimum astronaut height
  You may assume that the user enters a valid input (a non-negative number). Each time the program is run, the user is asked for their height only once. 

  Aside: If you are not the right height to be an astronaut, that is fine! Space is dangerous anyways. Chris is not the right height, but found a happy alternative job here on earth 🌱. 
```
- [Even Odd Table](https://github.com/xiaowuc2/Code-in-Place-2021-Assignment-Solution/blob/main/Diagnostic/2.%20Even%20Odd%20Table.py)
```
Print out each of the numbers 1 through 100 and whether that number is even or odd. 

100 is specified using a constant MAX_NUMBER. 

Here is what the output looks like when MAX_NUMBER = 100

```

- [Karel Makes Waves](https://github.com/xiaowuc2/Code-in-Place-2021-Assignment-Solution/blob/main/Diagnostic/3.%20Karel%20Makes%20Waves.py)
```
Write a program that has Karel draw four small "waves". Each wave is a triangle made up of three beepers. There is a gap between each wave.

This is the state of Karel's world when Karel starts:

Karel is in an empty world which is 11 corners wide and 5 corners tall. Karel is on the first row, first column, facing east
This is state of Karel's world when Karel has finished making waves!

karel is on the first row, last column, facing east. The world has four waves. Each wave is made up of a column with one beeper, followed by a column of two beepers. There is a blank corner between each of the waves.

A few notes
Karel always begins at the bottom left corner of the world, facing East

Karel's bag has infinite beepers.

It does not matter which direction Karel ends up facing.

You may assume that the world is always exactly 11 columns wide and 5 columns tall. Your program only needs to work for this sized world.

We've provided you implementations of the turn_right and turn_around functions, although you aren't required to use either of them.

You must not use any non-Karel features like variables, return or break. You may use any Karel features described in the course reader.
```
- [Nondecreasing](https://github.com/xiaowuc2/Code-in-Place-2021-Assignment-Solution/blob/main/Diagnostic/4.%20Nondecreasing.py)

```
A simple way to achieve great things in life is to make small forward progress every day. Non-decreasing progress is one of the principles behind modern AI.

Write a program that asks the user to enter a sequence of "non-decreasing" numbers one at a time. Numbers are non-decreasing if each number is greater than or equal to the last.

When the user enters a number which is smaller than their previously entered value, the program is over. Tell the user how long their sequence was.

Here is an example (values entered by the user are bolded and italicized for clarity, but they don't need to be in your program):

Enter a sequence of non-decreasing numbers.
Enter num: -1
Enter num: 0
Enter num: 1
Enter num: 3.12
Enter num: 99
Enter num: 99
Enter num: 42
Thanks for playing!
Sequence length: 6


A few notes:
Include the intro message, Enter a sequence of non-decreasing numbers.

Include the exit message, Thanks for playing!.

Include the exit message, Sequence length: followed by the length of the sequence.

The length of the sequence does not include the very last number entered as it is "decreasing"

Your program should accept floating point numbers.

The sequence only ends when one number is strictly less than the last.

You do not have to handle the case where the user enters a value which is not a number (say "abc").

The user can start with any number, positive or negative.

Note that the shortest possible sequence is 1. A sequence with a single number can't be decreasing. A sequence with two numbers can be decreasing.

More examples:
Enter a sequence of non-decreasing numbers.
Enter num: 5
Enter num: 4
Thanks for playing!
Sequence length: 1
Enter a sequence of non-decreasing numbers.
Enter num: 1
Enter num: 2.7
Enter num: 3
Enter num: 4
Enter num: 2
Thanks for playing!
Sequence length: 4

Enter a sequence of non-decreasing numbers.
Enter num: -5
Enter num: -5
Enter num: -5
Enter num: -6
Thanks for playing!
Sequence length: 3
```
- [Debugging & Tracing](https://github.com/xiaowuc2/Code-in-Place-2021-Assignment-Solution/blob/main/Diagnostic/5.%20Debugging%20%26%20Tracing.py)

```
Consider the following buggy code: 
def divide_and_round(n):
    """
    Divides an integer n by 2 and rounds 
    up to the nearest whole number
    """
    if n % 2 == 0:
        n = n / 2
    else:
        n = (n + 1) / 2

def main():
    n = 10
    divide_and_round(n)
    print(n)  # should print 5

if __name__ == "__main__":
    main()

def divide_and_round(n):
    """
    Divides an integer n by 2 and rounds 
    up to the nearest whole number
    """
    if n % 2 == 0:
        n = n / 2
    else:
        n = (n + 1) / 2



Part A
What will be printed at the end of this program? Why?

Part B
How can this program be fixed so that it does what it is meant to? You can make changes to both divide_and_round and main, but divide_and_round must implement the functionality described in its comment for all possible values of its parameter. You should write a fixed version of the program with comments indicating each line you changed.
```
