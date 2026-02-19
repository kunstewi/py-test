"""
A and B : 

Evaluates A

If A is False → stop immediately (return A)

If A is True → evaluate B
"""

# only the first one runs because it returns false the second doesn't run short circuiting
def first():
    print("First function called")
    return False

def second():
    print("Second function called")
    return True

result = first() and second()

print("Result:", result)

# when the first one true both run

# with variables
x = 0

if x != 0 and 10 / x > 1:
    print("Condition is True")
