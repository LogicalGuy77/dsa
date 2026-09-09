class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l = 0
        r = 0
        subArr = 0
        count = 0
        mapFreq = {}
        while r < len(s):
            if s[r] == "a" or s[r] == "b" or s[r] == "c":
                mapFreq[s[r]] = mapFreq.get(s[r], 0) + 1
                
            while len(mapFreq) == 3:
                subArr += len(s)-r

                mapFreq[s[l]] -= 1
                if mapFreq[s[l]] == 0:
                    del mapFreq[s[l]]
                l += 1

            r += 1
        
        print(subArr)


obj = Solution()
s = "abcabc"
obj.numberOfSubstrings(s)

