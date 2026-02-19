# Never modify a list while iterating over it directly.

# Iterate over a copy

# Or create a new list

# Or iterate backwards using indices

numbers = [2, 4, 6, 8]

for num in numbers:
    numbers.remove(num)

print(numbers)

# it returns [4, 8], why it didn't remove all the nums ?

"""
for num in numbers:
It internally uses an index pointer.

initial list:
[2, 4, 6, 8]

Index 0 → value 2
Remove 2
List becomes:
[4, 6, 8]

Now index moves to 1
But index 1 is now 6
(Because 4 shifted to index 0)

So 4 gets skipped!

removing elements shifts the lists so it's not a good idea to modify a list while iterating
"""

# correct - iterate over a copy
numbers = [2, 4, 6, 8]

for num in numbers[:]:   # copy of list
    numbers.remove(num)

print(numbers)


# using list comprehension
numbers = [1, 2, 3, 4, 5, 6]

numbers = [num for num in numbers if num % 2 != 0]

print(numbers)
