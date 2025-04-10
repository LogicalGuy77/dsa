nums = [1,2,2]
nums.sort()
ans = []
n = len(nums)
ds = []
def subset(index, ds):
    if index==n:
        if ds not in ans:
            ans.append(ds[:])
        return

    # take
    ds.append(nums[index])
    subset(index+1, ds)
    ds.pop()
    # not take
    subset(index+1, ds)

subset(0, [])

print(ans)