from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ans = 0
        l = 0
        r = 0
        k = 2
        m = {}
        while r<len(fruits):
            m[fruits[r]] = m.get(fruits[r], 0) + 1

            if len(m) > k:
                m[fruits[l]] -= 1
                if m[fruits[l]] == 0:
                    del m[fruits[l]]
                l += 1
            
            if len(m) <= k:
                ans = max(ans, r-l+1)
            
            r+=1
        print(ans)


obj = Solution()
num = [1,2,1]
obj.totalFruit(num)