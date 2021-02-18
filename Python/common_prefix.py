''' Write a function to find the longest common prefix string 
	in an array of strings.
	If there is no common prefix, return an empty string.'''

def common_pre(arr):
    arr.sort()
    prefix = ""
    for first, last in zip(arr[0], arr[-1]):
        if first == last:
            prefix += first
        else:
            break
    return prefix
	