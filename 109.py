# To find the index of a substring using .find() and .index() in Python:

# using .find()
text = "Python is powerful"

position = text.find("is")

print(position) # 7

"""
Returns the starting index of the substring.

If substring is not found, it returns -1.
"""

print(text.find("Java")) # -1


# using .index()
text = "Python is powerful"

position = text.index("is")

print(position) # 7

# If substring is not found, .index() raises an error.

print(text.index("Java")) # ValueError: substring not found

"""
Use .find() → when you want safe checking

Use .index() → when substring must exist
"""