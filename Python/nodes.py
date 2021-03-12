
'''Create a node class'''

class Node:
	def __init__(self, data, next=None):
		self.data = data
		self.next = None
		self.next=next

'''Create a LinkedList class with insert 
and print methods.'''

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,data):
        newNode = Node(data)
    #does the list have a head?
        if self.head:
            current=self.head
        #is there a next node?
            while current.next:
                current=current.next
        #end of list, insert data
            current.next =newNode
        else:
            self.head = newNode
    
    def printLL(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next