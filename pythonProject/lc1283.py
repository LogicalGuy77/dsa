import math
import sys

nums = [1, 2, 5, 9]
threshold = 6


def summ(arr, divisor):
    sum = 0
    for i in arr:
        sum += math.ceil(i / divisor)
    return sum


n = len(nums)
low = min(nums)
high = max(nums)
ans = -1
while low <= high:
    mid = (low + high) // 2
    s = summ(nums, mid)

    if s>threshold:
        low = mid+1
    else:
        ans = mid
        high = mid-1

print("ans=", ans)
