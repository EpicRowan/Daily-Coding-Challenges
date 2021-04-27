''' Replace att spaces in a string with "%" '''

def challenge(str):
    return "".join([x if x != " " else "%" for x in str])

def urlify_pythonic(text, length):
    """solution using standard library"""
    return text.rstrip().replace(" ", "%20")