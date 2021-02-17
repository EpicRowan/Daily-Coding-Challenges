''' Find the length of the sequence in an array, 
	between the first and the second occurrence of a specified number.'''

# first solution, established find() cannot be used in lists but index() can

def box(arr, num):
    first = arr.index(num)
    second = arr.index(num, first+1)
    return second - first