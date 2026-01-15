from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = { '2': {'a', 'b', 'c'},
                        '3': {'d', 'e', 'f'},
                        '4': {'g', 'h', 'i'},
                        '5': {'j', 'k', 'l'},
                        '6': {'m', 'n', 'o'},
                        '7': {'p', 'q', 'r'},
                        '8': {'t', 'u', 'v'},
                        '9': {'w', 'x', 'y', 'z'}
        }

        def backtrack(i , curStr):
            if len(digits) == i:
                res.append(curStr)
                return
            
            for char in digitToChar[digits[i]]:
                backtrack(i+1, curStr+char)
        
        if digits:
            backtrack(0, '')
        else:
            return ''
        
        print(res)


obj = Solution()
obj.letterCombinations("23")