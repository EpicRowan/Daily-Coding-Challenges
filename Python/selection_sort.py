'''Implement a selection sort'''

def select_sort(nums):
	   # Traverse through all array elements 
    for i in range(len(nums)): 
      
    # Find the minimum element in remaining  
    # unsorted array 
        min_idx = i 
        for j in range(i+1, len(nums)): 
            if nums[min_idx] > nums[j]: 
                min_idx = j 
              
    # Swap the found minimum element with  
    # the first element         
        nums[i], nums[min_idx] = nums[min_idx], nums[i] 
    return nums