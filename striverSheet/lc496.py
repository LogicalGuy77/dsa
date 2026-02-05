from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = []
        mp = {}

        for i in range(0, len(nums2)):
            while len(s)!=0 and nums2[i] > s[-1]:
                x = s.pop()
                mp[x] = nums2[i]
            s.append(nums2[i])

        # remaining elements have no geater ele
        while len(s)!=0:
            mp[s.pop()] = -1
        
        res = []

        for i in range(0, len(nums1)):
            res.append(mp[nums1[i]])
        
        return res




obj = Solution()
nums1 = [2,4]
nums2 = [1,2,3,4]
print(obj.nextGreaterElement(nums1, nums2))