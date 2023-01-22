class MyQueue:

    def __init__(self):
        self.lst = []

    def push(self, x: int) -> None:
        self.lst.insert(0, x)

    def pop(self) -> int:
        removed = self.lst.pop()
        return removed

    def peek(self) -> int:
        return self.lst[-1]

    def empty(self) -> bool:
        if len(self.lst) == 0:
            return True
        else:
            return False
