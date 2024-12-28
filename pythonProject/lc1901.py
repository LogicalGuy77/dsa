import sys

mat = [[10, 20, 15], [21, 30, 14], [7, 16, 32]]

low = 0
high = len(mat[0])


def maxRowIndex(arr, col):
    maxI = 0
    maxEle = arr[0][col]
    for i in range(1, len(arr)):
        if arr[i][col] > maxEle:
            maxEle = arr[i][col]
            maxI = i
    return maxI


while low <= high:
    mid = (low + high) // 2
    indx = maxRowIndex(mat, mid) #row
    left = mat[indx][mid-1] if (mid-1) >= 0 else -1
    right = mat[indx][mid+1] if (mid+1)<len(mat[0]) else -1

    if left<mat[indx][mid] and right<mat[indx][mid]:
        print(indx, mid)
        sys.exit(0)
    elif mat[indx][mid] < left:
        high = mid-1
    else:
        low = mid+1

