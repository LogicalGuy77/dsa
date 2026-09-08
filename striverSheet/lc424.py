class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        m = {}
        ans = 0

        while r < len(s):
            # check if in string, and inc freq
            m[s[r]] = m.get(s[r], 0) + 1

            maxFreq = max(m.values())
            
            toReplace = (r-l+1) - maxFreq

            if toReplace <= k:
                ans = max(ans, r-l+1)
            else:
                m[s[l]] -= 1
                if m[s[l]] == 0:
                    del m[s[l]]
                l += 1
            
            r += 1
        
        return ans

s = "AAAA"
k = 0
obj = Solution()
print(obj.characterReplacement(s, k))

