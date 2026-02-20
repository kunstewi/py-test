# ✅ 129. [Practice] Split a string by regex pattern (Python)

"""
re.split(pattern, string) - to split string using regular expression

pattern.split(string) - with a compiled pattern
"""

# split by multiple delimeters
import re

text = "apple,banana;grape orange"

# Split by comma OR semicolon OR space
result = re.split(r"[,\s;]+", text)

print(result)

"""
[,\s;]+

, → comma

; → semicolon

\s → whitespace

+ → one or more

Output:

['apple', 'banana', 'grape', 'orange']
"""

# using a compiled pattern
import re

pattern = re.compile(r"\d+")

text = "apple123banana456grape"

result = pattern.split(text)

print(result) # ['apple', 'banana', 'grape']


# keep the delimiters using groups
import re

text = "apple,banana;grape"

result = re.split(r"(,|;)", text)

print(result) # ['apple', ',', 'banana', ';', 'grape']

