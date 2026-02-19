# reverse a generic sequence

# for loop works for list, tuple, string
def reverse_sequence(seq):
    reversed_seq = []

    # Iterate from last index to first
    for i in range(len(seq) - 1, -1, -1):
        reversed_seq.append(seq[i])

    # Return same type as input
    return type(seq)(reversed_seq)


# Examples
print(reverse_sequence([1, 2, 3, 4]))
print(reverse_sequence((1, 2, 3, 4)))
print(reverse_sequence("abcd"))

"""
range(len(seq) - 1, -1, -1)
→ Start from last index
→ Stop at index 0
→ Step backwards by -1

Append each element to a new list.

Convert back to original type using type(seq)(...).
"""


# simpler approach building manually
def simple_reverse_sequence(seq):
    reversed_seq = []

    for item in seq:
        reversed_seq = [item] + reversed_seq

    return type(seq)(reversed_seq)



# in place reversal only for list
def reverse_list(lst):
    left = 0
    right = len(lst) - 1

    while left < right:
        # Swap elements
        lst[left], lst[right] = lst[right], lst[left]

        left += 1
        right -= 1

    return lst


nums = [1, 2, 3, 4]
print(reverse_list(nums))
