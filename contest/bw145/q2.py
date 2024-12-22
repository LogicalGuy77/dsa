def min_operations_to_make_equal(nums, k):
    # If k is greater than the maximum in nums, it's impossible
    if k > max(nums):
        return -1

    # Sort nums in descending order
    nums.sort(reverse=True)
    operations = 0

    # Initialize the current valid value to the maximum in nums
    current = nums[0]

    for num in nums:
        if num > k:
            # Reduce the current value to the new num (next smaller unique value in nums)
            if num < current:
                operations += 1
                current = num
        elif num == k:
            # Continue for values already equal to k
            continue
        else:
            return -1  # Cannot reduce any further without violating the rules

    # Add one last operation if current > k
    if current > k:
        operations += 1

    return operations

# Test cases
print(min_operations_to_make_equal([5, 2, 5, 4, 5], 2))  # Output: 2
print(min_operations_to_make_equal([2, 1, 2], 2))        # Output: -1

