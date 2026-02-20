# Binary Search

"""
Binary Search works only on a sorted list.
eg. arr = [1, 3, 5, 7, 9, 11, 13]
Goal: Find index of a target number efficiently.

Instead of checking every element (like linear search), we:

Check the middle element

If target < middle → search left half

If target > middle → search right half

Repeat until found or range becomes empty
"""

# iterative implementation
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2  # Find middle index

        if arr[mid] == target:
            return mid  # Target found
        
        elif arr[mid] < target:
            left = mid + 1  # Search right half
        
        else:
            right = mid - 1  # Search left half

    return -1  # Target not found

arr = [1, 3, 5, 7, 9, 11, 13]
print(binary_search(arr, 7))