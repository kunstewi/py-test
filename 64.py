"""
enumerate() lets you loop through a list and get:

- the index
- the value

at the same time.
"""

# without enumarate()
fruits = ["apple", "banana", "mango"]

for i in range(len(fruits)):
    print(i, fruits[i])


# with enumarate()
for index, value in enumerate(fruits):
    print(index, value)


# starting index can be changed
for index, value in enumerate(fruits, start=1):
    print(index, value)
