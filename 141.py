# - [ ] 141. **[Theory]** String interning in Python.

"""
String Interning

String interning is an optimization where Python stores only one copy of identical immutable strings in memory.

Instead of creating multiple identical string objects, Python reuses the same object.

Because:

Strings are immutable

Reusing saves memory

Comparison becomes faster (is works)
"""

# automatic
a = "hello"
b = "hello"

print(a == b)  # True (values equal)
print(a is b)  # True (same memory object)

# not always
a = "hello world"
b = "hello world"

print(a is b)  # Might be True or False

"""
Python automatically interns:

Short strings

Strings that look like identifiers (variable_name)

But not always long or complex strings
"""

# force interning
import sys

a = sys.intern("hello world")
b = sys.intern("hello world")

print(a is b)  # Always True


# is vs ==
x = "python"
y = "python"

print(x == y)  # True
print(x is y)  # True (interned)