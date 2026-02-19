# Flatten a 2D list using nested loops.

"""
we want

matrix = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8]
]

to be

[1, 2, 3, 4, 5, 6, 7, 8]
"""
matrix = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8]
]

# using nested loops
def flatten_2d_list(matrix):
    flat_list = []  # This will store final result
    
    for row in matrix:        # First loop → goes through each sublist
        for item in row:      # Second loop → goes through elements inside sublist
            flat_list.append(item)
    
    return flat_list


matrix = [[1, 2, 3], [4, 5], [6, 7, 8]]
print(flatten_2d_list(matrix))


# 