from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def dfs(i):
            if i>=len(s):
                # List are stored by refence in python, so we need to create a copy
                res.append(path.copy())
                return
            
            for j in range(i, len(s)):
                if self.isPaliindrome(i, j,s):
                    path.append(s[i:j+1])
                    dfs(j+1)
                    path.pop()

        dfs(0)
        return res
    
    def isPaliindrome(self, left, right, s):
        while left<right:
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        return True





obj = Solution()
print(obj.partition("aab"))