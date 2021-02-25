'''Given an array, rotate the array to the right by k steps, where k is non-negative.

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4] '''

def rotate(nums, k):
	#rotates k rotations
	for i in range(k):
	previous = nums[-1]
		#rotates end to front one rotation
		for j in range(len(nums)):
		nums[j], previous = previous, nums[j]
	return nums