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
    def breadth_first_search(self):
        if not self.root:
            return []
        queue = [self.root]
        result = []
        while queue:
            current_node = queue.pop(0) # get the first node in the queue
            result.append(current_node.value) # Process the node
            #Add left and right children to the queue
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        return result
    
    # Recursive BFS implementation
    def breadth_first_search_recursive(self, queue, result):
        if len(queue) == 0:
            return result  # Base case: If the queue is empty, return the result list

        current_node = queue.pop(0)  # Process the first node in the queue
        result.append(current_node.value)  # Add the current node's value to the result list

        # Add the left and right children to the queue for the next level (if they exist)
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

        # Recursive call with the updated queue and result list
        return self.breadth_first_search_recursive(queue, result)

    def bfs(self):
        # Initiating the recursive BFS with the root node and an empty result list
        if not self.root:
            return []
        return self.breadth_first_search_recursive([self.root], [])
    
    def in_order_traversal_pranjal(self, node):
        if (node is not None):
            # print(f'checking node {node.value}')
            self.in_order_traversal_pranjal(node.left)
            print (node.value)
            self.in_order_traversal_pranjal(node.right)

    def pre_order_traversal(self, node):
        if (node is not None):
            print (node.value,end= ' ')
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)

    def post_order_traversal(self, node):
        if (node is not None):
            # print(f'Pranjal {node.value}')
            self.post_order_traversal(node.left)
            # print(node.value,end = ' ')
            self.post_order_traversal(node.right)
            print(node.value,end = ' ')


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

print('Tree created at this stage is:')
tree.in_order_traversal(tree.root)
print('\nBreadth First Search result:')
print(tree.breadth_first_search())  # Output will show BFS traversal
print('\nBreadth First Search result (Recursive):')
print(tree.bfs())  # Output will show BFS traversal

print('Pre order Depth First Search in tree')
tree.pre_order_traversal(tree.root)

print(' ')
print('Post order Depth First Search in tree')
tree.post_order_traversal(tree.root)
print(' ')

tree.removal(1)
tree.removal(4)
tree.removal(87)
tree.removal(170)
tree.removal(9)
tree.in_order_traversal(tree.root)
print('checking')
tree.in_order_traversal_pranjal(None)