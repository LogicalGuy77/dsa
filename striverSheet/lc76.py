class Solution:
    def minWindow(self, s: str, t:str) -> str:
        if t == "":
            return ""
        freqMapT = {}

        for i in range(0, len(t)):
            freqMapT[t[i]] = freqMapT.get(t[i], 0) + 1

        l = 0
        r = 0
        have = 0
        need = len(freqMapT)
        freqMapS = {}

        ans = -1
        ansLen = float("inf")

        while r < len(s):
            freqMapS[s[r]] = freqMapS.get(s[r], 0) + 1

            if s[r] in freqMapT and freqMapS[s[r]] == freqMapT[s[r]]:
                have += 1
            
            while have == need:
                if (r-l+1) < ansLen:
                    ans = l
                    ansLen = r-l+1

                freqMapS[s[l]] -= 1
                if s[l] in freqMapT and freqMapS[s[l]] < freqMapT[s[l]]:
                    have -= 1
                
                l += 1
            
            r += 1
        
        if ans > -1:
            print(s[ans:ans+ansLen])
        
        return ""


s = "ADOBECODEBANC"
t = "ABC"
obj = Solution()
obj.minWindow(s, t)