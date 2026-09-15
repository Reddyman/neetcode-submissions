class MyStack:

    def __init__(self):
        self.queueA = []
        self.queueB = []

    def push(self, x: int) -> None:
        self.queueA.append(x)

    def pop(self) -> int:
        self.flush()
        return self.queueB.pop()

    def top(self) -> int:
        self.flush()
        return self.queueB[-1]
        
    def empty(self) -> bool:
        self.flush()
        return len(self.queueB) == 0

    def flush(self):
        while (self.queueA):
            self.queueB.append(self.queueA.pop(0))


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()