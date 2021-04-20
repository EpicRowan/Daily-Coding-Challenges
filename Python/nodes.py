
'''Create a node class'''

class Node:
	def __init__(self, data, next=None):
		self.data = data
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


'''Add a .remove_node() method to LinkedList. It should take value_to_remove as a parameter.
 We'll be looking for a node with this value to remove.'''

 	def remove_node(self, value_to_remove):

		current_node = self.head
		if current_node.data == value_to_remove:
			self.head = current_node.next
		else:
			while current_node:
				next_node = current_node.next
				if next_node.data == value_to_remove:
					current_node.next(next_node.next)
					current_node = None
				else:
					current_node = next_node