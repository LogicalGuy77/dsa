class Solution:
    def kDistinctChar(self, s, k):
        r = 0
        l = 0
        ans = 0
        freqMap = {}

        while r<len(s):
            freqMap[s[r]] = freqMap.get(s[r], 0) + 1

            while len(freqMap) > k:
                freqMap[s[l]] -= 1
                if freqMap[s[l]] == 0:
                    del freqMap[s[l]]
                l += 1
            
            ans = max(ans, r-l+1)
            r += 1
        return ans


obj = Solution()
s = "aababbcaacc"
k = 2
print(obj.kDistinctChar(s, k))