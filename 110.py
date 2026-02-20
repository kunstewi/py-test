# Convert to `.upper()`, `.lower()`, `.title()`.

# ✅ 1. .upper() → Convert to UPPERCASE
text = "python is powerful"

result = text.upper()

print(result) # PYTHON IS POWERFUL


# ✅ 2. .lower() → Convert to lowercase
text = "PYTHON IS POWERFUL"

result = text.lower()

print(result) # python is powerful


# ✅ 3. .title() → Capitalize Each Word
text = "python is powerful"

result = text.title()

print(result) # Python Is Powerful


# example - case sensitive operation
user_input = "Python"

if user_input.lower() == "python":
    print("Match found!")