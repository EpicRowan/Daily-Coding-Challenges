''' Write a function to return the mean, median, and mode 
	of a list of numbers.'''

def mean(arr):
    return sum(arr) / int(len(arr))

def median(arr):
    arr = sorted(arr)
    return arr[int(len(arr)/2)]


#refactored to account for multiple modes in a list

def mode(arr):
    dict = {}
    mode = []
    for item in arr:
        dict[item] = dict.get(item,0)+1

    highest = max(list(dict.values()))
    return [num for num, count in dict.items() if count == highest]