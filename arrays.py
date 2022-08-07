# Data Structures

new_list = [1, 2, 3]
result = new_list[0]

if 1 in new_list: print(True)

for n in new_list:
    if n == 1:
        print(True)
        break
new_list.append(10)
new_list.extend([4, 5, 6, 7, 8])
new_list.sort()
# We have .insert() and .delete() as well
print(new_list)
