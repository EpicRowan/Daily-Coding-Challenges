''' Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]'''

#first idea, assumes two numbers grouped will be part of solution

def sum_of_three(arr):
	two_sum = 0
	result = []
	for i in range(len(arr-1)):
		two_sum = arr[i] + arr[i+1]
		if two_sum < 0:
			if abs(two_sum) in arr:
				result.append(arr[i], arr[i+1], abs(two_sum))
	return result
