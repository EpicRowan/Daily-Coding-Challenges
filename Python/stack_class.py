''' Outline a Stack class with any methods you
would define'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, top = None, bottom = None):
        self.top = top
        self.bottom = bottom
        self.length = 0
    
    def peek(self):
        return self.top.value
    
    def push(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.top = newNode
            self.bottom = newNode
        else:
            hold = self.top
            self.top = newNode
            self.top.next = hold
        self.length +=1
    
    def pop(self):
        if self.length == 0:
            return None
        elif self.top == self.bottom:
        	self.bottom = None
        else:
            hold = self.top
            self.top = self.top.next
            self.length -= 1
        return hold