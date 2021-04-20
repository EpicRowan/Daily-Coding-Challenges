''' Remove duplicates from a Linked List. 
How would you do it if a temporary buffer isn't allowed?'''

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LL:
    def __init__(self, head):
        self.head = head

    def dups(self):
        seen = [current.value]
        current = self.head
        while current.next:
            if current.next.value in seen:
                current.next = current.next.next
            else:
                seen.add(current.next.value)
                current = current.next

# Follow-up


	def dups_followup(ll):
	    if ll.head is None:
	        return

	    current = ll.head
	    while current:
	        runner = current
	        while runner.next:
	            if runner.next.value == current.value:
	                runner.next = runner.next.next
	            else:
	                runner = runner.next
	        current = current.next

	    return ll.head