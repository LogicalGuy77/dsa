from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapFreq = {}
        freq = [[] for i in range(len(nums)+1)]

        for i in nums:
            mapFreq[i] = mapFreq.get(i, 0) + 1

        for n,c in mapFreq.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


obj = Solution()
nums = [1,1,1,2,2,2,2,3]
k = 2
print(obj.topKFrequent(nums, k))