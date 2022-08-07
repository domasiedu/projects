'''BINARY SEARCH ALGORITHM FUNCTION'''


def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last) // 2

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None


'''VERIFYING THE BINARY SEARCH ALGO'''


def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in the list")


"""NB: numbers/List needs to be sorted"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

'''Here the numbers is referencing the List in the fxn, 12 references the 12'''

result = binary_search(numbers, 10)
verify(result)
