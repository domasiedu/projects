"""
Copy in Python
Exploring Shallow and Deep Copy
"""

# Shallow copy
import copy
x = [1, 2, [3,5], 4]
y = copy.copy(x)
y[2][0] = 5
print(x)
print(y)


# Deep Copy

x = [1, 2, [3,5], 4]
y = copy.deepcopy(x)
y[2][0] = 5
print(x)
print(y)

