from typing import Optional

# Define the ListNode class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Define the Solution class with the middleNode function
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Code
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

# Helper function to create a linked list from a list
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to print a linked list
def print_linked_list(head):
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    print(" -> ".join(map(str, values)))

# Simulate the input
head_values = [1, 2, 3, 4, 5]
head = create_linked_list(head_values)

# Print the original linked list
print("Original Linked List:")
print_linked_list(head)

# Find and print the middle node
solution = Solution()
middle = solution.middleNode(head)
print("\nMiddle Node Value:")
print(middle.val if middle else "No middle node")
