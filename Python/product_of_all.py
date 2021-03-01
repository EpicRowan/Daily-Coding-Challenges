'''You have a list of integers, and for each index you want to find the product 
of every integer except the integer at that index.

  [1, 7, 3, 4]  ->

  [84, 12, 28, 21] ->

  [7 * 3 * 4,  1 * 3 * 4,  1 * 7 * 4,  1 * 7 * 3]'''

def product_except(arr):

    # We make a list with the length of the input list to
    # hold our products
	products_of_all_except_at_index = [None] * len(arr)
	product_so_far = 1


	 # For each integer, we find the product of all the integers
    # before it, storing the total product so far each time
    # example: [1,2,3] -> 	[1, None, None]
	#						[1, 1, None]
	#						[1, 1, 2]

    for i in range(len(arr)):
        products_of_all_except_at_index[i] = product_so_far
        product_so_far *= arr[i]

	#going backwards through list

	# For each integer, we find the product of all the integers
    # after it. since each index in products already has the
    # product of all the integers before it, now we're storing
    # the total product of all other integers

    # example: [1,2,3] -> 	[None, None, 1]
	#						[None, 3, 1]
	#						[6, 3, 1]

	for i in range(len(arr) - 1, -1, -1):
		products_of_all_except_at_index[i] = product_so_far
		product_so_far *= arr[i]

	return products_of_all_ints_except_at_index