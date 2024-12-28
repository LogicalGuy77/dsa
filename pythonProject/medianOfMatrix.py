mat = [[1, 3, 5], [2, 6, 9], [3, 6, 9]]

low = float('inf')
high = float('-inf')

n = len(mat)
m = len(mat[0])

def upperBound(matrix, x):
    ans = n
    low = 0
    high = len(matrix)-1

    while low<=high:
        mid = (low+high)//2
        if matrix[mid] > x:
            ans = mid
            high = mid-1
        else:
            low = mid+1
    return ans

def countSmallEqual(matrix, x):
    count = 0
    for i in range(n):
        count += upperBound(matrix[i], x)
    return count

for i in range(0, n):
    low = min(low, mat[i][0])
    high = max(high, mat[i][m-1])

req = (m*n)//2

while low<=high:
    mid = (low+high)//2
    smallEqual = countSmallEqual(mat, mid)
    if smallEqual<=req:
        low = mid+1
    else:
        high = mid-1

print(low)
