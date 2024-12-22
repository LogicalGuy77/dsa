nums = [3,3]
target = 6

numDict = {}

for i in range(0, len(nums)):
    diff = target - nums[i]
    j = numDict.get(diff, -1)
    if j!=-1:
        print(j,i)
    numDict[nums[i]] = i

print(numDict)