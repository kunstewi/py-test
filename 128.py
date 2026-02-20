# Extract groups from a regex match object.

"""
When you use parentheses () in a regex pattern, you create capturing groups.
You can extract them from a match object using:

match.group()

match.group(1)

match.groups()
"""

import re

pattern = re.compile(r"(\d{2})-(\d{2})-(\d{4})")

text = "Today's date is 20-02-2026"

match = pattern.search(text)

if match:
    print("Full match:", match.group(0))   # Entire match
    print("Day:", match.group(1))          # First group
    print("Month:", match.group(2))        # Second group
    print("Year:", match.group(3))         # Third group

"""
Output:
Full match: 20-02-2026
Day: 20
Month: 02
Year: 2026

Explanation:
(\d{2})-(\d{2})-(\d{4})

(\d{2}) → Day

(\d{2}) → Month

(\d{4}) → Year
"""

# extract all groups at once
print(match.groups()) # ('20', '02', '2026')


# named groups
import re

pattern = re.compile(r"(?P<username>\w+)@(?P<domain>\w+\.\w+)")

text = "Email: test@gmail.com"

match = pattern.search(text)

if match:
    print("Username:", match.group("username"))
    print("Domain:", match.group("domain"))


# syntax : (?P<name>pattern)