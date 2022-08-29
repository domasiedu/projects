"""
Generators are used to create iterators,
but with a different approach.
Generators are simple functions which return an iterable set of items,
one at a time, in a special way.
"""
import random


def lottery():
    # Returns 6 numbers between 1 & 40
    for i in range(6):
        yield random.randint(1, 40)

    # Returns a 7th number 1 and 15
    yield random.randint(1, 15)


for random_number in lottery():
    print("And the next number is... %d!" % (random_number))


# Fibonacci function using generator


def fib():
    a, b = 1, 1
    while 1:
        yield a
        a, b = b, a + b


# testing the fib code
import types

if type(fib()) == types.GeneratorType:
    print("Good, The fib function is a generator.")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break
a, b = 1, 1
