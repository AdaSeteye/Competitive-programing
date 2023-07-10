class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.left = 0
        self.capacity = k
        self.size = 0
        self.right = -1
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.right += 1
        self.right %= self.capacity
        self.queue[self.right] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.left += 1
        self.left %= self.capacity
        self.size -= 1
        return True

    def Front(self) -> int:
        if not self.isEmpty():
            return self.queue[self.left]
        return -1

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.queue[self.right]
        return -1

    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        return False

        

    def isFull(self) -> bool:
        if self.size == self.capacity:
            return True
        return False
