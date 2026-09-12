from typing import List, Optional
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        new_list = []

        for head in lists:
            curr = head

            while curr:
                new_list.append(curr.val)
                curr = curr.next

        heapq.heapify(new_list)
        return self.heapsort(new_list)
        

    def heapsort(self, arr):
        dummy = ListNode()
        curr = dummy

        while arr:
            minn = heapq.heappop(arr)

            curr.next = ListNode(minn)
            curr = curr.next

        return dummy.next



lists = [[1,4,5],[1,3,4],[2,6]]
obj = Solution()
print(obj.mergeKLists(lists))