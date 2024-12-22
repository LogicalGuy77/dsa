import math

nums = [-1,-4,3,-5,-6]

ans = 0
i = 0
j = 2
while j<len(nums):

    if (nums[i] + nums[j]) == (nums[i+1] / 2):
        print("nums[i] = ", nums[i])
        print("nums[i+1] = ", nums[i+1])
        print("nums[j] = ", nums[j])
        print("math.floor(nums[i+1] / 2 = ", (nums[i+1] / 2))
        ans += 1
    i+=1
    j+=1


print(ans)