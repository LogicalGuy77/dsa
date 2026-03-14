from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stk = []
        maxArea = 0

        for i in range(0, n):
            while stk and heights[stk[-1]] > heights[i]:
                ele = stk[-1]
                stk.pop()
                nse = i
                pse = -1 if stk==[] else stk[-1]
                area = heights[ele]*(nse - pse -1)
                maxArea = max(maxArea, area)
            
            stk.append(i)
        
        while stk:
            nse = n
            ele = stk[-1]
            stk.pop()
            pse = -1 if stk==[] else stk[-1]
            area = heights[ele]*(nse - pse -1)
            maxArea = max(maxArea, area)
            
        print(maxArea)

obj = Solution()
heights = [1,1]
obj.largestRectangleArea(heights)

# from typing import List
# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         n = len(heights)
#         nse = [n]*n
#         stk = []

#         for i in range(n-1, -1, -1):
#             while stk and heights[stk[-1]] > heights[i]:
#                 stk.pop()

#             nse[i] = n if stk==[] else stk[-1]
#             stk.append(i)

#         pse = [-1]*n
#         stk = []
#         for i in range(0, n):
#             while stk and heights[stk[-1]] >= heights[i]:
#                 stk.pop()

#             pse[i] = -1 if stk==[] else stk[-1]
#             stk.append(i)
        
#         ans = 0
#         for i in range(0, n):
#             compute = heights[i]*(nse[i] - pse[i] -1)
#             ans = max(ans, compute)
        
#         print(ans)