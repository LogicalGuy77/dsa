intervals = [[1, 3], [2, 6], [15, 18], [8, 10]]
intervals.sort()
ans = []

for i in range(0, len(intervals)):
    if ans == [] or intervals[i][0] > ans[len(ans)-1][1]:
        ans.append([intervals[i][0],intervals[i][1]])
    else:
        ans[len(ans)-1][1] = max(intervals[i][1],ans[len(ans)-1][1] )

print(ans)