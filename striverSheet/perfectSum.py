arr = [5,2,3,10,6,8]
res = []
ans = []
last_occur = {}
sum = 0
target = 10

def countSub(i, sum):

    if i >= len(arr):
        if sum == target:
            ans.append(res.copy())
        sum = 0
        return

    char = arr[i]

    res.append(char)
    sum += char
    countSub(i+1, sum)
    res.pop()

    sum -= char
    countSub(i+1, sum)
    return ans

k = countSub(0, sum)
print(k)