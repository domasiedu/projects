"""
Take arrays as inputs and prints in reverse order

"""

# Step 2: take input from the user (let’s say size) and create empty list
size = int(input("Number of Arrays to be created: "))
arr = []

# Adding the elements of the list by taking inputs from the user
for i in range(0, size):
    element = int(input("Please give value for Array index " + str(i) + ": "))
    arr.append(element)

# Printing in reverse order
"""
# First Print option
for i in range(size - 1, -1, -1):
    print(arr[i], end=' ')
"""
# Second Print Option

arr.reverse()
print(arr)

