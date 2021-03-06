'''Given two already-sorted lists:
	>>> a = [1, 3, 5, 7]
	>>> b = [2, 6, 8, 10]
	Write a function that returns a new list that is 
	the sorted merge of both of them.'''

def sorted_lists(lst1,lst2):
	lst1_dex = 0
	lst2_dex = 0
	sorted = []
	for item in lst1:
		if item[lst1_dex] < lst2[lst2_dex]:
			sorted.append(item)
			lst1_dex += 1
		else:
			sorted.append(lst2[lst2_dex])
			lst2_dex += 1
	return sorted

# Refactored to account for leftover numbers

def sorted_lists(lst1,lst2):
    lst1_dex = 0
    lst2_dex = 0
    sorted = []
    while lst1_dex < len(lst1) and lst2_dex < len(lst2):
        if lst1[lst1_dex] < lst2[lst2_dex]:
            sorted.append(lst1[lst1_dex])
            lst1_dex += 1
        else:
            sorted.append(lst2[lst2_dex])
            lst2_dex += 1
        sorted.extend(lst1[lst1_dex:])
        sorted.extend(lst2[lst2_dex:])
        return sorted
