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
        temp = []

        while left<=m and right<=r:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left+=1
            else:
                temp.append(arr[right])
                cnt += (mid - left + 1)
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


N = 8
arr = [24, 18, 38, 43, 14, 40, 1, 54]
sorter = Solution()
ans = sorter.noOfInversion(arr,N-1)
print(ans)