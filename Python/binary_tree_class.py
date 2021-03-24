'''Create a binary search tree'''

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    

class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, value):
        newNode = Node(value)
        if self.root == None:
            self.root = newNode
        else:
            current = self.root
            while current:
                if value < current.value:
                    if current.left is None:
                        current.left = newNode
                        break
                    current = current.left
                else:
                    if current.right is None:
                        current.right = newNode
                        break
                    current = current.right
                    
    def lookup(self, value):
        current = self.root
        while current is not None:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
        return False