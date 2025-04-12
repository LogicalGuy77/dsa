word = "amrvxnhsewkoipjyuclgtdbfq"
n = len(word)
keys = 8

ans = 0

if n <= keys:
    ans = n

if keys < n <= keys*2:
    ans = 8 + (n-8)*2

if keys*2 < n <= keys*3:
    ans = 8 + 16 + (n-16)*3

if keys*3 < n:
    ans = 8 + 16 + 24 + (n-24)*4

print(ans)
