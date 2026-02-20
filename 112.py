# Count occurrences of a char with `.count()`.

text = "programming"

# Count how many times 'm' appears
count_m = text.count("m")

print(count_m) # 2

"""
string.count(substring)

Returns the number of times the substring appears.

It is case-sensitive.
"""

# counting a word
sentence = "Python is easy. Python is powerful."

count_python = sentence.count("Python")

print(count_python) # 2