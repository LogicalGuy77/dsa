A = [4, 2, 2, 6, 4]
B = 6
ans = 0
n = len(A)

xorA = 0
prefixXor = {0: 1}

for i in range(0, n):
    xorA = xorA ^ A[i]
    x = xorA ^ B

    ans += prefixXor.get(x, 0)

    if xorA not in prefixXor:
        prefixXor[xorA] = 1
    else:
        prefixXor[xorA] += 1

print(ans)
