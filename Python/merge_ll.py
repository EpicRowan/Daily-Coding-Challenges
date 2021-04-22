''' Merge two sorted linked lists and return it 
	as a new sorted list.'''

def merge_ll(lst1, lst2):
	dummy = current = self.head
	while lst1 and lst2:
        if lst1.value < lst2.value:
            current.next = lst1
            lst1 = lst1.next
        else:
            current.next = lst2
            lst2 = lst2.next
        current = current.next
    current.next = lst1 or lst2
    return dummy.next