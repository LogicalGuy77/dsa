import sys

nums = [1,2,3,1]



if len(nums)==1:
    print(0)
    sys.exit(0)
if nums[0]>nums[1]:
    print(0)
    sys.exit(0)
if nums[len(nums)-1]>nums[len(nums)-2]:
    print(len(nums)-1)
    sys.exit(0)

low = 0
high = len(nums)-1

while low<=high:
    mid=(low+high)//2

    if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
        print(mid)
        sys.exit(0)
    if nums[mid] > nums[mid - 1] and nums[mid] < nums[mid + 1]:
        low = mid+1
    elif nums[mid] < nums[mid - 1] and nums[mid] > nums[mid + 1]:
        high = mid-1
    else:
        high=mid-1