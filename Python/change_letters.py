'''  Replace every letter in the string with the letter following it in the alphabet 
	(ie. c becomes d, z becomes a). 
	Then capitalize every vowel in this new string (a, e, i, o, u)'''


# first solution, does not account for integers or punctuation

def replace_letters(str):
    alphabet = "abcdEfghIjklmnOpqrstUvwxyz"
    new = ""
    for letter in str.lower():
        if letter == "z":
            new += "A"
        else:
            found = alphabet.find(letter)
            new += alphabet[found+1]
    return new



