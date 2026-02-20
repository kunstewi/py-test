# Use `re.match()` vs `re.search()`.

# Both functions are used to find patterns using regex — but they behave differently.

"""
re.match()

Checks for a match only at the beginning of the string.

If the pattern is not at the start → returns None.
"""

import re

text = "Python is powerful"

result = re.match(r"Python", text)

print(result) # <re.Match object ...>

# now 
result = re.match(r"is", text)
print(result) # None


"""
re.search()

Searches the entire string

Returns the first match anywhere
"""

import re

text = "Python is powerful"

result = re.search(r"is", text)

print(result) # <re.Match object ...>

"""
String:  "Python is powerful"
          ↑
match()  checks only here

search() checks entire string → →
"""

# extract matched text
import re

text = "Python is powerful"

m1 = re.match(r"Python", text)
m2 = re.search(r"is", text)

print(m1.group())  # Python
print(m2.group())  # is


# If you want to force search() to match only at the start, you can use ^:
re.search(r"^Python", text)
