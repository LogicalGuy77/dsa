import sys

k = 3
n = 9
ans = []
ds = []

if n < ((k*(k+1))//2):
    print(ds)
    sys.exit(0)

def combSum(num, tar, ds):
    if num==10:
        if tar==0 and len(ds)==k:
            ans.append(ds[:])
        return
    # take
    if len(ds) < k:
        ds.append(num)
        combSum(num+1, tar-num, ds)
        ds.pop()
    # not take
    combSum(num+1, tar, ds)

combSum(1, n, [])
print(ans)

