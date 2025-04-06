candidates = [2, 3, 6, 7]
target = 7
n = len(candidates)
ans = []
ds = []


def soln(index, tar, ds):
    if index == n:
        if tar == 0:
            ## append copy
            ans.append(ds[:])
        return
    # pick
    if tar - candidates[index] > -1:
        ds.append(candidates[index])
        soln(index, tar - candidates[index], ds)
        ds.pop()
    # not pick
    soln(index + 1, tar, ds)


soln(0, target, ds)
print(ans)
