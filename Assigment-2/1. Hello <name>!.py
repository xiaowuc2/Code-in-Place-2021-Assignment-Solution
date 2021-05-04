"""
Write a customizable version of the classic "hello world!" program in hello.py which, instead of saying "hello world!", 
prompts the user for their name and then says hello to them! An example run of the program is as follows (user input is in bold italics):

$ python hello.py
What is your name? Karel 
Hello Karel!

"""

def main():
    a=input("What is your name? ")
    print("Hello "+a+"!")
    
if __name__ == '__main__':
    main()
