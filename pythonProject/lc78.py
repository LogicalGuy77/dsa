res = []
curr = []

# Why curr.copy()?
# Preserves the snapshot of curr at that moment
def dfs(i):
    if i >= len(nums):
        res.append(curr.copy())
        return

    curr.append(nums[i])
    dfs(i + 1)

    curr.pop()
    dfs(i + 1)


dfs(0)
return res