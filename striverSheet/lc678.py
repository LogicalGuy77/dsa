class Solution:
    def checkValidString(self, s: str) -> bool:
        maxx = 0
        minn = 0
        # we keep a range

        for i in s:
            if i == '(':
                minn +=1
                maxx += 1
            elif i == ')':
                minn -= 1
                maxx -= 1
            else:
                minn -= 1
                maxx += 1

            if minn < 0:
                minn = 0
        
            if maxx < 0:
                return False
        
        return minn == 0

obj = Solution()
s = "()"
print(obj.checkValidString(s))