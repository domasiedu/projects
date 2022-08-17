# Mapping 2 to the elements in the arrays below

arr = [10, 20, 30, 40, 50]


def add(num):
    return num + 2


result = list(map(add, arr))

print(result)
