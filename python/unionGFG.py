arr1 = [1,2,3,4,5]
arr2 = [1,2,3,6,6,7]

m = 5
n = 6
ans = []
i, j = 0, 0

while i<m and j<n:
    if arr1[i]<=arr2[j]:
        if len(ans) == 0 or ans[len(ans)-1] != arr1[i]:
            ans.append(arr1[i])
        i+=1
    else:
        if len(ans) == 0 or ans[len(ans)-1] != arr2[j]:
            ans.append(arr2[j])
        j+=1
while i<m:
    if len(ans) == 0 or ans[len(ans) - 1] != arr1[i]:
        ans.append(arr1[i])
    i += 1
while j<n:
    if len(ans) == 0 or ans[len(ans) - 1] != arr2[j]:
        ans.append(arr2[j])
    j += 1
print(ans)