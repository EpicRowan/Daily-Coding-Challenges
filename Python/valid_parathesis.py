''' Determine if the input string has valid opening and closing brackets.
	An input string is valid if:
	-Open brackets must be closed by the same type of brackets.
	-Open brackets must be closed in the correct order'''


# Solution assumes no characters other than those in dictionary

def valid_brackets(str):
    dict = { "}" : "{", ")" : "(","]" : "["}
    stack = ["{""["]
    for item in str:
    	# if closing bracket
        if item in dict:
        	# take the most recent item off the top of the stack
            top_stack = stack.pop()
            # if the popped item isn't the matching opening bracket
            # then it's invalid and return false
            if dict[item] != top_stack:
                return False
        else:
            stack.append(item)
            
    return not stack 

