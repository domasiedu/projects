"""
Building a tower with stars and spaces
Build a pyramid-shaped tower given a positive
integer number of floors. A tower block is represented with "*" character.

"""


# First code

def tower_builder(n_floors):
    tower = []
    floor = ''

    for f in range(n_floors):
        stars = '*' * (f * 2 + 1)
        spaces = ' ' * (n_floors - f - 1)
        floor = spaces + stars + spaces
        tower.append(floor)
    return tower


towerDisplay = tower_builder(4)
print(towerDisplay)


# Second Code

def tower_builder(n):
    return [("*" * (i * 2 - 1)).center(n * 2 - 1) for i in range(1, n + 1)]


# Third Code


def tower_builder(n_floors):
    tower = []
    level = 1
    pad = n_floors - 1

    for _ in range(0, n_floors):
        tower.append(" " * pad + "*" * level + " " * pad)
        pad -= 1
        level += 2
    return tower

# Fourth code

def tower_builder(n_floors):
    floors = []
    for i in range(n_floors):
        n_floors -= 1
        floors.append(' ' * n_floors + '*' * (i * 2 + 1) + ' ' * n_floors)

    return floors
