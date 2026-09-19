class Solution:
    def jump(self, nums: list[int]) -> int:
        l, r = 0, 0
        jumps = 0
        while r < len(nums)-1:
            maxReach = r
            for i in range(l, r+1):
                maxReach = max(maxReach, i+nums[i])

            l = r+1
            r = maxReach
            jumps += 1
        
            
        return jumps
        


nums = [2,3,1,1,4]
obj = Solution()
print(obj.jump(nums))