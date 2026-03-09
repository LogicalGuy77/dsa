from typing import List
# class Solution:
#     def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
#         print(nums)

#         ans = []

#         n = len(nums)

#         for i in range(0, n):

#             for j in range((i+1)%n, n*2):
#                 if nums[j%n] > nums[i]:
#                     ans.append(nums[j%n])
#                     break
#                 if j%n == i:
#                     ans.append(-1)
#                     break

#         print(ans)

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        stack = []

        for i in range(2 * n):
            while stack and nums[stack[-1]] < nums[i % n]:
                idx = stack.pop()
                ans[idx] = nums[i % n]

            if i < n:
                stack.append(i)

        return ans




nums = [1,2,1]
obj = Solution()
obj.nextGreaterElements(nums)