nums = [3,4,5,1,2]

b = sorted(nums)
ans = None
for x in range (0, len(nums)):
    for i in range(0, len(nums)):
        if nums[i]==b[((i+x)%len(nums))]:
            ans = True
        else:
            ans = False
            break
    if ans == True:
        return ans
