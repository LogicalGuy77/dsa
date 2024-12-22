arr = [-1,1,-1,1]
n = len(arr)

target = 0

prefixSum = {0:-1}
currSum = 0
maxLen = 0

for i in range(0, n):
    currSum += arr[i]

    if currSum in prefixSum:
        maxLen = max(maxLen, i - prefixSum[currSum])
    else:
        prefixSum[currSum] = i

print(maxLen)