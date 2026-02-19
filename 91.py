# Print a star pyramid pattern.

rows = 5  # height of pyramid

for i in range(1, rows + 1):
    # print spaces
    print(" " * (rows - i), end="")
    
    # print stars
    print("*" * (2 * i - 1))


# full diamond pattern

# Upper pyramid
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))

# Lower inverted pyramid
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
