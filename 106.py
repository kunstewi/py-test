# 1. .strip() → Removes whitespace from both sides
text = "   Hello World   "

clean_text = text.strip()

print(clean_text) # Hello World


# 2. .lstrip() → Removes whitespace from the left side
text = "   Hello World   "

left_clean = text.lstrip()

print(left_clean) # (Only left spaces removed)

# 3. .rstrip() → Removes whitespace from the right side
text = "   Hello World   "

right_clean = text.rstrip()

print(right_clean) # (Only right spaces removed)

# it can remove specific characters too
text = "###Python###"

print(text.strip("#"))
print(text.lstrip("#"))
print(text.rstrip("#"))

