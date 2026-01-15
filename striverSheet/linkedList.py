class Node:
    def __init__(self, data):
        self.data = data  # The data stored in the node
        self.next = None  # Pointer to the next node

class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the linked list with an empty head

    def append(self, data):
        """Add a new node at the end of the list."""
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
            return
        # Traverse to the end of the list
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        """Display the linked list elements."""
        if not self.head:
            print("The linked list is empty.")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def remove(self, key):
        """Remove the first occurrence of a node with the given key."""
        current = self.head

        # If the head node itself holds the key
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        # Search for the key to be deleted
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        # If the key was not found
        if not current:
            print(f"Value {key} not found in the list.")
            return

        # Unlink the node
        prev.next = current.next
        current = None

# Example Usage
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.display()  # Output: 10 -> 20 -> 30 -> None
    ll.remove(20)
    ll.display()  # Output: 10 -> 30 -> None
    ll.remove(40) # Output: Value 40 not found in the list.
