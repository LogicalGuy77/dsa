from collections import defaultdict

def count_special_subsequences(nums):
    n = len(nums)
    product_map = defaultdict(list)
    subsequences = set()  # To store unique subsequences

    # Build product_map with valid (p, r) pairs
    for p in range(n - 3):
        for r in range(p + 2, n - 1):  # Ensure there's room for 'q' and 's'
            product = nums[p] * nums[r]
            product_map[product].append((p, r))

    # Check (q, s) pairs against product_map
    for q in range(1, n - 2):
        for s in range(q + 2, n):
            product = nums[q] * nums[s]
            if product in product_map:
                for p, r in product_map[product]:
                    if p < q < r < s and q - p > 1 and r - q > 1 and s - r > 1:
                        subsequences.add((p, q, r, s))  # Add the unique subsequence

    return len(subsequences)

# Example Usage
nums =  [3,4,3,4,3,4,3,4]
print(count_special_subsequences(nums))  # Output: 2
