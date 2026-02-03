class Solution:
    def isValid(self, s: str) -> bool:
        
        s1 = []
        for c in s:
            if not s1:
                s1.append(c)
            else:
                if s1[-1] == '[' and c == ']':
                    s1.pop()
                elif s1[-1] == '{' and c == '}':
                    s1.pop()
                elif s1[-1] == '(' and c == ')':
                    s1.pop()
                else:
                    s1.append(c)
        return len(s1) == 0



obj = Solution()
s = "([])"
print(obj.isValid(s))