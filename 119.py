# ord() and chr() are used to convert between characters and their Unicode (ASCII) integer values.

# 🔹 1. ord() → Character ➝ Number
# ord(character) returns the Unicode code point (integer).

"""
ord() works on a single character only

chr() works on a valid Unicode integer

Unicode supports thousands of characters (not just English)
"""

print(ord("A"))
print(ord("a"))
print(ord("1"))

"""
65
97
49
"""

# 🔹 2. chr() → Number ➝ Character
# chr(number) converts a Unicode number back into a character.

print(chr(65))
print(chr(97))
print(chr(49))

"""
A
a
1
"""


# 🔹 Practical Example: Shift Character (Basic Caesar Cipher Idea)
letter = "A"

shifted = chr(ord(letter) + 1)

print(shifted) # B

"""
👉 ord("A") → 65
👉 65 + 1 → 66
👉 chr(66) → "B"
"""

