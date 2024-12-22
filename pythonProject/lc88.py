nums1 = [1]
m = 1
nums2 = []
n = 0

for i in range(0, m):
    if nums1[i] <= nums2[0]:
        continue
    else:
        temp = nums1[i]
        nums1[i] = nums2[0]
        nums2[0] = temp
        nums2.sort()

for i in range(0, n):
    nums1[i+m] = nums2[i]

print(nums1)
