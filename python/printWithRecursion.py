import sys
sys.setrecursionlimit(20000)
N = 18468


def printNoss(n, sumAll):
    # Your code here
    if n==0:
        return sumAll
    sumAll+=n**3
    return printNoss(n-1, sumAll)


print(printNoss(N, 0))