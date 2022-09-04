"""
Multiple function arguments
"""


def foo(first, second, third, *therest):
    print("First: %s" % (first))
    print("Second: %s" % (second))
    print("Third: %s" % (third))
    print("And all the rest... %s" % (list(therest)))


foo(1, 2, 3, 4, 5)


# Second Example

def bar(first, second, third, **options):
    if options.get("action") == "sum":
        print("The sum is: %d" % (first + second + third))

    if options.get("number") == "first":
        return first


result = bar(1, 2, 3, action="sum", number="first")
print("Result: %d" % (result))

"""
Fill in the foo and bar functions so they can receive a variable amount of arguments (3 or more) 
The foo function must return the amount of extra arguments received. 
The bar must return True if the argument with the keyword magicnumber is worth 7, and False otherwise.
"""


# Example Three

def foo(a, b, c, *d):
    return (len(d))
    pass


def bar(a, b, c, **options):
    if options.get("magicnumber") == 7:
        return True
    else:
        return False
    pass


# test code
if foo(1, 2, 3, 4) == 1:
    print("Good.")
if foo(1, 2, 3, 4, 5) == 2:
    print("Better.")
if bar(1, 2, 3, magicnumber=6) == False:
    print("Great.")
if bar(1, 2, 3, magicnumber=7) == True:
    print("Awesome!")
