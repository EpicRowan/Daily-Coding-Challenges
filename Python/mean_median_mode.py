''' Write a function to return the mean, median, and mode 
	of a list of numbers.'''

def mean(arr):
    return sum(arr) / int(len(arr))

def median(arr):
    arr = sorted(arr)
    return arr[int(len(arr)/2)]


#only works if only single number is mode
def mode(arr):
    dict = {}
    mode = 0
    for item in arr:
        dict[item] = dict.get(item,0)+1
    for item in dict:
        if dict[item] > mode:
            mode = item
    return mode