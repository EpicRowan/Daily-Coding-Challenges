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

def isPalindrome(str):
	s = s.lower()
	start = 0
	end = len(s)- 1
	while start < end:
		if not s[start].isalnum():
			start += 1
		elif not s[end].isalnum():
			end -= 1
		else:
			if s[start].lower() != s[end].lower():
				return False
			else:
				start += 1
				end -= 1
	return True

''' Follow-up: Check if a linked list is a palindrone'''

def is_palindrome(ll):
    fast = slow = ll.head
    stack = []

    while fast and fast.next:
        stack.append(slow.value)
        slow = slow.next
        fast = fast.next.next

    if fast:
        slow = slow.next

    while slow:
        top = stack.pop()

        if top != slow.value:
            return False

        slow = slow.next

    return True