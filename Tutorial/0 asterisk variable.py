# in simple words. * here means "take everything what is not taken".
# your example is not that obvious. Assume we have such a snippet:
# a, *b, c = 1, 2,3,4,5,8
# here a takes the first value from the right part, c = the last value,
# and *b is interpreted the last and takes everything left as a list:
# >>> a, *b, c = 1, 2,3,4,5,8
# >>> a
# 1
# >>> c
# 8
# >>> b
# [2, 3, 4, 5]
# >>> print(*b)
# 2 3 4 5
