class Stack:
    def __init__(self):
        self.bottom = None
        self.top =  None
        self.length = 0
        self.arr = list()
    def peek(self):
        if(self.length == 0):
            print('None')
        else:
            print(self.top)
    def push(self,value):
       self.arr.append(value)
       if(self.length == 0):
           self.top = self.arr[0]
           self.bottom = self.arr[0]
    #  print(f'Pranjal : {self.arr[self.length]}')
       else:
           self.top = self.arr[self.length]
       self.length = self.length + 1

    def pop(self):
        if(self.length > 1):
            self.arr.pop()
            self.length = self.length - 1
            self.top = self.arr[self.length-1]
        elif(self.length == 1):
            self.arr.pop()
            self.length = self.length - 1
            self.bottom = None
            self.top = None
        else:
            print('None')
       

myStack = Stack()
myStack.peek()
myStack.push('google')
myStack.push('udemy')
myStack.push('discord')
print(myStack.arr)
myStack.peek()
myStack.pop()
myStack.peek()
myStack.pop()
myStack.peek()
myStack.pop()
# # print(vars(myStack))
# # print(myStack.top.value)
# print(myStack.bottom)
print(myStack.arr)