class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0,0
        maxLen = 0
        map = {}
        size = 0
        while r<len(s):
            if s[r] not in map:
                map[s[r]] = r
            else:
                if map[s[r]] >= l:
                    l = map[s[r]]+1
                map[s[r]] = r
            
            size = r - l + 1
            if size>maxLen:
                maxLen = size
            r+=1
        return maxLen


s = "abcabcbb"
obj = Solution()
obj.lengthOfLongestSubstring(s)