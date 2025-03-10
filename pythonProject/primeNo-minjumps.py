Arr = [10, 14, 29, 21, 17, 4, 18, 20, 18, 22, 21, 14, 27, 12, 3, 28, 17, 0, 2, 18, 8, 20, 26, 16, 9, 23, 25, 20,
       7, 27,
       5, 7, 16, 5, 25, 11, 3, 7, 2, 17, 14, 6, 12, 14, 23, 25, 26, 5, 18, 1, 6, 10, 9, 12, 2, 25, 29, 12, 19, 4, 8, 5,
       8, 30, 2, 22, 24, 30, 7, 24, 8, 15, 16, 2, 11, 20]
N = 76


def minJump(arr, n):
    # code here
    l = r = 0
    res = 0

    while r < n - 1:
        furthest = 0
        for i in range(l, r + 1):
            furthest = max(furthest, i + arr[i])
        if r==furthest:
               return -1
        l = r + 1
        r = furthest
        res += 1
    return res


print(minJump(Arr, N))
