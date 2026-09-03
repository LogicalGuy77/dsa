import unittest


class Node:
    def __init__(self, key, val):
        # The key and value stored in the cache.
        self.key = key
        self.val = val

        # A newly inserted key has been used once.
        self.freq = 1

        # Pointers used by the doubly linked list.
        self.prev = None
        self.next = None


class DoublyLinkedList:
    """
    Stores nodes that have the same frequency.

    The most recently used node is placed near head.
    The least recently used node is placed near tail.
    """

    def __init__(self):
        # Dummy nodes make insertion and removal easier.
        self.head = Node(None, None)
        self.tail = Node(None, None)

        self.size = 0

        # Initially:
        #
        # head <-> tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_first(self, node: Node) -> None:
        """
        Add a node immediately after head.

        This makes it the most recently used node
        within its frequency group.
        """

        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

        self.size += 1

    def remove(self, node: Node) -> None:
        """
        Remove a particular node in O(1) time.

        Because the node already has prev and next references,
        we don't need to traverse the linked list.
        """

        node.prev.next = node.next
        node.next.prev = node.prev

        # Disconnect the removed node from the list.
        node.prev = None
        node.next = None

        self.size -= 1

    def remove_last(self) -> Node | None:
        """
        Remove and return the least recently used node.

        The real node immediately before tail is the
        least recently used node in this frequency group.
        """

        if self.is_empty():
            return None

        node = self.tail.prev
        self.remove(node)

        return node

    def move_to_front(self, node: Node) -> None:
        """
        Move a node to the most recently used position
        within the same linked list.
        """

        self.remove(node)
        self.add_first(node)

    def is_empty(self) -> bool:
        """
        The list is empty when head points directly to tail.
        """

        return self.head.next is self.tail


class LFUCache:
    def __init__(self, capacity: int):
        # Maximum number of key-value pairs the cache can hold.
        self.capacity = capacity

        # Smallest frequency currently present in the cache.
        #
        # It starts at 0 because the cache is initially empty.
        self.minFreq = 0

        # Maps:
        #
        # key -> Node
        #
        # This allows get() to find a node in average O(1) time.
        self.keyMap = {}

        # Maps:
        #
        # frequency -> DoublyLinkedList
        #
        # Every linked list stores nodes having the same frequency.
        self.freqMap = {}

    def increase_frequency(self, node: Node) -> None:
        """
        Move a node from its current frequency group
        to the next frequency group.

        This method is used by:
        - A successful get()
        - A put() that updates an existing key
        """

        # Step 1: Remember the node's current frequency.
        old_frequency = node.freq

        # Step 2: Find the linked list for that frequency.
        old_list = self.freqMap[old_frequency]

        # Step 3: Remove the node from its old frequency list.
        old_list.remove(node)

        # Step 4: If the old list becomes empty, remove it.
        if old_list.is_empty():
            del self.freqMap[old_frequency]

            # If this was the minimum-frequency group,
            # the minimum frequency moves up by one.
            if old_frequency == self.minFreq:
                self.minFreq += 1

        # Step 5: Increase this particular node's frequency.
        node.freq += 1
        new_frequency = node.freq

        # Step 6: Create the new frequency list if necessary.
        if new_frequency not in self.freqMap:
            self.freqMap[new_frequency] = DoublyLinkedList()

        # Step 7: Add the node to the front of its new list.
        #
        # It is now the most recently used node among the
        # nodes having new_frequency.
        self.freqMap[new_frequency].add_first(node)

    def get(self, key: int) -> int:
        """
        Return the value associated with key.

        If the key doesn't exist:
        - Return -1.
        - Don't change the cache.

        If the key exists:
        - Increase its frequency.
        - Update its recent-use position.
        - Return its value.
        """

        # Case 1: Missing key.
        if key not in self.keyMap:
            return -1

        # Case 2: Existing key.
        node = self.keyMap[key]

        # A successful get counts as another use.
        self.increase_frequency(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        """
        Update an existing key or insert a new key.

        There are four cases:

        1. The capacity is zero.
        2. The key already exists.
        3. The key is new and the cache is full.
        4. A new node must be inserted.
        """

        # Case 0: The cache cannot store anything.
        if self.capacity == 0:
            return

        # Case 1: The key already exists.
        if key in self.keyMap:
            # Get the existing node.
            node = self.keyMap[key]

            # Update its value.
            node.val = value

            # Updating an existing key counts as another use.
            self.increase_frequency(node)

            # Stop here so the key isn't inserted again.
            return

        # Case 2: The key is new, but the cache is full.
        if len(self.keyMap) == self.capacity:
            # Get the list containing the least frequently
            # used nodes.
            minimum_frequency_list = self.freqMap[self.minFreq]

            # If multiple nodes have minFreq, remove the LRU node.
            # The LRU node is located immediately before tail.
            evicted_node = minimum_frequency_list.remove_last()

            # Remove the evicted key from the key lookup map.
            del self.keyMap[evicted_node.key]

            # Remove the frequency group if it is now empty.
            if minimum_frequency_list.is_empty():
                del self.freqMap[self.minFreq]

        # Case 3: Insert the new key.

        # A newly created node starts with frequency 1.
        node = Node(key, value)

        # Add it to the key lookup map.
        self.keyMap[key] = node

        # Create the frequency-1 list if it doesn't exist.
        if 1 not in self.freqMap:
            self.freqMap[1] = DoublyLinkedList()

        # The newly inserted node is the most recently used
        # node in the frequency-1 group.
        self.freqMap[1].add_first(node)

        # Every new node starts at frequency 1, so the minimum
        # frequency is now definitely 1.
        self.minFreq = 1