nums = [2,1,5,4,3,0,0]
n = len(nums)

index = -1

for i in range(n-2, -1, -1):
    if nums[i]<nums[i+1]:
        index = i
        break
if index == -1:
    print(nums[::-1])

for i in range(n-1, index-1, -1):
    if nums[i]>nums[index]:
        temp = nums[i]
        nums[i] = nums[index]
        nums[index] = temp
        break

s = index+1
e = n-1

while s<e:
    temp = nums[s]
    nums[s] = nums[e]
    nums[e] = temp
    s+=1
    e-=1

print(nums)
