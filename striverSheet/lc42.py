from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        prefixMax = [height[0]]
        for i in range(1, n):
            prefixMax.append(max(prefixMax[i-1], height[i]))

        # print(prefixMax)

        suffixMax = [-1]*(n-1)
        suffixMax.append(height[-1])
        for i in range(n-2, -1, -1):
            suffixMax[i] = (max(suffixMax[i+1], height[i]))

        # print(suffixMax)

        # water[i] = summation of [ min(leftMax, rightMax) - height[i] ]
        total = 0
        for i in range(0, n):
            leftMax = prefixMax[i]
            rightMax = suffixMax[i]

            if leftMax > height[i] and rightMax > height[i]:
                total += min(leftMax, rightMax) - height[i]
        
        print(total)

obj = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
obj.trap(height)



# class Solution:
#     def trap(self, height: List[int]) -> int:
#         left, right = 0, len(height) - 1
#         leftMax = rightMax = 0
#         total = 0

#         while left < right:
#             if height[left] < height[right]:
#                 if height[left] >= leftMax:
#                     leftMax = height[left]
#                 else:
#                     total += leftMax - height[left]
#                 left += 1
#             else:
#                 if height[right] >= rightMax:
#                     rightMax = height[right]
#                 else:
#                     total += rightMax - height[right]
#                 right -= 1

#         return total