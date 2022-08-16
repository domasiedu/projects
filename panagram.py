import string, sys

"""
Note : Pangrams are words or sentences containing every 
letter of the alphabet at least once.
"""


def pangram(string1: object, alphabet: object = string.ascii_lowercase) -> object:
    allset = set(alphabet)
    return allset <= set(string1.lower())


print((pangram('The quick brown fox jumps over the lazy dog')))


"""
SIMPLER VERSION 1

"""

def is_pangram(s, alphabet=string.ascii_lowercase):
    allset = set(alphabet)
    return allset <= set(s.lower())
"""
SIMPLER VERSION 2

"""

def is_pangram(s):
    s = s.lower()
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in s:
            return False
    return True
