from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        memo = {}

        def dfs(cpyStr, n):
            if n == len(s):
                return cpyStr in wordSet or cpyStr == ""

            key = (n, cpyStr)
            if key in memo:
                return memo[key]

            # option 1: continue building word
            take = dfs(cpyStr + s[n], n + 1)

            # option 2: split if current word is valid
            split = False
            if cpyStr in wordSet:
                split = dfs("", n)

            memo[key] = take or split
            return memo[key]

        return dfs("", 0)







s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
obj = Solution()
print(obj.wordBreak(s, wordDict))