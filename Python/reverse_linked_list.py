""" Reverse a singly linked list."""

class ListNode:
	def __init__(self, value=0, next=None):
		self.value = value
		self.next = next

#iterative

def reverse(self, head):
	current = head
	previous = None
	while current:
		current.next = previous
		previous = current
		current = current.next
	return previous


# Recursive

def reverseList_v1(self, head): 

	if not head or not head.next:
		return head
	p = self.reverseList(head.next)
	head.next.next = head
	head.next = None
	return p