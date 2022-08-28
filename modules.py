"""
In this exercise, print an alphabetically sorted list of all
the functions in the 're module' containing the word find.
"""

import re

dir(re)
find_members = []
for member in dir(re):
    if "find" in member:
        find_members.append(member)
find_members.sort()
print(find_members)
