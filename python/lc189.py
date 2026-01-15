nums = [1,2]
k = 2
temp = []

end1 = (len(nums) - k) % len(nums)
start1 = k%len(nums)
print(start1)

if len(nums)==1 or k==0 or k==len(nums):
    exit(1)

for i in range(0, end1):
    temp.append(nums[i])
for i in range(end1, len(nums)):
    nums[i-end1] = nums[i]
for i in range(start1, len(nums)):
    nums[i] = temp[i-start1]


print(nums)
print(temp)