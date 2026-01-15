# arr = [2,4,1,3,5]
#
# n = len(arr)
# count = 0
# for i in range(0, n):
#     a = arr[i]
#     for j in range(i+1, n):
#         if a > arr[j]:
#             count+=1
# print(count)

class Solution:
    def merge(self, arr, l, m, r):
        # code here
        cnt = 0
        mid = m
        left = l
        right = m+1
        right2 = m+1
        temp = []

        for i in range(l, m+1):
            while right2<=r and arr[i] > 2*arr[right2]:
                right2+=1
            cnt += (right2 - (m + 1))

        while left<=m and right<=r:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left+=1
            # right is smaller
            else:
                temp.append(arr[right])
                right+=1
        while left<=mid:
            temp.append(arr[left])
            left+=1
        while right<=r:
            temp.append(arr[right])
            right+=1
        for i in range(l, r+1):
            arr[i] = temp[i-l]

        return cnt

    def mergeSort(self, arr, l, r):
        # code here
        cnt = 0
        if l>=r:
            return cnt
        mid = (l+r)//2
        cnt += self.mergeSort(arr, l, mid)
        cnt += self.mergeSort(arr, mid+1, r)
        cnt += self.merge(arr, l, mid, r)
        return cnt

    def noOfInversion(self, arr, N):
        count = self.mergeSort(arr, 0, N)
        return count


N = 5
arr = [1,3,2,3,1]
sorter = Solution()
ans = sorter.noOfInversion(arr,N-1)
print(ans)