# filter even number
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)

# filter numbers greater than 5
filtered = []

for num in numbers:
    if num > 5:
        filtered.append(num)

print(filtered)

"""
syntax :

new_list = []

for item in old_list:
    if condition:
        new_list.append(item)

"""
