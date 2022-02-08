class MinStack:

    lifo = None
    minimum = None

    def __init__(self):
        self.lifo = []
        self.minimum = [inf]

    def push(self, val: int) -> None:
        self.lifo.append(val)
        if val <= self.minimum[-1]:
            self.minimum.append(val)

    def pop(self) -> None:
        if self.lifo.pop() == self.minimum[-1]:
            self.minimum.pop()

    def top(self) -> int:
        return self.lifo[-1]

    def getMin(self) -> int:
        return self.minimum[-1]