class MyCircularQueue:

    def __init__(self, k: int):
        self.MAX_LEN = k+1
        self.l = [0] * (k+1)
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.l[self.rear] = value
        self.rear = (self.rear + 1) % self.MAX_LEN
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.MAX_LEN
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.l[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.l[(self.rear-1+self.MAX_LEN) %self.MAX_LEN]

    def isEmpty(self) -> bool:
        return self.front == self.rear

    def isFull(self) -> bool:
        return (self.rear + 1) % self.MAX_LEN == self.front
