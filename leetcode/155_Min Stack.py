class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> None:
        if len(self.stack) <= 0:
            return

        ret = self.stack[-1]
        del self.stack[-1]
        return ret

    def top(self) -> int:
        if len(self.stack) <= 0:
            return

        return self.stack[-1]

    def getMin(self) -> int:
        if len(self.stack) <= 0:
            return

        return min(self.stack)
