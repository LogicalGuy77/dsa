n = 5
k = 14
a = [4, 2, 5, 6, 7]

dp = {}  # Memoization dictionary


def checkSum(i, s):
    if s == k:  # If we found a valid subset, return True
        return True
    if i >= n or s > k:  # If out of bounds or sum exceeds k, return False
        return False
    if (i, s) in dp:  # If the result is already computed, return it
        return dp[(i, s)]

    # Take the current element
    take = checkSum(i + 1, s + a[i])

    # Don't take the current element
    not_take = checkSum(i + 1, s)

    # Store the result in the DP table
    dp[(i, s)] = take or not_take
    return dp[(i, s)]


checkSum(0, 0) # Expected Output: True
print(dp)