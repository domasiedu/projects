''' LINEAR SEARCH ALGORITHM IMPLEMENTATION '''

def linear_search(list, target):
    """
    Returns the index position of the target if found, 
    else returns None """

    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None

'''VERIFYING THE ALGO'''

def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in the list")
    
numbers = [1,2,3,4,5,6,7,8,9,10]


'''Here the numbers is referencing the List in the fxn, 12 references the 12'''

result = linear_search(numbers, 6)
verify(result)