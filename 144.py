"""
strftime()

It converts a datetime object → formatted string.
"""

# basic example
from datetime import datetime

now = datetime.now()

formatted = now.strftime("%Y-%m-%d %H:%M:%S")

print(formatted) # 2026-02-20 14:35:12

"""
common formatted codes

| Code | Meaning       | Example  |
| ---- | ------------- | -------- |
| `%Y` | Full year     | 2026     |
| `%y` | Short year    | 26       |
| `%m` | Month (01-12) | 02       |
| `%d` | Day (01-31)   | 20       |
| `%H` | Hour (24hr)   | 14       |
| `%I` | Hour (12hr)   | 02       |
| `%M` | Minutes       | 35       |
| `%S` | Seconds       | 12       |
| `%A` | Weekday name  | Friday   |
| `%B` | Month name    | February |

"""

# custome friendly format
from datetime import datetime

now = datetime.now()

formatted = now.strftime("%A, %d %B %Y")

print(formatted) # Friday, 20 February 2026


# 12 hour format
formatted = now.strftime("%I:%M %p")
print(formatted) # 02:35 PM


# formatting specific date
from datetime import datetime

dt = datetime(2026, 1, 15, 10, 30)

print(dt.strftime("%d/%m/%Y")) # 15/01/2026