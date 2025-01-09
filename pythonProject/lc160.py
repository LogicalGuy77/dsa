class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA = 0
        lenB = 0

        temp = headA
        while temp:
            lenA += 1
            temp = temp.next

        temp = headB
        while temp:
            lenB += 1
            temp = temp.next

        if lenA > lenB:
            diff = lenA - lenB
            newHeadA = headA
            for i in range(0, diff):
                newHeadA = newHeadA.next

            var = headB
            while newHeadA:
                if newHeadA == var:
                    return newHeadA
                newHeadA = newHeadA.next
                var = var.next
            return None

        else:
            diff = lenB - lenA
            newHeadB = headB
            for i in range(0, diff):
                newHeadB = newHeadB.next

            var = headA
            while newHeadB:
                if newHeadB == var:
                    return newHeadB
                newHeadB = newHeadB.next
                var = var.next
            return None
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Create two linked lists with an intersection
listA_values = [4, 1]
listB_values = [5, 6, 1]
intersection_values = [8, 4, 5]

# Create individual parts of the lists
listA = create_linked_list(listA_values)
listB = create_linked_list(listB_values)
intersection = create_linked_list(intersection_values)

# Attach the intersection part to both lists
currentA = listA
while currentA.next:
    currentA = currentA.next
currentA.next = intersection

currentB = listB
while currentB.next:
    currentB = currentB.next
currentB.next = intersection

# Print the linked lists
print("List A:")
print_linked_list(listA)

print("List B:")
print_linked_list(listB)
