
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert(self, value):
        if value >= self.data:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)
        else:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()


def invertTree(root):
    if not root:
        return
    invertTree(root.left)
    invertTree(root.right)

    root.left, root.right = root.right, root.left


def max_depth(root):
    if root is None:
        return 0
    left = max_depth(root.left)
    right = max_depth(root.right)
    if left > right:
        return left + 1
    else:
        return right + 1


A = Node(1)

A.insert(2)
A.insert(3)
A.insert(5)
# A.PrintTree()
print("Height of tree is %d" % (max_depth(A)))
print(max_depth(A))
