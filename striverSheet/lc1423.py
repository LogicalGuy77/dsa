from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        l = 0
        r = 0
        ans = 0
        maxPoints = sum(cardPoints)

        if k == len(cardPoints):
            return maxPoints
        sumCurrWindow = 0
        mapPrefixSum = []
        while r < len(cardPoints):
            previous_sum = mapPrefixSum[r - 1] if r > 0 else 0
            mapPrefixSum.append(previous_sum + cardPoints[r])

            while len(cardPoints) - k < r-l+1 and l<r:
                l += 1
            
            if len(cardPoints) - k == r-l+1:
                if l == 0:
                    ans = max(ans, maxPoints - (mapPrefixSum[r]))
                else:
                    ans = max(ans, maxPoints - (mapPrefixSum[r]-mapPrefixSum[l-1]))
            r += 1
        
        print(ans)

            


obj = Solution()
cardPoints = [9,7,7,9,7,7,9]
k = 5
obj.maxScore(cardPoints, k)
