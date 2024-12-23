position = [1,2,3,4,7]
m = 3

def canPlace(arr, dist, balls):
    ballsPlaced = 1
    lastPlaced = arr[0]

    for i in range(1, len(arr)):
        if arr[i]-lastPlaced >= dist:
            ballsPlaced+=1
            lastPlaced = arr[i]
        if ballsPlaced>=balls:
            return True
    return False

n = len(position)
position.sort()
low = 1
high = position[n-1]-position[0]

while low<=high:
    mid = (low+high)//2

    if canPlace(position, mid, m):
        low = mid+1
    else:
        high = mid-1
print(high)