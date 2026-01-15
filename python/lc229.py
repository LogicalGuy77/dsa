nums = [3,2,3]

count1 = 0
count2 = 0
ele1 = 0
ele2 = 0
ans= []
for num in nums:
    if count1==0 and ele2!=num:
        ele1 = num
        count1 = 1
    elif count2==0 and ele1!=num:
        ele2 = num
        count2 = 1
    elif num==ele1:
        count1+=1
    elif num==ele2:
        count2+=1
    else:
        count1-=1
        count2-=1

print([ele1, ele2])
# optimal
# nums = [1,2]
# ans = []
# count = len(nums)//3
# dictionary = {}
# for element in nums:
#     if element in dictionary:
#         dictionary[element] += 1
#     else:
#         dictionary[element] = 1
#
# for ele in dictionary:
#     if dictionary[ele]>count:
#         ans.append(ele)
#
# print(ans)