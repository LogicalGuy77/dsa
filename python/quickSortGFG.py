class Solution:
    # Function to sort a list using quick sort algorithm.
    def quickSort(self, arr, low, high):
        # code here
        if low<high:
            pIndex = self.partition(arr, low, high)
            self.quickSort(arr, low, pIndex-1)
            self.quickSort(arr, pIndex+1, high)
        print(arr)

    def partition(self, arr, low, high):
        # code here
        pivot = arr[low]
        i=low
        j=high
        while i<j:
            while arr[i]<=pivot and i<=high-1:
                i+=1
            while arr[j]>pivot and j>=low+1:
                j-=1
            if i<j:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
        copy = arr[low]
        arr[low] = arr[j]
        arr[j] = copy
        return j



N=5
arr = [4,1,3,9,7]
sorter = Solution()
sorter.quickSort(arr, 0, 4)

