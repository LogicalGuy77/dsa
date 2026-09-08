from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def lessEqual(goal):
            if goal < 0:
                return 0
            l = 0
            r = 0
            count = 0
            subArr = 0
            while r < len(nums):
                if nums[r]%2 == 1:
                    count += 1
                
                while count > goal and l<=r:
                    if nums[l]%2  == 1:
                        count -= 1
                    l += 1
                
                subArr += r - l +  1
                r += 1
            return subArr
        
        a1 = lessEqual(k)
        print(a1)
        a2 = lessEqual(k-1)
        print(a2)
        return  a1- a2


nums = [45627,50891,94884,11286,35337,46414,62029,20247,72789,89158,54203,79628,25920,16832,47469,80909]
k = 1
obj = Solution()
print(obj.numberOfSubarrays(nums, k))