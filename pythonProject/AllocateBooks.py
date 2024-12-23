arr = [25, 46, 28, 49, 24]
m = 4

def noStudents(array, pag):
    stu = 1
    currPages = 0
    for i in array:
        if currPages+i <= pag:
            currPages+=i
        else:
            stu+=1
            currPages=i
    return stu

low = max(arr)
high = sum(arr)

while low<=high:
    mid = (low+high)//2
    ans = noStudents(arr, mid)
    if ans<=m:
        high = mid-1
    else:
        low = mid+1
print(low)