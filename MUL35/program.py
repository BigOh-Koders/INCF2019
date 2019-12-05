"""
Problem Statement:

If we list all the natural number below 20 that are multiples of 3 or 5,
we get 3,5,6,9,10,12,15,18. The sum if these multiples is 78.

Find the sum of all the multiples of 3 or 5 below N.

"""

def SumDivisibleBy35(n,target):
    """
    Returns the sum of all the multiples of 3 or 5 below N

    """
    if target > 0:
        p = target // n
        return (n*(p*(p+1))) // 2
    else:
        return 0

if __name__ == "__main__":
    test = int(input())
    while test:
        N = int(input()) 
        target = N-1
        print(SumDivisibleBy35(3,target) + SumDivisibleBy35(5,target) - SumDivisibleBy35(15,target))
        test = test - 1