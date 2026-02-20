"""
Matrix transpose means:

Rows become columns

Columns become rows

example :

1  2  3
4  5  6

to 

1  4
2  5
3  6
"""

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]


# using nested loops
rows = len(matrix)
cols = len(matrix[0])

# Create empty transpose matrix
transpose = []

for j in range(cols):          # Loop over columns
    new_row = []
    for i in range(rows):      # Loop over rows
        new_row.append(matrix[i][j])
    transpose.append(new_row)

print(transpose)

"""
Outer loop → goes column by column
Inner loop → collects values from each row

We are basically flipping indices:

matrix[i][j]  →  transpose[j][i]
"""

# pre allocating
rows = len(matrix)
cols = len(matrix[0])

transpose = [[0 for _ in range(rows)] for _ in range(cols)]

for i in range(rows):
    for j in range(cols):
        transpose[j][i] = matrix[i][j]

print(transpose)
