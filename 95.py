"""
walrus operator - :=

This is the walrus operator (assignment expression).
It was introduced in: 3.8

It allows you to:

Assign a value

AND use that value immediately

Inside an expression
"""

# (n := n - 1) > 0 means :

"""
Subtract 1 from n

Assign the new value back to n

Check if the new value is greater than 0

If True → loop runs

If False → loop stops
"""


while (n := n - 1) > 0:
    print(n)

# is equivalant to 

while True:
    n = n - 1
    if n > 0:
        print(n)
    else:
        break