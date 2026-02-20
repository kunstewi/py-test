# Partition a string with `.partition()`.

"""
The .partition(separator) method splits a string into exactly 3 parts:

(before_separator, separator, after_separator)

It always returns a tuple of 3 elements.

string.partition(sep)
→ (before, sep, after)
"""

text = "apple-banana-orange"

result = text.partition("-")

print(result) # ('apple', '-', 'banana-orange')

# 👉 It splits only at the first occurrence of "-".


# with space
sentence = "Hello World Python"

print(sentence.partition(" ")) # ('Hello', ' ', 'World Python')


# if separator not found
text = "HelloWorld"

print(text.partition("-")) # ('HelloWorld', '', '')

"""
f separator is not found:

First element = whole string

Second and third elements = empty strings
"""


# extracct email, username
email = "kanai@example.com"

username, sep, domain = email.partition("@")

print("Username:", username)
print("Domain:", domain)

"""
Username: kanai
Domain: example.com
"""