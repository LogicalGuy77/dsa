class ArrayStack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if self.isEmpty():
            print("Popping from empty stack")
        else:
            return self.stack.pop()

    def top(self):
        if self.isEmpty():
            print("Empty stack")
        else:
            return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0


# Queue implementation using array
class ArrayQueue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, x):
        self.queue.append(x)
    
    def dequeue(self):
        if self.isEmpty():
            print("Dequeuing from empty queue")
        else:
            self.queue.pop(0)
    
    def front(self):
        if self.isEmpty():
            print("Empty queue")
        else:
            return self.queue[0]
    
    def isEmpty(self):
        return len(self.queue) == 0
