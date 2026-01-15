numRows = 5

matrix = [[1]]

# if numRows == 1:
#     return matrix

for i in range(1, numRows):
    arr = []
    for j in range(0, i+1):
        if j==0 or j==i:
            arr.append(1)
        else:
            op = matrix[i-1][j] + matrix[i-1][j-1]
            arr.append(op)
    matrix.append(arr)

print(matrix)