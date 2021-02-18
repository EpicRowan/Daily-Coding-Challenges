'''We want to check if two strings are, at most, one edit away from being the same. 
	An edit is adding, deleting, or changing a single letter.
	So, for example, "make" can be turned into "fake" by just changing one letter'''


def two(str1,str2):
    if abs(len(str1) - len(str2)) > 1:
        return False
    edits = 0
    for x,y in zip(str1, str2):
        if x!= y:
            edits +=1
    if abs(len(str1) - len(str2)) == 1:
        edits += 1

    return edits <= 1