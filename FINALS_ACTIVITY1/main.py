from LinkedStack import LinkedStack as Stack
from LinkedQueue import LinkedQueue as Queue
from LinkedDeque import LinkedDeque as Deque
Q = Queue()
S = Stack()
D = Deque()

D.insert_last(1)
D.insert_last(2)
D.insert_last(3)
D.insert_last(4)
D.insert_last(5)
D.insert_last(6)
D.insert_last(7)
D.insert_last(8)

Q.enqueue(D.delete_first())#1
Q.enqueue(D.delete_first())#12
Q.enqueue(D.delete_first())#123
D.insert_last(D.delete_first())#5674
Q.enqueue(D.delete_first())#1235
Q.enqueue(D.delete_last())#12354
Q.enqueue(D.delete_first())#123546
Q.enqueue(D.delete_first())#1235467
Q.enqueue(D.delete_first())#12354678

D.insert_last(Q.dequeue())
D.insert_last(Q.dequeue())
D.insert_last(Q.dequeue())
D.insert_last(Q.dequeue())
D.insert_last(Q.dequeue())
D.insert_last(Q.dequeue())
D.insert_last(Q.dequeue())
D.insert_last(Q.dequeue())
print("Using Dequeue and Queue elements in D:")
print("D: [1,2,3,5,4,6,7,8]")
while not D.is_empty():
    print(D.delete_first())

D.insert_last(1)
D.insert_last(2)
D.insert_last(3)
D.insert_last(4)
D.insert_last(5)
D.insert_last(6)
D.insert_last(7)
D.insert_last(8)

S.push(D.delete_first())#1
S.push(D.delete_first())#12
S.push(D.delete_first())#123
S.push(D.delete_last())#1238
S.push(D.delete_last())#12387
S.push(D.delete_last())#123876
S.push(D.delete_first())#1238764
S.push(D.delete_first())#12387645

D.insert_last(S.pop())
D.insert_last(S.pop())
D.insert_last(S.pop())
D.insert_last(S.pop())
D.insert_last(S.pop())
D.insert_first(S.pop())
D.insert_first(S.pop())
D.insert_first(S.pop())
print("Using Dequeue and Stacks elements in D:")
print("D: [1,2,3,5,4,6,7,8]")
while not D.is_empty():
    print(D.delete_first())







