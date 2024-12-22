


class Solution:
    def select(self, arr, i):
        # code here
        min = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min]:
                min = j
        return min

    def selectionSort(self, arr, n):
        # code here
        for i in range(0, n - 1):
            min = self.select(arr, i)
            # swap
            temp = arr[i]
            arr[i] = arr[min]
            arr[min] = temp
        print(arr)

N = 5
arr = [4, 1, 3, 9, 7]
sorter = Solution()
sorter.selectionSort(arr, N)