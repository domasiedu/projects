"""
Enumerates/Adds a counter to each element in the array
syntax:  enumerater(iterable, starting=0)
"""
name = ['ram', 'mohan', 'niraj']
for item in enumerate(name, start=1):
  print(item)

#Second code

name = ['ram', 'mohan', 'niraj']
for index, item in enumerate(name):
  print(item) 
