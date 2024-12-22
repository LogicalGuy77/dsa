nums = [18,57]
k = 97
numOperations = 2

nums.sort()

left = 0
max_freq = 1
total_operations = 0
for right in range(len(nums)):
    total_operations += nums[right]

    while (nums[right] * (right - left + 1) - total_operations) > numOperations:
        total_operations -= nums[left]
        left += 1
    max_freq = max(max_freq, right - left + 1)




print("Maximum possible frequency:", max_freq)
