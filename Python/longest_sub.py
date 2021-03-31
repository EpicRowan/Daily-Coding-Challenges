''' Given a string s, find the length of the longest substring without 
repeating characters.

Input: s = "abcabcbb"
Output: 3'''

def lengthOfLongestSubstring(s):
    start = 0
    maxLength = 0
    usedChar = {}
    for index,char in enumerate(s):
        if char in usedChar and start <= usedChar[char]:
            start = usedChar[char] + 1
            
        else:
            maxLength = max(maxLength, index - start + 1)
        usedChar[char] = index
    return maxLength