''' Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.


Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]'''


#first idea, inefficient

def collect_anagrams(arr):
    results = []
    for i in range(len(arr)-1):
        for j in range(1,len(arr)-2):
            x =''.join(sorted(arr[i]))
            y = ''.join(sorted(arr[j]))
            if x == y:
                results.append([arr[i], arr[j]])
    return results

print(collect_anagrams(["eat","tea","tan","ate","nat","bat"]))
