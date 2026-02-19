# Read this snippet: [x for x in data if x % 2 == 0]. Rewrite it as a regular loop.

data = [1, 3, 6, 6, 6, 8, 9]
result = []

for x in data:
    if x % 2 == 0:
        result.append(x)
