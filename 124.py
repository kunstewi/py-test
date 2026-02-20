import re

text = """
Contact us at support@example.com
or sales.team@company.co.in
You can also reach admin123@gmail.com
"""

# Regex pattern for emails
pattern = r"\b[\w\.-]+@[\w\.-]+\.\w+\b"

emails = re.findall(pattern, text)

print(emails) # ['support@example.com', 'sales.team@company.co.in', 'admin123@gmail.com']

"""
\b                → Word boundary
[\w\.-]+          → Username (letters, digits, _, ., -)
@                 → Literal @ symbol
[\w\.-]+          → Domain name
\.                → Dot (escaped)
\w+               → Extension (com, org, in, etc.)
\b                → Word boundary

re.search() → finds first match only

re.findall() → returns all matches as a list
"""

"""
Regular Expressions (Regex) are patterns used to search, match, and manipulate text.

common regex symbols

| Pattern | Meaning                           |
| ------- | --------------------------------- |
| `.`     | Any character                     |
| `\d`    | Digit (0-9)                       |
| `\w`    | Word character (a-z, A-Z, 0-9, _) |
| `\s`    | Whitespace                        |
| `+`     | One or more                       |
| `*`     | Zero or more                      |
| `?`     | Optional                          |
| `^`     | Start of string                   |
| `$`     | End of string                     |

"""