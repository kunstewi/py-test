# reverse a string
text = "HelloWorld"

# Reverse the string
reversed_text = text[::-1]

print(reversed_text)

"""
string[start : stop : step]

when you write : text[::-1]

start → not given (default = beginning)

stop → not given (default = end)

step = -1 → move backwards

Since the step is -1, Python starts from the end and goes backward one character at a time.
"""