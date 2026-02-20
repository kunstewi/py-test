# - [ ] 146. **[Practice]** Remove duplicate characters from a string (preserving order).

# "programming" -> "progamin"

# first occurences kept, duplicates removed

# using loops

# Take input
s = input("Enter a string: ")

result = ""          # Empty string to store unique characters

for char in s:
    if char not in result:   # If character not already added
        result += char       # Add it to result

print("After removing duplicates:", result)

# using set
s = input("Enter a string: ")

seen = set()
result = ""

for char in s:
    if char not in seen:
        seen.add(char)
        result += char

print(result)

# one liner
s = input("Enter a string: ")
print("".join(dict.fromkeys(s)))

"""
dict.fromkeys(s) keeps order (Python 3.7+)

Keys are unique

Then join them back into string
"""