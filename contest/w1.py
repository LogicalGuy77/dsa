def is_strictly_increasing(start: int, end: int) -> bool:
    for i in range(start, end - 1):
        if nums[i] >= nums[i + 1]:
            return False
    return True

n = len(nums)

for i in range(n - 2 * k + 1):
    if is_strictly_increasing(i, i + k):
        if is_strictly_increasing(i + k, i + 2 * k):
            return True

return False