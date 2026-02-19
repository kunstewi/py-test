# correct - iterate over a copy
numbers = [2, 4, 6, 8]

for num in numbers[:]:   # copy of list
    numbers.remove(num)

print(numbers)


# using list comprehension
numbers = [1, 2, 3, 4, 5, 6]

numbers = [num for num in numbers if num % 2 != 0]

print(numbers)
