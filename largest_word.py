''' Return the longest word in a string.'''


# first solution, does not account for punctuation

def longest(str):
	str = str.split()
	return max(str)

#solution with regex that accounts for punctuation
import re

def longest(str):
	sen = re.sub("[^\w\s]", "", str)
	str = sen.split()
	return max(str)


