from typing import List
class Solution:
    def numSubarrayWithSum(self, nums: List[int], goal: int) -> int:
        sol = self.lessThanEqualGoal(nums, goal) - self.lessThanEqualGoal(nums, goal-1)
        return sol
    
    def lessThanEqualGoal(self, n: List[int], goal: int) -> int:
        l = 0
        r = 0
        s = 0
        count = 0
        if goal < 0:
            return 0
        while r < len(nums):
            s += nums[r]

            while s > goal:
                s -= nums[l]
                l += 1
            
            count += (r - l + 1)
            r += 1
        return count        


obj = Solution()
nums = [1,0,1,0,1]
goal = 2
print(obj.numSubarrayWithSum(nums, goal))