N = 54
a = []


def fact(n, k, factorial):
    if factorial <= n:
        a.append(factorial)
        k+=1
        fact(n, k, factorial*k)
    return a


ans = fact(N, 1, 1)
print(ans)
