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
            
        return (maxArea)

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        maxArea = 0
        hist = [0]*len(matrix[0])
        for i in matrix:
            for j in range(0, len(i)):
                hist[j] = hist[j]+1 if i[j]=="1" else 0
            
            area = self.largestRectangleArea(hist)
            maxArea = max(maxArea, area)

        print(maxArea)


obj = Solution()
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
obj.maximalRectangle(matrix)