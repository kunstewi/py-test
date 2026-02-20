# Compile a regex pattern object.
import re

# Compile a regex pattern
pattern = re.compile(r"\d+")

print(pattern)

"""
re.compile() → creates a regex pattern object

r"\d+"

r → raw string (so \ works properly)

\d → matches any digit (0–9)

+ → one or more times

Now pattern is a reusable regex object.
"""

# use the compiled pattern
import re

pattern = re.compile(r"\d+")

text = "I have 25 apples and 300 mangoes"

matches = pattern.findall(text)

print(matches) # ['25', '300']


# email pattern
import re

email_pattern = re.compile(r"\w+@\w+\.\w+")

text = "Contact me at test@gmail.com"

match = email_pattern.search(text)

print(match.group())

"""
instead of writing :

re.findall(r"\d+", text)

Compiling is better when:

You reuse the same regex many times

You want cleaner and faster code
"""

