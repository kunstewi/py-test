"""
By default, zip() stops at the shortest list.
But with strict=True, Python will raise an error if the lists are not the same length.
"""

# same length works file
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 95]

for name, score in zip(names, scores, strict=True):
    print(name, score)


# will raise error
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90]

for name, score in zip(names, scores, strict=True):
    print(name, score)
