# ✅ 1. startswith() → Checks beginning of a string
text = "Python is powerful"

# Check if string starts with "Python" if it doesn't match it would return false
result = text.startswith("Python")

print(result) # True


# ✅ 2. endswith() → Checks ending of a string
filename = "report.pdf"

# Check if file ends with .pdf
result = filename.endswith(".pdf")

print(result) # True


# You can check multiple values
file = "image.png"

print(file.endswith((".png", ".jpg", ".jpeg")))

"""
startswith() → checks beginning

endswith() → checks ending

Returns True or False

Can accept a tuple of multiple options
"""
