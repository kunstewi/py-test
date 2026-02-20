# Use `.replace()` to swap substrings.
text = "I love Java"

# Replace "Java" with "Python"
new_text = text.replace("Java", "Python")

print(new_text) # I love Python

"""
string.replace(old, new, count)

old → substring to replace

new → replacement text

count → (optional) number of replacements
"""

# replace all occurences
text = "apple apple apple"

result = text.replace("apple", "mango")

print(result) # mango mango mango


# replace limited times
text = "apple apple apple"

result = text.replace("apple", "mango", 1)

print(result) # mango apple apple

"""
Strings are immutable in Python.

.replace() does not modify the original string.

It returns a new string.
"""