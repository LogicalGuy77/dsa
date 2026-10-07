import heapq
import random

class Solution:
    # def findKthLargest(self, nums: list[int], k: int) -> int:
    #     print(nums)
    #     for i in range(0, len(nums)):
    #         nums[i] = nums[i]*-1

    #     heapq.heapify(nums)
    #     ans = []
    #     while nums:
    #         ans.append(heapq.heappop(nums))
    #     return (ans[k-1]*-1)

    def findKthLargest(self, nums: list[int], k: int) -> int:
        k = len(nums) - k

        def quickSelect(l, r):
            pivot_index = random.randint(l, r)
            nums[pivot_index], nums[r] = nums[r], nums[pivot_index]

            pivot = nums[r]
            p = l

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1

            nums[p], nums[r] = nums[r], nums[p]

            if p == k:
                return nums[p]
            elif p > k:
                return quickSelect(l, p - 1)
            else:
                return quickSelect(p + 1, r)

        return quickSelect(0, len(nums) - 1)


nums = [3,2,1,5,6,4]
k = 2
obj = Solution()
print(obj.findKthLargest(nums, k))