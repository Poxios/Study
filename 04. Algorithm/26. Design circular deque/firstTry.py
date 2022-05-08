class MyCircularDeque:
# deque -> same as queue, but it can push / pop to both left, right side
# Double Linked List
    def __init__(self, k: int):
        self.MAX_LEN = k+1
        self.l = [0] * (k+1)
        self.front = 0
        self.rear = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.front = (self.front - 1 + self.MAX_LEN) % self.MAX_LEN
        self.l[self.front] = value
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.l[self.rear] = value
        self.rear = (self.rear + 1) % self.MAX_LEN
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.MAX_LEN
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1 + self.MAX_LEN) % self.MAX_LEN
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.l[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.l[(self.rear-1+self.MAX_LEN) %self.MAX_LEN]

    def isEmpty(self) -> bool:
        return self.front == self.rear

    def isFull(self) -> bool:
        return (self.rear + 1) % self.MAX_LEN == self.front


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()