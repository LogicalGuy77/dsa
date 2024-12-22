nums = [1]
perms = [[]]
res = []

for p in perms:
    for i in range(len(p)+1):
        p_copy = p.copy()
        p_copy.insert(i, nums[0])
        res.append(p_copy)

print(res)