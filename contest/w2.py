from typing import List


class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        def check(k: int) -> bool:
            for i in range(n - 2 * k + 1):
                valid_first = True
                for j in range(i, i + k - 1):
                    if nums[j] >= nums[j + 1]:
                        valid_first = False
                        i = j
                        break

                if not valid_first:
                    continue

                valid_second = True
                for j in range(i + k, i + 2 * k - 1):
                    if nums[j] >= nums[j + 1]:
                        valid_second = False
                        break

                if valid_second:
                    return True

            return False

        n = len(nums)
        left, right = 1, n // 2
        result = 0

        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result


# Test cases
def test():
    sol = Solution()

    # Test case 1
    nums1 = [2, 5, 7, 8, 9, 2, 3, 4, 3, 1]
    print(sol.maxIncreasingSubarrays(nums1))  # Expected: 3

    # Test case 2
    nums2 = [1, 2, 3, 4, 4, 4, 4, 5, 6, 7]
    print(sol.maxIncreasingSubarrays(nums2))  # Expected: 2
