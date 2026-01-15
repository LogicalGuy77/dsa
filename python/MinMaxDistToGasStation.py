arr = [1,2,3,4,5,6,7]
k = 6

n = len(arr)
hasPlaced = [0]*(n-1)

# placing gas stations one by one
for i in range(0, k):
    maxVal = -1
    maxIndex = -1

    for i in range(0, n-1):
        diff = arr[i+1]-arr[i]
        secLen = diff / (hasPlaced[i]+1)

        if secLen>maxVal:
            maxVal=secLen
            maxIndex=i
    hasPlaced[maxIndex]+=1

maxAns = -1
for i in range(0, n-1):
    diff = arr[i+1]-arr[i]
    secLen =  diff / (hasPlaced[i]+1)

    maxAns = max(maxAns, secLen)

print(maxAns)



