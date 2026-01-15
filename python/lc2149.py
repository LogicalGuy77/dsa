nums = [3,1,-2,-5,2,-4]
n = len(nums)
arr = [0]*n

i=0
k=1
for j in range(0, n):
    if nums[j]>=0:
        arr[i] = nums[j]
        i+=2
    else:
        arr[k] = nums[j]
        k+=2

print(arr)