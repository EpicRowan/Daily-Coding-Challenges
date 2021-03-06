# Given list of ints, return True if any two nums in list sum to 0.

# >> > add_to_zero([])
# False

# >> > add_to_zero([1])
# False

# >> > add_to_zero([1, 2, 3])
# False

# >> > add_to_zero([1, 2, 3, -2])
# True

def add_to_zero(nums):
    set_nums = set(nums)

    for n in nums:
        if -n in set_nums:
            return True

    return False


print(add_to_zero([1, 2, 3]))
