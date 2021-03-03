''' Write a function that divides an amount into possible change that could
be made from that amount 

27 -> [25, 1, 1]

'''
#first impulse, recursive

def make_change(num, result=[]):
    coins = [25, 10, 5, 1]
    if num < 1:
        return result
    for change in coins:
        if change <= num:
            result.append(change)
            num -= change
            return make_change(num, result)

