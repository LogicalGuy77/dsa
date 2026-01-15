nums = [7, 2, 5, 10, 8]
k = 2

low = max(nums)
high = sum(nums)

def noParts(arr, size):
    ctr = 1
    currSize = 0
    for i in arr:
        if currSize+i<=size:
            currSize+=i
        else:
            ctr+=1
            currSize=i
    return ctr

while low<=high:
    mid = (low+high)//2
    parts = noParts(nums, mid)

    if parts>k:
        low = mid+1
    else:
        high = mid-1

print(low)