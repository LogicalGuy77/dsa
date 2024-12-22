arr = [16, 17, 4, 3, 5, 2]
currMax = [arr[-1]]
maxNum = arr[-1]

for i in range(len(arr)-2, -1, -1):
    maxNum = max(maxNum, arr[i])
    if arr[i] == maxNum:
        currMax.insert(0, arr[i])

print(currMax)