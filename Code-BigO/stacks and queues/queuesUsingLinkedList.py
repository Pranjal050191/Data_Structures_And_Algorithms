class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class Queue:
    def __init__(self):
        self.first = None
        self.last =  None
        self.length = 0
    def peek(self):
        if(self.length == 0):
            print('None')
        else:
            print(self.first.value)

    def enqueue(self,value):
        node1 = Node(value)
        if(self.length == 0):
            self.first = node1
            self.last = node1
        else:
            self.last.next = node1
            self.last = node1
        self.length = self.length + 1
        return self
    def dequeue(self):
        if(self.first.value):
            print(self.first.value)
        if(self.length == 0):
            print('None')
        elif(self.length == 1):
            self.first = None
            self.last = None
            self.length = 0
        else:
            self.first = self.first.next
            self.length = self.length - 1

myQueue = Queue()
myQueue.peek()
myQueue.enqueue('Joy')
myQueue.enqueue('Matt')
myQueue.enqueue('Pavel')
myQueue.enqueue('Samir')
myQueue.peek()
myQueue.dequeue()
myQueue.peek()
myQueue.dequeue()
myQueue.peek()
myQueue.dequeue()
myQueue.dequeue()
print(vars(myQueue))
# # print(myQueue.top.value)
# print(myQueue.bottom)