'''Implement a queue class'''


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, first = None, last = None):
        self.first = first
        self.last = last
        self.length = 0
    
    def peek(self):
        return self.first.value

    def enqueue(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.first = newNode
        else:
            self.last.next = newNode
        self.last = newNode
        self.length +=1
    
    def dequeue(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            return self.first
        else:
            holder = self.first.value
            self.first = self.first.next
            self.length -= 1
            if self.length == 1:
                self.last = None

  #       1   -->   2     -->    3
  	# (first)    (first.next)