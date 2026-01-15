arr = [1, 4, 3, 3, 5, 5]
n = 6
k = 16

currSum = 0
prefixSum = {0: 0}
maxLen = 0

for i in range(0, n):
    currSum += arr[i]
    diff = currSum - k

    index = prefixSum.get(diff, -1)
    if index!=-1:
        maxLen = max(maxLen, i-index+1)
    if prefixSum.get(currSum, -1) == -1:
        prefixSum[currSum] = i+1

print(maxLen)
