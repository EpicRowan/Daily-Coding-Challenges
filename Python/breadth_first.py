''' Implement a breadth first search'''

#iterative

def breadth(self):
    queue = []
    visited = []
    queue.append(self.root)

    while queue:
        current = queue.pop()
        visited.append(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    
    return visited
    