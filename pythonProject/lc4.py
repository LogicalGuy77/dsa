nums1 = [1,3,4]
nums2 = [2]

n1 = len(nums1)
n2 = len(nums2)
i, j = 0, 0
count = 0
index1 = (n1+n2)//2
index2 = index1-1
ele1, ele2 = -1, -1

while i<n1 and j<n2:
    if nums1[i]<nums2[j]:
        if count==index1:
            ele1 = nums1[i]
        if count==index2:
            ele2 = nums1[i]
        count+=1
        i+=1
    else:
        if count==index1:
            ele1 = nums2[j]
        if count==index2:
            ele2 = nums2[j]
        count+=1
        j+=1

while i<n1:
    if count == index1:
        ele1 = nums1[i]
    if count == index2:
        ele2 = nums1[i]
    count += 1
    i+=1

while j<n2:
    if count == index1:
        ele1 = nums2[j]
    if count == index2:
        ele2 = nums2[j]
    count += 1
    j+=1

if (n1+n2)%2 == 1:
    print(ele1)
else:
    ans = (ele1+ele2)/2
    print(ans)