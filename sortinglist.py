"""
Sorting a list of integers in Descending Order
"""


# First function considers 0 - 9
def descending_Order(num):
    return int("".join(map(str, sorted([i for i in str(num)], reverse=True))))


print(descending_Order(2376489011))


# Second function

def descending_Order1(num):
    return int("".join(sorted(str(num), reverse=True)))


print(descending_Order1(2376489011))


# Third function  works differently

def descending_Order2(num1):
    return int(str(num1)[::-1])


print(descending_Order2(2376489011))
