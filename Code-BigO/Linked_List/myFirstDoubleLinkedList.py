class DoublyLinkedList:
    def __init__(self,value) -> None:
        self.head = {
            'previous': None
            ,'value': value
            ,'next': None
        }
        self.tail = self.head
        self.length = 1
    def append(self,value):
        newNode = {
            'value': value
            ,'next': None
            ,'previous': None
        }
        newNode['previous'] = self.tail
        self.tail['next'] = newNode # this updates head.next as well.
        self.tail = newNode
        self.length =self.length + 1
        return self
    def prepend(self,value):
        newNode1 = {
            'value': value
            ,'next': self.head
            ,'previous': None
        }
        self.head['previous'] = newNode1 
        self.head = newNode1
        self.length =self.length+ 1
        return self
    def printList(self):
        array1  = list()
        currentNode =  self.head
        while (currentNode != None):
            array1.append(currentNode['value'])
            currentNode = currentNode['next']
        print(array1)
    def insert(self,index,value):
        if (index > self.length):
            return self.append(value)
        elif(index == 0):
            self.prepend(value)
            return self.printList()
        newNode = {
            'value': value
            ,'next': None
            ,'previous': None
        }
        leader = self.traverseToIndex(index-1)
        follower = leader['next']
        leader['next'] = newNode
        newNode['previous'] = leader
        newNode['next'] = follower
        follower['previous'] = newNode
        self.length = self.length + 1
        print(f'Pranjal {self.__dict__}')
        return self.printList()
    def traverseToIndex(self,index):
        counter = 0
        currentNode = self.head
        while(counter != index):
            currentNode = currentNode['next']
            counter = counter + 1
        return currentNode
    def remove(self,index):
        if (index == 0):
            self.head = self.head['next']
            self.length = self.length - 1
            return self.printList()
        elif (index >= self.length) or (index == self.length-1):
            # currentNode = self.head
            # for i in range(self.length-2):
            #     currentNode = currentNode['next']
            currentNode = self.traverseToIndex(self.length - 2)
            currentNode['next'] =  None
            self.length = self.length - 1
            self.tail = currentNode
            return self.printList()
        else:
            leader = self.traverseToIndex(index-1)
            follower = leader['next']
            follower_next = follower['next']
            leader['next'] = follower['next']
            follower_next['previous'] = follower['previous']
            self.length = self.length - 1
            return self.printList()

myLinkedList = DoublyLinkedList(10)
myLinkedList.append(5)
myLinkedList.append(16)
myLinkedList.prepend(1)
# print(myLinkedList.__dict__)
myLinkedList.printList()
myLinkedList.insert(200,99)
# print(myLinkedList.tail)
myLinkedList.insert(2,99)
myLinkedList.insert(0,45)
myLinkedList.remove(2)
myLinkedList.remove(0)
myLinkedList.remove(99)
myLinkedList.remove(3)
# print(myLinkedList.__dict__) 
# # # print(myLinkedList.head['next'])