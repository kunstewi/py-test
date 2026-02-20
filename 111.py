# Use `in` keyword to check for substring existence.

text = "Python is powerful"

# Check if "Python" exists in text
result = "Python" in text

print(result) # True

# if doesn't exist
print("Java" in text) # False


# using with if
text = "I love programming"

if "love" in text:
    print("Substring found!")
else:
    print("Substring not found.")

"""
in returns True or False

It is case-sensitive
"""