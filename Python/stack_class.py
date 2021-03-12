''' Outline a Stack class with any methods you
would define'''

class Stack:
	
	def __init__(self):
		self.stack = []

	def push(self, item):
		self.stack.append(item)

	def pop(self):
		return self.stack.pop()

	def peek(self):
		return self.stack[-1]

	def is_empty(self):
		return not self.stack