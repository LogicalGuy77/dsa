nums = [1, 0, 2, 0, 3]

l = len(nums)
ans = 0

# A zeroed array to compare for validation
target = [0] * l

# Function to simulate the process
def simulate(start, direction):
    cpy = nums[:]  # Deep copy of the nums array
    curr = start
    d = direction  # 0 for left, 1 for right

    while 0 <= curr < l:
        if cpy[curr] == 0:
            # Move in the current direction
            if d == 0:  # Move left
                curr -= 1
            else:       # Move right
                curr += 1
        else:
            # Decrement and reverse direction
            cpy[curr] -= 1
            if d == 0:  # Reverse direction to right
                d = 1
                curr += 1
            else:       # Reverse direction to left
                d = 0
                curr -= 1

    # Check if all elements became zero
    return cpy == target

# Iterate through all positions where nums[i] == 0
for i in range(l):
    if nums[i] == 0:
        # Simulate for both directions
        if simulate(i, 0):  # Start moving left
            ans += 1
        if simulate(i, 1):  # Start moving right
            ans += 1

print(ans)
