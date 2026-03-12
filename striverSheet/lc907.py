from typing import List
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        sum = 0
        n = len(arr)

        # prev smallest index
        stack = []
        psi = [-1]*n
        
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            psi[i] = stack[-1] if stack else -1
            stack.append(i)
        
        print(psi)

        # next smallest index
        stk = []
        nsi = [n]*n
        for i in range(n-1, -1, -1):
            while (stk!=[] and arr[i] <= arr[stk[-1]]):
                stk.pop()
            nsi[i] = n if stk == [] else stk[-1]
            stk.append(i)
        
        for i in range(0, n):
            left = i - psi[i]
            right = nsi[i] - i

            # no. of sub arr you can generate is left*right
            sum += right*left*arr[i]
        

        print(sum % (10**9 + 7))





obj = Solution()
arr = [2,9,7,8,3,4,6,1]
obj.sumSubarrayMins(arr)



# class Solution:
#     def sumSubarrayMins(self, arr: List[int]) -> int:
#         sum = 0
#         n = len(arr)
#         for i in range(0, n):
#             mini = arr[i]
#             for j in range(i, n):
#                 mini = min(mini, arr[j])
#                 sum += mini
        
#         print(sum% (10**9 + 7))


#     # O(n^2)