from typing import List

class Solution:
    def addOperators(self, num: str, target: int):
        res = []
        n = len(num)

        def dfs(idx, expr, curr_val, last):
            if idx == n:
                if curr_val == target:
                    res.append(expr)
                return

            for i in range(idx, n):
                # avoid leading zeros
                if i > idx and num[idx] == '0':
                    break

                curr_num = int(num[idx:i+1])

                if idx == 0:
                    # first number, no operator
                    dfs(i+1, str(curr_num), curr_num, curr_num)
                else:
                    dfs(i+1, expr + "+" + str(curr_num),
                        curr_val + curr_num, curr_num)

                    dfs(i+1, expr + "-" + str(curr_num),
                        curr_val - curr_num, -curr_num)

                    dfs(i+1, expr + "*" + str(curr_num),
                        curr_val - last + last * curr_num,
                        last * curr_num)

        dfs(0, "", 0, 0)
        return res


obj = Solution()
obj.addOperators("123", 6)