# Use itertools.product to avoid nested loops (Introduction).

"""
itertools.product() gives you the Cartesian product of iterables.
It generates all combinations, just like nested loops would.
"""

# nested loops
for i in range(3):
    for j in range(3):
        print(i, j)

# same thing using itertools.product
from itertools import product

for i, j in product(range(3), range(3)):
    print(i, j)



# star square using nested loops
rows = 4
cols = 4

for i in range(rows):
    for j in range(cols):
        print("*", end=" ")
    print()


# same thing using product
for i, j in product(range(rows), range(cols)):
    print("*", end=" ")
    
    if j == cols - 1:   # end of row
        print()


# multiplication table grid
for i, j in product(range(1, 4), range(1, 4)):
    print(f"{i*j:3}", end=" ")
    
    if j == 3:
        print()


# if ranges are same
for i, j in product(range(3), repeat=2):
    print(i, j)
