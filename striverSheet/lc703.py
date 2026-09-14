from typing import List
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums
        heapq.heapify(self.minHeap)

        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)


    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)

        if len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
        
        return self.minHeap[0]






k = 3
nums = [4, 5, 8, 2]
kthLargest = KthLargest(k, nums);
print(kthLargest.add(3))