class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None


class Solution:
    def addOne(self, head):
        # Reverse the linked list to make addition easier
        def reverse(node):
            prev = None
            current = node
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev

        # Step 1: Reverse the linked list
        head = reverse(head)

        # Step 2: Add one to the number represented by the reversed list
        carry = 1
        current = head
        prev = None
        while current:
            new_value = current.data + carry
            current.data = new_value % 10
            carry = new_value // 10
            prev = current
            current = current.next

        # Step 3: If there's still a carry, add a new node
        if carry > 0:
            prev.next = Node(carry)

        # Step 4: Reverse the list back to its original order
        head = reverse(head)

        return head


# Helper function to create a linked list from a list
def create_linked_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for value in values[1:]:
        current.next = Node(value)
    return head


# Helper function to print a linked list
def print_linked_list(head):
    current = head
    result = []
    while current:
        result.append(current.data)
        current = current.next
    print(" -> ".join(map(str, result)))


# Test the addOne function
values = [9, 9, 9]  # Representing the number 999
head = create_linked_list(values)
solution = Solution()
new_head = solution.addOne(head)
print_linked_list(new_head)  # Output: 1 -> 0 -> 0 -> 0
