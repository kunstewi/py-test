# - [ ] 149. **[Practice]** Expand a compressed string.

"""
compressed string - a3b2c4

uncompressed - aaabbcccc
"""

# using simple loop 

# Take input
s = input("Enter compressed string: ")

result = ""

i = 0
while i < len(s):
    char = s[i]           # letter
    count = int(s[i + 1]) # number after letter
    
    result += char * count
    
    i += 2   # move to next letter-number pair

print("Expanded string:", result)


# method 2
s = input("Enter compressed string: ")

expanded = ""

for i in range(0, len(s), 2):
    expanded += s[i] * int(s[i + 1])

print(expanded)


"""
This works only if:

Every character is followed by exactly one digit

Example: a3b12 ❌ (won’t work properly)
"""

# Advanced Version to handle these
s = input("Enter compressed string: ")

result = ""
i = 0

while i < len(s):
    char = s[i]
    i += 1
    
    num = ""
    while i < len(s) and s[i].isdigit():
        num += s[i]
        i += 1
    
    result += char * int(num)

print(result) # a12b3 -> aaaaaaaaaaaabbb

