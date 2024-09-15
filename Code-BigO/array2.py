class MyArray:
    def __init__(self):
        self.length = 0
        self.data = {}
    def get(self,index):
        return self.data.get(index,'Index doesnt exist')
    def push(self,item):
        self.data[self.length] = item
        self.length += 1
        return self.length
    def pop(self):
        lastItem = self.data[self.length-1]
        del self.data[self.length-1]
        self.length -= 1
        return lastItem
    def delete(self,index):
        item = self.data[index]
        self.shiftItems(index)
        return item
    def shiftItems(self,index):
        for i in range(index,len(self.data)-1):
            self.data[i] = self.data[i+1]
        del self.data[self.length-1]
        self.length -= 1
newArray = MyArray()
newArray.push('hi')
newArray.push('you')
newArray.push('!')
# newArray.pop()
# newArray.pop()
newArray.delete(0)
newArray.push('are')
newArray.push('nice')
newArray.delete(1)
print(newArray.data)