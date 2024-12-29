num = "35427"

n = len(num)
index = -1
for i in range(n - 1, -1, -1):
    print(num[i])
    if int(num[i]) % 2 == 1:
        index = i
        break

ans = num[:index+1]
print(ans)
