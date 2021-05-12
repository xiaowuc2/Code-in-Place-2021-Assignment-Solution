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
