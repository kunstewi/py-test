# Manually call next() on an iterator (from iter(range(3))).

"""
An iterator is an object that:

- Has a __next__() method
- Returns values one by one
- Raises StopIteration when done
"""

it = iter(range(3))

print(next(it))  # 0
print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # Error!

# range(3) creates a sequence 0, 1, 2
# iter(range(3)) - Converts the sequence into an iterator object.

# After returning 2, the iterator is exhausted.
# so it gives error on 3

# Loop version
it = iter(range(3))

try:
    while True:
        print(next(it))
except StopIteration:
    print("Iterator finished!")