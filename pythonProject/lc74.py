matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

n = len(matrix)
m = len(matrix[0])

l = 0
h = (n*m-1)

while l<=h:
    mid = (l+h)//2
    r = mid//m
    c = mid%m
    if matrix[r][c]==target:
        return True
    elif matrix[r][c]<target:
        l = mid+1
    else:
        h = mid-1
return False