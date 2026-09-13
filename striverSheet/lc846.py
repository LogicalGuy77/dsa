from typing import List
from collections import Counter
import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        freq = Counter(hand)
        heap = list(freq.keys())
        heapq.heapify(heap)

        while heap:
            first = heap[0]

            for num in range(first, first + groupSize):
                if freq[num] == 0:
                    return False

                freq[num] -= 1

                # If we've used all copies, it should be the smallest
                # remaining number.
                if freq[num] == 0 and num == heap[0]:
                    heapq.heappop(heap)

        return True



obj = Solution()
hand = [1,2,3,6,2,3,4,7,8]
groupSize = 3
print(obj.isNStraightHand(hand, groupSize))