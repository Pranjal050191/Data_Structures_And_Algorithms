# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.
class MinStack:

    def __init__(self):
        self.arr = list()
        self.topp = None
        self.l = -1
        

    def push(self, val: int) -> None:
        self.arr.append(val)
        self.l = self.l+1
        self.topp = self.arr[self.l]
        print(self.arr)


        

    def pop(self) -> None:
        if(self.l > 0):
            self.arr.pop()
            self.l = self.l - 1
            self.topp = self.arr[self.l]
        elif(self.l == 0):
            self.arr.pop()
            self.l = self.l - 1
            self.topp = None
        print(self.arr)
        

    def top(self) -> int:
        return self.arr[self.l]
        

    def getMin(self) -> int:
        return min(self.arr)
        


# Your MinStack object will be instantiated and called as such:
minStack = MinStack()
minStack.push(2147483646)
minStack.push(2147483646)
minStack.push(2147483647)
print(minStack.top())
minStack.pop()
print(minStack.getMin())
minStack.pop()
print(minStack.getMin())
minStack.pop()
minStack.push(2147483647)
print(minStack.top())