weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
days = 5

def daysTaken(arr, capacity):
    day = 1
    currCap = 0
    for i in arr:
        if currCap+i > capacity:
            day+=1
            currCap=i
        else:
            currCap+=i
    return day



s = 0
for i in weights:
    s += i
low = max(weights)
high = s
minc = -1
while low <= high:
    mid = (low + high) // 2
    # mid is capacity
    d = daysTaken(weights, mid)

    if d<=days:
        high = mid-1

    else:
        low = mid+1

print(low)