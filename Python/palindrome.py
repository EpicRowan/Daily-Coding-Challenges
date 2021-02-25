''' Check for a palindrone without using sorted.'''

def challenge(str):
    start = 0
    end = len(str)-1
    while start < end:
        if str[start] != str[end]:
            return False
        start += 1
        end -= 1
    return True

# refactor: ignore cases and makes cases like
# "A man, a plan, a canal: Panama" 
# read as true