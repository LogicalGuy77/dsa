arr = [1, 2, 3, 4, 5, 6]
k = 7

l = 0
h = len(arr) - 1
if k==arr[0] or k==arr[h]:
    print(1)
if k<arr[0] or k>arr[h]:
    print(-1)
while (h - l) > 1:
    mid = (l + h) // 2

    if k == arr[mid]:
        print(1)
        break
    if k > arr[mid]:
        l = mid
    if k < arr[mid]:
        h = mid
print(0)
