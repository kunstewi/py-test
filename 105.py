words = ["Python", "is", "very", "powerful"]

# Join words with space
sentence = " ".join(words)

print(sentence)

"""
separator.join(list)

The string before .join() is the separator

It inserts that separator between each element of the list

All elements must be strings
"""

# different separator
words = ["2026", "02", "20"]

date = "-".join(words)

print(date)