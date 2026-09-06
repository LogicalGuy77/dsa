from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        print(nums)
        msize = 0
        left = 0
        zero_c = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                zero_c += 1

            while zero_c > k:
                if nums[left] == 0:
                    zero_c -= 1
                left += 1
                
            
            msize = max(msize, r-left+1)
        
        print(msize)









nums = [1,1,1,0,0,0,1,1,1,1,0]
obj = Solution()
obj.longestOnes(nums, 2)