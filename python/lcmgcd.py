A, B = 6, 10


def gcd(a, b):
    maxNum = max(a, b)
    minNum = min(a, b)
    if minNum == 0:
        return maxNum
    return gcd(maxNum % minNum, minNum)


GCD = gcd(A, B)
LCM = (A * B) // GCD
myList = [LCM, GCD]

print(myList)
