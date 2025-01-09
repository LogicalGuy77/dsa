# User function Template for python3

class Solution:
    # Function to sort a linked list of 0s, 1s, and 2s.
    def segregate(self, head):
        if head is None or head.next is None:
            return head

        # Dummy nodes for separate lists of 0s, 1s, and 2s
        zeroHead = Node(-1)
        oneHead = Node(-1)
        twoHead = Node(-1)

        # Pointers to iterate through the new lists
        zero = zeroHead
        one = oneHead
        two = twoHead

        # Traverse the original list and segregate nodes
        temp = head
        while temp is not None:
            if temp.data == 0:
                zero.next = temp
                zero = zero.next
            elif temp.data == 1:
                one.next = temp
                one = one.next
            else:  # temp.data == 2
                two.next = temp
                two = two.next
            temp = temp.next

        # Connect the segregated lists
        zero.next = oneHead.next if oneHead.next else twoHead.next
        one.next = twoHead.next
        two.next = None

        # The head of the new list is the next of zeroHead
        return zeroHead.next


# Driver Code Starts
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()


if __name__ == "__main__":
    t = int(input("Enter number of test cases: "))
    for _ in range(t):
        arr = list(map(int, input("Enter elements of the list: ").strip().split()))
        head = None
        if arr:
            head = Node(arr[0])
            tail = head
            for value in arr[1:]:
                tail.next = Node(value)
                tail = tail.next

        print("Sorted list:")
        printList(Solution().segregate(head))
        print("~")
