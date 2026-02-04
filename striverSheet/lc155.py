class MinStack:

    def __init__(self):
        self.s = []
        self.min = []

    def push(self, val: int) -> None:
        self.s.append(val)
        if len(self.min) == 0:
            self.min.append(val)
        elif val < self.min[-1]:
            self.min.append(val)

    def pop(self) -> None:
        if len(self.s):
            x = self.s.pop()
            if len(self.min) and x == self.min[-1]:
                self.min.pop()

    def top(self) -> int:
        if len(self.s)>0:
            return self.s[-1]

    def getMin(self) -> int:
        if len(self.min):
            return self.min[-1]
    
minStack = MinStack()
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
print(minStack.s)
print(minStack.getMin())
minStack.pop();
print(minStack.s);
print(minStack.getMin())