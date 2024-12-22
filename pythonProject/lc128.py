nums = [-100,-99]
if len(nums)==0:
    print(0)
k = max(nums)
l = min(nums)
c = 0
if l<0:
    c=l*-1
    hashMap = [0]*(k+c+1)
else:
    hashMap = [0]*(k+1)

for num in nums:
    hashMap[num+c] = 1

countMax = 0
count = 0
for i in hashMap:
    if i==1:
        count += 1
    else:
        count = 0
    if count>countMax:
        countMax = count

print(countMax)