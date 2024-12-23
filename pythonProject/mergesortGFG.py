class Solution:
    def merge(self, arr, l, m, r):
        # code here
        mid = m
        temp = []
        left = l
        right = mid + 1
        while left <= mid and right <= r:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1
        while left <= mid:
            temp.append(arr[left])
            left += 1
        while right <= r:
            temp.append(arr[right])
            right += 1
        for i in range(l, r+1):
            arr[i] = temp[i - l]

    def mergeSort(self, arr, l, r):
        # code here
        if l >= r:
            return
        mid = (l + r) // 2
        self.mergeSort(arr, l, mid)
        self.mergeSort(arr, mid + 1, r)
        self.merge(arr, l, mid, r)
        print(arr)

N = 8
arr = [24, 18, 38, 43, 14, 40, 1, 54]
sorter = Solution()
sorter.mergeSort(arr,0,N-1)