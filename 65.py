# zip() allows you to iterate over multiple lists at the same time.
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 95]

for name, score in zip(names, scores):
    print(name, score)


# converting zip to lists
pairs = list(zip(names, scores))
print(pairs)


# note - If lists are different sizes, zip() stops at the shortest one.

# using zip with more than 2 lists
names = ["Alice", "Bob"]
scores = [85, 90]
grades = ["A", "A+"]

for name, score, grade in zip(names, scores, grades):
    print(name, score, grade)


