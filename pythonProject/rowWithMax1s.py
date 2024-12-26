arr = [[0,1,1,1], [0,0,1,1], [1,1,1,1], [0,0,0,0]]

n = len(arr)
m = len(arr[0])
ans = 0
index = -1
for i in range(0, n):
    low = 0
    high = m - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[i][mid] == 0:
            low = mid + 1
        else:
            high = mid - 1
    if m-low>ans:
        index = i
    ans = max(ans, m - low)

print(ans, index)