nums = [3,0,1]

xor1=0
xor2=0

for i in range(0, len(nums)):
    xor2 = xor2^nums[i]
    xor1 = xor1 ^ i
xor1 = xor1^len(nums)

print((xor1^xor2))