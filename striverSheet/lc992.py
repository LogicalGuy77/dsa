from typing import List
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        def atMostK(ck):
            if ck == 0:
                return 0
            l = 0
            r = 0
            freqMap = {}
            ans  = 0

            while r<len(nums):
                freqMap[nums[r]] = freqMap.get(nums[r], 0) + 1

                while len(freqMap) > ck:
                    freqMap[nums[l]] -= 1
                    if freqMap[nums[l]] == 0:
                        del freqMap[nums[l]]
                    l += 1
                
                ans += r - l + 1
                r += 1
            return ans
        
        return atMostK(k) - atMostK(k-1)


obj = Solution()
nums = [1,2,1,2,3]
k = 2
print(obj.subarraysWithKDistinct(nums, k))