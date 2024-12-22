nums = [2,0,2,1,1,0]
zero = 0
one = 0
two = 0
for i in nums:
    if i == 0:
        zero += 1
    elif i == 1:
        one += 1
    else:
        two += 1
for i in range(0, zero):
    nums[i] = 0
for i in range(zero, zero+one):
    nums[i] = 1
for i in range(zero+one, zero+one+two):
    nums[i] = 2

print(nums)
print(zero, one , two)