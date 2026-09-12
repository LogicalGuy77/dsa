import heapq

class Solution:
    def heapsort(self, arr):
        heapq.heapify(arr)
        print(arr)

        new_arr = [0]*len(arr)

        for i in range(len(arr)):
            minn = heapq.heappop(arr)
            new_arr[i] = minn 

        print(new_arr)



arr = [3,1,2,3,10,7,8]
obj = Solution()
obj.heapsort(arr)