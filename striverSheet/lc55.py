class Solution:
    def canJump(self, nums: list[int]) -> bool:
        maxIndx = 0
        for i in range(0, len(nums)):
            if i > maxIndx:
                return False
            maxIndx = max(maxIndx, i + nums[i])

        return True



nums = [3,2,1,0,4]
obj = Solution()
print(obj.canJump(nums))