nums = [6,5,5]
count = 0

for i in nums:
    print(count)
    if count==0:
        count = 1
        ele = i
    elif i == ele:
        count+=1
    else:
        count-=1

print(ele)