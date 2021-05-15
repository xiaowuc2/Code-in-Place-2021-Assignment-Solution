def main():
    a=[]
    i=0
    print("Enter a sequence of non-decreasing numbers.")
    g=float(input("Enter num: "))
    a. append(g)
    for i in range(100):
        c=float(input("Enter num: "))
        a.append(c)
        if a[-2]>a[-1]:
                print("Thanks for playing!")
                print("Sequence length: "+str(i+1))
                break
        else: 
            i+=1
    



if __name__ == "__main__":
    main()
