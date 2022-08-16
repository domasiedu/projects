"""
Bus stop solution returning Sum
"""


def number(bus_stops):
    sum = 0
    for i in bus_stops:
        sum += i[0] - i[1]
    return sum


# Second function using generator

def number(bus_stop):
    return sum([i[0] - i[1] for i in bus_stop])


# Third function

def number(bus_stops):
    return sum(on - off for on, off in bus_stops)

# Third function
