arr = [1, 2, 1]
ans = []
n = len(arr)
def calcSum(index, sum):
    if index==n:
        ans.append(sum)
        return
    # take
    calcSum(index+1, sum+arr[index])
    # not take
    calcSum(index+1, sum)

calcSum(0, 0)
print(ans)