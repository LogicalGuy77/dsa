from typing import List
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        
        def minSubSum(arr):
            sum = 0
            n  = len(nums)

            stk = []
            preMin = [-1]*n
            for i in range(n):
                while stk and arr[stk[-1]] > arr[i]:
                    stk.pop()
                preMin[i] = -1 if stk==[] else stk[-1]
                stk.append(i)
            
            nextMin = [n]*n
            stk = []
            for i in range(n-1, -1, -1):
                while stk and arr[stk[-1]] >= arr[i]:
                    stk.pop()
                nextMin[i] = n if stk==[] else stk[-1]
                stk.append(i)
            
            for i in range(n):
                left = i - preMin[i]
                right = nextMin[i] - i
                sum += left*right*arr[i]                

            return sum
        
        def maxSubSum(arr):
            sum = 0
            n = len(arr)

            stk = []
            preMax = [-1]*n
            for i in range(n):
                while stk and arr[stk[-1]] < arr[i]:
                    stk.pop()
                preMax[i] = -1 if stk==[] else stk[-1]
                stk.append(i)

            stk = []
            nextMax = [n]*n
            for i in range(n-1, -1, -1):
                while stk and arr[stk[-1]] <= arr[i]:
                    stk.pop()
                nextMax[i] = n if stk==[] else stk[-1]
                stk.append(i)

            for i in range(n):
                left = i - preMax[i]
                right = nextMax[i] - i
                sum += right*left*arr[i]
            return sum

        return maxSubSum(nums) - minSubSum(nums)

obj = Solution()
nums = [1, 2, 3]
print(obj.subArrayRanges(nums))