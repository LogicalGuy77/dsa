import sys

bloomDay = [7,7,7,7,12,7,7]
m = 2
k = 3


def noOfFlowers(arr, day, k):
    bouquets = 0
    flowers = 0

    for i in arr:
        if i<=day:
            flowers+=1
            if flowers==k:
                bouquets+=1
                flowers=0
        else:
            flowers=0
    return  bouquets


n = len(bloomDay)

if m * k > n:
    print(-1)
    sys.exit(0)

low = min(bloomDay)
high = max(bloomDay)
ans = -1
while low <= high:
    mid = (low + high) // 2
    bouquets = noOfFlowers(bloomDay, mid, k)

    if bouquets < m:
        low = mid + 1
    else:
        ans = mid
        high = mid - 1

print("ans=", ans)
