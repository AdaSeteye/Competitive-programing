class MyCircularDeque:

    def __init__(self, k: int):
        self.queue = []
        self.maxSize = k

    def insertFront(self, value: int) -> bool:
        if len(self.queue) < self.maxSize:
            self.queue.append(value)
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if len(self.queue) < self.maxSize:
            self.queue.insert(0, value)
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if len(self.queue) == 0:
            return False
        else:
            self.queue.pop()
            return True

    def deleteLast(self) -> bool:
        if len(self.queue) == 0:
            return False
        else:
            self.queue.pop(0)
            return True

    def getFront(self) -> int:
        if len(self.queue) == 0:
            return -1
        else:
            return self.queue[-1]

    def getRear(self) -> int:
        if len(self.queue) == 0:
            return -1
        else:
            return self.queue[0]

    def isEmpty(self) -> bool:
        if len(self.queue) == 0:
            return True
        else:
            return False


    def isFull(self) -> bool:
        if len(self.queue) == self.maxSize:
            return True
        else:
            return False
