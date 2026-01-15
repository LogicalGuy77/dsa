x = 2.000
n = -2

def myPow(x, n):
    def helper(x, n):
        if x == 0:
            return 0
        if n == 0:
            return 1

        res = helper(x, n//2)
        res = res*res

        return x*res if n%2!=0 else res


    ok = helper(x, abs(n))
    if n<0:
        return 1/ok
    else:
        return ok


ans = myPow(x, n)
print(ans)