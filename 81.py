def find_max(numbers):
    # checking for empty list
    if not numbers:
        raise ValueError("List is empty")
    
    # Assume the first element is the maximum initially
    maximum = numbers[0]

    # Loop through the list starting from the second element
    for num in numbers[1:]:
        # If current number is greater than maximum, update maximum
        if num > maximum:
            maximum = num

    return maximum


# Example usage
nums = [10, 45, 23, 89, 12]
print(find_max(nums))
