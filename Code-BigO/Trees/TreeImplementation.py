class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value
class BinarySearchtree:
    def __init__(self) -> None:
        self.root = None
    def insert(self,value):
        node1 = Node(value)
        if(self.root is None):
            self.root = node1
        else:
            currentNode = self.root
            while(True):
                if(value < currentNode.value):
                    if not(currentNode.left):
                        currentNode.left = node1
                        return self
                    currentNode = currentNode.left
                else:
                    if not(currentNode.right):
                        currentNode.right = node1
                        return self
                    currentNode = currentNode.right
    def lookup(self,value):
        currentNode = self.root
        holdingPointer = currentNode
        while(True):
            if(currentNode.value == value):
                return currentNode,holdingPointer
            elif(currentNode.value < value):
                if  (currentNode.right):
                    holdingPointer = currentNode
                    currentNode = currentNode.right
                else:
                    return False,False
            else:
                if (currentNode.left):
                    holdingPointer = currentNode
                    currentNode = currentNode.left
                else:
                    return False,False
    def removal(self,value):
        currentNode,holdingPointer = self.lookup(value)
        if (currentNode) and (holdingPointer):
            print (f'element found proceeding: {value}')
        else:
            print(f'Element doesnt exist. hence exiting: {value}')
            return None
        if (currentNode.left is None) and (currentNode.right is None):
            print(f'In left and right None case, i.e. removing leaf node: {value}')
            if(holdingPointer.value < value):
                holdingPointer.right = None
            else:
                holdingPointer.left = None
        # print(holdingPointer.left,holdingPointer.right)
        elif (currentNode.left is None) or (currentNode.right is None):
            print(f'In left OR right None case, i.e. One side of tree is present: {value}')
            if (holdingPointer.value < value):
                if(currentNode.right):
                    holdingPointer.right = currentNode.right
                else:
                    holdingPointer.right = currentNode.left
            else:
                if(currentNode.left):
                    holdingPointer.left = currentNode.left
                else:
                    holdingPointer.left = currentNode.right
        else:
            print(f'Removing intermediate node, i.e. Both side of tree is present: {value}')
            if(holdingPointer.value < value):
                parentNode = holdingPointer
                leftPointer = currentNode.left
                rightPointer = currentNode.right
                currentNode = currentNode.right
                if(currentNode.left is None) and (currentNode.right is None):
                    currentNode.left = leftPointer
                    parentNode.right = currentNode
                    currentNode.right = None
                    return self
                while(currentNode.left):
                    parentNode = currentNode
                    currentNode = currentNode.left
                    print(f'Traversing to left: {currentNode.value} + {parentNode.value}')
                currentNode.left = leftPointer
                currentNode.right = rightPointer
                holdingPointer.right = currentNode
                parentNode.left = None
            else:
                if(holdingPointer.value >= value):
                    parentNode = holdingPointer
                    leftPointer = currentNode.left
                    rightPointer = currentNode.right
                    currentNode = currentNode.right
                    if(currentNode.left is None) and (currentNode.right is None):
                        currentNode.left = leftPointer
                        currentNode.right = None
                        parentNode.left = currentNode
                        return self
                    else:
                        while(currentNode.left):
                            parentNode = currentNode
                            currentNode = currentNode.left
                            print(f'Traversing to left: {currentNode.value} + {parentNode.value}')
                        currentNode.left = leftPointer
                    currentNode.right = rightPointer
                    holdingPointer.left = currentNode
                    parentNode.left = None
    def in_order_traversal(self, node):
        if node is not None:
            self.in_order_traversal(node.left)
            print(node.value, end=' ')
            self.in_order_traversal(node.right)


tree = BinarySearchtree()
tree.insert(9)
tree.insert(4)
tree.insert(20)
tree.insert(1)
tree.insert(6)
tree.insert(15)
tree.insert(170)
tree.insert(25)
tree.insert(172)
tree.insert(22)
tree.insert(26)
tree.insert(171)
tree.insert(173)
tree.insert(5)
print('Tree created at this stage is')
tree.in_order_traversal(tree.root)
print(tree.lookup(170))
print(tree.lookup(10))
print(tree.lookup(171))
tree.removal(1)
tree.removal(4)
tree.removal(87)
tree.removal(170)
tree.removal(9)
tree.in_order_traversal(tree.root)