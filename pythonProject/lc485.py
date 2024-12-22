nums = [1,1,0,1,1,1]
maax, curr = 0, 0
i = 0
while i < len(nums):
    print(i)
    if nums[i] == 1:
        curr += 1
        i += 1
        if curr > maax:
            maax = curr
        continue
    curr = 0
    i += 1
print(maax)