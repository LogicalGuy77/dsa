from typing import List
import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqMap = {}

        for k in tasks:
            freqMap[k] = freqMap.get(k, 0) + 1

        heap_arr = []
        for cnt in freqMap.values():
            heap_arr.append(-cnt)
        
        heapq.heapify(heap_arr)

        # heap_arr = [-cnt]
        time = 0
        q = deque()

        while heap_arr or q:
            time += 1
            if heap_arr:
                cnt = 1 + heapq.heappop(heap_arr)
                if cnt:
                    q.append([cnt, time+n])
            
            if q and q[0][1] == time:
                heapq.heappush(heap_arr, q.popleft()[0])

        return time





tasks = ["A","A","A","B","B","B"]
n = 2
obj = Solution()
print(obj.leastInterval(tasks, n))