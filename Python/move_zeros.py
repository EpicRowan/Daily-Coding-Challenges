'''Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]'''


# inital idea, doesn't yield correct solution because zeros
# get left behind

def move_zeroes(arr):
	for i in range(len(arr)-1):
		if arr[i] == 0:
			arr[i], arr[i+1] = arr[i+1], arr[i]
	return arr

# refactored
def move_zeroes(arr):
	index_a = 0
	index_b = 0
	while index_a < len(arr):
		if arr[index_a] != 0:
			arr[index_a], arr[index_b] = arr[index_b], arr[index_a]
		if arr[index_b] != 0:
			index_b += 1
		index_a += 1
	return arr