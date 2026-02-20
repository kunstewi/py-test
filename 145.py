# - [ ] 145. **[Practice]** Convert string input "1, 2, 3" into list of integers.

# "1, 2, 3" -> [1, 2, 3]

# Take input from user
user_input = input("Enter numbers separated by comma: ")

# Step 1: Split the string by comma
split_values = user_input.split(",")

# Step 2: Convert each value to integer (after stripping spaces)
numbers = []

for value in split_values:
    numbers.append(int(value.strip()))

# Print final list
print(numbers)


# using list comprehension
user_input = input("Enter numbers separated by comma: ")

numbers = [int(value.strip()) for value in user_input.split(",")]

print(numbers)