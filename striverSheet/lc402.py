class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        if len(num) == k:
            print("0")
            return
        
        stk = []
        for i in num:
            while stk and stk[-1] > i and k>0:
                stk.pop()
                k -= 1

            stk.append(i)

        while k!=0:
            stk.pop()
            k -= 1
        
        ez = []
        flag = True
        for i in stk:
            if i=='0' and flag:
                print("reach")
                continue
            flag = False
            ez.append(i)
            print(ez)

        ans = ""
        for i in ez:
            ans += i
        
        if ans == "":
            print("0")
        else:
            print(ans)



obj = Solution()
num = "10"
k = 1
obj.removeKdigits(num, k)