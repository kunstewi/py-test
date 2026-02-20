# str.maketrans() creates a translation table.
# .translate() uses that table to modify a string.

# Create translation table
table = str.maketrans("abc", "123")

text = "apple and banana"

result = text.translate(table)

print(result) # 1pple 1nd 21n1n1

"""
"a" → "1"

"b" → "2"

"c" → "3"
"""

# using dictionary form
table = str.maketrans({
    "a": "@",
    "e": "3",
    "i": "1",
    "o": "0"
})

text = "hello world"

print(text.translate(table)) # h3ll0 w0rld


# You can remove characters by mapping them to None.
table = str.maketrans("", "", "aeiou")

text = "hello world"

print(text.translate(table)) # hll wrld