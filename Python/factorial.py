''' Create a function that returns the factorial of it. 
For example: if num = 4, then your program should return 
(4 * 3 * 2 * 1) = 24  '''


# iterative solution

def factorial(num):
	result = num
    for i in range(1, num):
        result = result * i
    return result

# recursive solution

def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num-1)
