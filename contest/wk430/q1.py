grid = [[3, 2], [1, 3], [3, 4], [0, 1]]

ans=0

n = len(grid)
m = len(grid[0])
ans = 0

for j in range(m):
    colOp = 0
    for i in range(n-1):
        if grid[i+1][j] <= grid[i][j]:
            colOp+= (grid[i][j]-grid[i+1][j])+1
            grid[i+1][j] = grid[i][j]+1
    ans+=colOp

print(ans)