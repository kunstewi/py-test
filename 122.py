# ✅ Practice 122: Format currency using f-strings ($1,000.00 style)

amount = 1000

formatted = f"${amount:,.2f}"

print(formatted) # $1,000.00

"""
: → start of format specifier

, → adds comma as thousands separator

.2f → 2 decimal places (float)
"""

# with larger number
amount = 1234567.5

print(f"${amount:,.2f}") # $1,234,567.50


# always show two decimal place
price = 99

print(f"${price:,.2f}") # $99.00


# using variables dynamically
currency = "$"
amount = 45000.789

print(f"{currency}{amount:,.2f}") # $99.00


# negative numbers
amount = -5000
print(f"${amount:,.2f}") # $-5,000.00

