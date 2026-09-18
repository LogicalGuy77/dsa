class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        five, ten = 0, 0

        for i in bills:
            if i == 5:
                five += 1
            elif i == 10:
                if five:
                    five -= 1
                    ten += 1
                else:
                    return False
            else:
                if ten and five:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        
        return True



bills = [5,5,10,10,20]
obj = Solution()
print(obj.lemonadeChange(bills))