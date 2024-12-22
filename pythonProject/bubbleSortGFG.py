class Solution:
    # Function to sort the array using bubble sort algorithm.
    def bubbleSort(self, arr, n):
        temp=0
        for j in range (0, n):
            if arr[j]>arr[j+1]:
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp
        print(arr)

N = 8
arr = [24, 18, 38, 43, 14, 40, 1, 54]
sorter = Solution()
sorter.bubbleSort(arr, N)
