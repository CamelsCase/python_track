class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        if not self.is_empty():
            return self.stack.pop()

    def top(self) -> int:
        if not self.is_empty():
            return self.stack[-1]

    def getMin(self) -> int:
        if not self.is_empty():
            return min(self.stack)

    def is_empty(self) -> bool:
        return len(self.stack) == 0