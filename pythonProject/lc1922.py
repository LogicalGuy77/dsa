n = 4
mod = 10**9 + 7

def countGoodNumbers(n):
    odd = n//2
    even = n//2 + n%2
    print(even, odd)
    eCount = 5**even
    oCount = 4**odd
    ans = eCount*oCount
    print(ans%mod)

countGoodNumbers(n)