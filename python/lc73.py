matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
row = len(matrix)
col = len(matrix[0])
col0 = 1

for i in range(0, row):
    for j in range(0, col):
        if matrix[i][j]==0:
            matrix[i][0] = 0
            if j!=0:
                matrix[0][j] = 0
            else:
                col0 = 0

for i in range(1, row):
    for j in range(1, col):
        if matrix[i][0]==0 or matrix[0][j]==0:
            matrix[i][j] = 0

if matrix[0][0]==0:
    for i in range(0, col):
        matrix[0][i]=0

if col0==0:
    for j in range(0, row):
        matrix[j][0]=0

print(matrix)
