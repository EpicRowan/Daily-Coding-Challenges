''' How can we print the number of words in descending order by count?
{'dog': 2, 'apple': 1, 'cat': 3}'''

def dict_order(dict):
	counts = [(count, word) for word, count in dict.items()]
	counts.sort()
	for count, word in counts:
		print('f{count}: {word}')