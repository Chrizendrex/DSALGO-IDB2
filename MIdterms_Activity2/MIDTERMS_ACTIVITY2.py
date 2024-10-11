class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def first(self):
        if self.is_empty():
            return None
        return self.queue[0]

    def size(self):
        return len(self.queue)

    def display(self):
        print(self.queue)
print("----------------------------------------------------")
print("Part 1:")
print("----------------------------------------------------")
print("Values returned are:")
print("OPERATION:     RETURN:")
Q = Queue()
Q.enqueue(5)
print("Q.enqueue(5):")
print("Q.enqueue(3):")
Q.enqueue(3)
print("len(Q):      ", Q.size())
print("Q.dequeue(): ", Q.dequeue())
print("Q.is_empty():", Q.is_empty())
print("Q.dequeue() :", Q.dequeue())
print("Q.is_empty:  ", Q.is_empty())
print("Q.dequeue:   ", Q.dequeue())
Q.enqueue(7)
print("Q.enqueue(7):")
Q.enqueue(9)
print("Q.enqueue(9):")
print("Q.first():   ", Q.first())
Q.enqueue(4)
print("Q.enqueue(4):")
print("len(Q):      ", Q.size())
print("Q.dequeue(): ", Q.dequeue())
Q.display()


print("----------------------------------------------------")
print("Part 2:")
print("----------------------------------------------------")
print("Values returned are:")
print("OPERATION:     RETURN:")

Q2 = Queue()
Q2.enqueue(5)
Q2.enqueue(3)
print("Q2.dequeue():",Q2.dequeue())
Q2.enqueue(2)
Q2.enqueue(8)
print("Q2.dequeue():",Q2.dequeue())
print("Q2.dequeue():",Q2.dequeue())
Q2.enqueue(9)
Q2.enqueue(1)
print("Q2.dequeue():",Q2.dequeue())
Q2.enqueue(7)
Q2.enqueue(6)
print("Q2.dequeue():",Q2.dequeue())
print("Q2.dequeue():",Q2.dequeue())
Q2.enqueue(4)
print("Q2.dequeue():",Q2.dequeue())
print("Q2.dequeue():",Q2.dequeue())

