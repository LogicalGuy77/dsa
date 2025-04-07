candidates = [2,5,2,1,2]
candidates.sort()
target = 5
n = len(candidates)
ans = []
ds = []


def soln(index, tar, ds):
    if tar == 0:
        ans.append(ds[:])
        return
    for i in range(index, n):
        if i > index and candidates[i] == candidates[i - 1]:
            continue  # skip duplicates
        if candidates[i] > tar:
            break
        ds.append(candidates[i])
        soln(i + 1, tar - candidates[i], ds)
        ds.pop()

soln(0, target, ds)
print(ans)
