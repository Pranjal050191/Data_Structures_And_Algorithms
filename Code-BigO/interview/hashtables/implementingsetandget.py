class HashTable:
    def __init__(self,size:int,default_value=None) -> None:
        self.size = size
        self.data = [default_value] * size
        #data is a list of given size and default value
    def __hash__(self,key) -> int:
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i]) * i) % len(self.data)
        return hash
    def set(self,key,value):
        address = self.__hash__(key)
        if not (self.data[address]):
            self.data[address] = [] # to handle collision we declare an empty list first and then append values
        self.data[address].append([key,value])
        # print(self.data)
        return self.data
    def get(self,key):
        address = self.__hash__(key)
        currentBucket = self.data[address]
        if (currentBucket):
            for i in range(len(currentBucket)):
                if(currentBucket[i][0] == key):
                    #print(currentBucket[i][1])
                    return currentBucket[i][1]
        return None
    def keys(self):
        keysArray = list()
        for i in range(len(self.data)):
            if(self.data[i]):
                for j in range(len(self.data[i])):
                    # print(self.data[i][j][0])
                      keysArray.append(self.data[i][j][0])
        return keysArray
    def values(self):
        keysArray = list()
        for i in range(len(self.data)):
            if(self.data[i]):
                for j in range(len(self.data[i])):
                    # print(self.data[i][j][0])
                      keysArray.append(self.data[i][j][1])
        return keysArray
myHashTable = HashTable(2)
myHashTable.set('grapes',1000)
myHashTable.set('apples',54)
myHashTable.set('oranges',2)
print(f'{myHashTable.keys()}') 
print(f'{myHashTable.values()}') 
# myHashTable.keys()