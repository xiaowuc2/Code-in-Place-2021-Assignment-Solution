"""
Part A:
10, because hte program is buggy.
"""

"""
Part B: 
Edit this code so that it works correctly
"""
def divide_and_round(n):
    """
    Divides an integer n by 2 and rounds 
    up to the nearest whole number
    """
    print("4")
    if n % 2 == 0:
        n = n / 2
        return int(n)
    else:
        n = (n + 1) / 2
        return int(n)

def main():
    n = 10
    print(divide_and_round(n))  # should print 5

if __name__ == "__main__":
    main()
