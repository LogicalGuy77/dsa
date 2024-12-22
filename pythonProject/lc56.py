intervals = [[1, 3], [2, 6], [15, 18], [8, 10]]
intervals.sort()
ans = []

for i in range(0, len(intervals)):
    start = intervals[i][0]
    end = intervals[i][1]
    if ans != [] and end <= ans[len(ans)-1][1]:
        continue
    for j in range(i+1, len(intervals)):
        if intervals[j][0] <= end:
            end = max(end, intervals[j][1])
        else:
            break
    ans.append([start, end])
print(intervals)
print(ans)
