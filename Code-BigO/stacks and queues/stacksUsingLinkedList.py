class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class Stack:
    def __init__(self):
        self.bottom = None
        self.top =  None
        self.length = 0
    def peek(self):
        if(self.top):
            print(self.top.value)
        else:
            print('None')

    def push(self,value):
        node1 = Node(value)
        if (self.length == 0):
            self.top = node1
            self.bottom = self.top
        else:
            node1.next = self.top
        self.top = node1
        self.length = self.length + 1
        print(node1.value)

    def pop(self):
        if(self.top):
            self.top = self.top.next
            self.length = self.length - 1
        if (self.top == self.bottom):
            self.bottom = None
        else:
            print('None')

myStack = Stack()
myStack.peek()
myStack.push('google')
myStack.push('udemy')
myStack.push('discord')
myStack.peek()
myStack.pop()
myStack.peek()
myStack.pop()
myStack.peek()
myStack.pop()
# print(vars(myStack))
# print(myStack.top.value)
print(myStack.bottom)