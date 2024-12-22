nums = [2, 3, -2, 4]
n = len(nums)

mini = nums[0]
maxi = nums[0]
ans = nums[0]

for i in range(1, n):
    if nums[i]<0:
        maxi, mini = mini, maxi
    maxi = max(nums[i], maxi*nums[i])
    mini = min(nums[i], mini*nums[i])

    ans = max(ans, maxi)

print(ans)