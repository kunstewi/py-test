# Check if string `.isdigit()`, `.isalpha()`, `.isalnum()`.

# ✅ 1. .isdigit() → Checks if all characters are digits
text = "12345"

print(text.isdigit()) # True

print("123a".isdigit()) # False


# ✅ 2. .isalpha() → Checks if all characters are letters
text = "Python"

print(text.isalpha()) # True

print("Python3".isalpha()) # False


# ✅ 3. .isalnum() → Checks if all characters are letters OR numbers
text = "Python3"

print(text.isalnum()) # True

print("Python 3".isalnum()) # False

