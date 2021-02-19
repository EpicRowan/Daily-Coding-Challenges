""" Write a function that takes a list of characters 
	and reverses the letters in place. """


# Must be a list since Python strings are immutable

def challenge(lst):
    left = 0
    right = len(lst) - 1
    while left < right:
        lst[left], lst[right] = lst[right],lst[left]
        left +=1
        right -= 1
    return lst
