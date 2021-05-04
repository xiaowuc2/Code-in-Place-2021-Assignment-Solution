"""
Add one line of code in madlibs.py to complete the story of Karel the Omniscient (and build your understanding of Python)!

Mad Libs is a word game where players are prompted for one word at a time, and the words are eventually filled into the blanks of a word template to make an entertaining story! In the starter code we've provided most of a short story, with constants WIZARD, NUMBER_OF, FRUIT, PRICE, and YEARS interspersed throughout! Start by taking a close look at the starter code and running it as is to see how the story goes so far. Notice that if you change the value of, say, the WIZARD constant at the top and rerun the program, it'll change throughout the story! 

Your job is to finish writing the last line of this story, which should go like this (recall that YEARS = 300 and WIZARD = 'Karel the Omniscient'; you should use both these constants in your line of code):

Legend says 300 years later, Karel the Omniscient is still eating fruit.
The full story should read:

There once was a wizard by the name of Karel the Omniscient who loved to eat mangoes.
Karel the Omniscient always kept a stash of 6174 mangoes in their mini fridge!
Karel the Omniscient realized they couldn't keep all those mangoes to themselves, 
so they sold them at the market for $2.99 apiece, 
and with the earnings bought fruit to share with the entire village!
Legend says 300 years later, Karel the Omniscient is still eating fruit.

Please press submit on your code once your story looks like the above!!

To verify that you've used constants correctly, if you change the values of the constants as follows:

WIZARD = "Merlin"
NUMBER_OF = 28
FRUIT = "durian"
PRICE = 1.55
YEARS = 100
The story should now read:

There once was a wizard by the name of Merlin who loved to eat durian.
Merlin always kept a stash of 28 durian in their mini fridge!
Merlin realized they couldn't keep all those durian to themselves,
so they sold them at the market for $1.55 apiece,
and with the earnings bought fruit to share with the entire village!
Legend says 100 years later, Merlin is still eating fruit.
"""

WIZARD = 'Merlin'
NUMBER_OF = 28
FRUIT = 'durian'
PRICE = 1.55
YEARS = 100

def main():
    print("There once was a wizard by the name of " + WIZARD + " who loved to eat " + FRUIT + ".")
    print(WIZARD + " always kept a stash of " + str(NUMBER_OF) + " " + FRUIT + " in their mini fridge!")
    print(WIZARD + " realized they couldn't keep all those " + FRUIT + " to themselves,")
    print("so they sold them at the market for $" + str(PRICE) + " apiece,")
    print("and with the earnings bought fruit to share with the entire village!")
    print("Legend says " + str(YEARS)+ " years later, " +str(WIZARD)+ " is still eating fruit.")

if __name__ == '__main__':
    main()
