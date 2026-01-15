stalls = [0, 3, 4, 7, 10, 9]
k = 4

def canPlace(arr, dist, cows):
    cowPlaced = 1
    lastPlaced = arr[0]

    for i in range(1, len(arr)):
        if arr[i]-lastPlaced >= dist:
            cowPlaced+=1
            lastPlaced = arr[i]
        if cowPlaced >= cows:
            return True
    return False

stalls.sort()
n = len(stalls)
low = 1
high = stalls[n-1]-stalls[0]

while low<=high:
    mid = (low+high)//2

    if canPlace(stalls, mid, k)==True:
        low = mid+1
    else:
        high = mid-1
print(high)