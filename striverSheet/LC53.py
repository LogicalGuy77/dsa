nums = [5,4,-1,7,8]
maxVal = nums[0]
sum = 0
ansS, ansE = 0, 0
start = 0
for i in nums:
    if sum == 0:
        start = i
    sum += i
    if sum > maxVal:
        maxVal = sum
        ansS = start
        ansE = i
    if sum<0:
        sum=0
print(maxVal, ansS, ansE)