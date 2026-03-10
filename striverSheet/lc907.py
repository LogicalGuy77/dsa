from typing import List
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        sum = 0
        n = len(arr)

        # prev smallest index
        psi = [-1]
        for i in range(1, n):
            idx = i-1 if arr[i-1] < arr[i] else psi[-1]
            psi.append(idx)
        
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

            sum += right*left*arr[i]
        

        print(sum % (10**9 + 7))





obj = Solution()
arr = [3,1,2,4]
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