from typing import List
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        stk = deque()
        ans = []

        for i in range(0, n):
            while stk and stk[0]<i-k+1:
                stk.popleft()
            
            while stk and nums[stk[-1]] < nums[i]:
                stk.pop()
            
            stk.append(i)

            if i>=k-1:
                ans.append(nums[stk[0]])
        return ans



        


nums = [1,3,-1,-3,5,3,6,7]
k = 3
obj = Solution()
print(obj.maxSlidingWindow(nums, k))