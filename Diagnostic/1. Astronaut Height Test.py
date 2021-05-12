'''
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
'''
def main():
    a=float(input("Enter your height in meters: "))
    if a<1.6:
        print("Below minimum astronaut height")
    elif a>1.9:
        print("Above maximum astronaut height")
    else:
        print("Correct height to be an astronaut")

if __name__ == "__main__:
    main()
