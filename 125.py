# re.sub() is used to search for a pattern and replace it with something else.

"""
syntax

re.sub(pattern, replacement, string)

pattern → what you want to find (regex)

replacement → what you want instead

string → original text
"""

# replace all digits with #
import re

text = "My number is 9876543210"

result = re.sub(r"\d", "#", text)

print(result) # My number is ##########


# remove extra spaces
import re

text = "Hello     world     Python"

result = re.sub(r"\s+", " ", text)

print(result) # Hello world Python


# replace email address
import re

text = "Contact: user@gmail.com"

result = re.sub(r"gmail\.com", "company.com", text)

print(result) # Contact: user@company.com


# You can pass a function instead of a string.
import re

def double_number(match):
    number = int(match.group())
    return str(number * 2)

text = "Prices: 10 20 30"

result = re.sub(r"\d+", double_number, text)

print(result) # Prices: 20 40 60

