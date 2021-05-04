"""
If you're up for it, we can make Khansole Academy an even better learning tool. Be creative! We recommend you start with the "three in a row" extension first, 
then come up with your own :-).

Three in a row

In the previous milestone you wrote code to randomly generate one addition problem at a time and tell the user if they got it right or not. In this milestone, 
you should randomly generate addition problems until the user has gotten 3 problems correct in a row. (Note: the number of problems the user needs to get correctly 
in a row to complete the program is just one example of a good place to specify a constant in your program).

You should be able to use a lot of your code from the previous milestone to help out here!

A sample run of the program is shown below (user input is in bold italics).

$ python khansole_academy.py
What is 51 + 79?
Your answer: 120
Incorrect. The expected answer is 130
What is 33 + 19?
Your answer: 42
Incorrect. The expected answer is 52
What is 55 + 11?
Your answer: 66
Correct! You've gotten 1 correct in a row.
What is 84 + 25?
Your answer: 109
Correct! You've gotten 2 correct in a row.
What is 26 + 58?
Your answer: 74
Incorrect. The expected answer is 84
What is 98 + 85?
Your answer: 183
Correct! You've gotten 1 correct in a row.
What is 79 + 66?
Your answer: 145
Correct! You've gotten 2 correct in a row.
What is 97 + 20?
Your answer: 117
Correct! You've gotten 3 correct in a row.
Congratulations! You mastered addition.
"""

import random 

def main():
    k=0
    a=random.randint(10,99)
    b=random.randint(10,99)
    while k!=3: 
        print("What is "+str(a)+" + "+str(b)+"?")
        g=int(input("Your answer: "))
        if g==a+b:
            k=k+1
            print("Correct! You've gotten " +str(k)+ " correct in a row.")
        else:
            k=k-1
            print("Incorrect. The expected answer is "+str(a+b))
    print("Congratulations! You mastered addition.")
    


if __name__ == '__main__':
    main()
