# - [ ] 142. **[Practice]** Use `sys.getsizeof()` on strings.

import sys

s = "hello"
print(sys.getsizeof(s))

"""
it returns

Total memory used by the string object

Includes:

Object overhead

String content

Measured in bytes
"""

# compare different strings
import sys

s1 = ""
s2 = "a"
s3 = "hello"
s4 = "hello world"
s5 = "a" * 100

print(sys.getsizeof(s1))
print(sys.getsizeof(s2))
print(sys.getsizeof(s3))
print(sys.getsizeof(s4))
print(sys.getsizeof(s5))

"""
Empty string already has some base memory.

Larger strings use more memory.

Python adds overhead beyond just character count.
"""

# Observe growth pattern
import sys

for i in range(0, 51, 10):
    s = "a" * i
    print(f"Length: {i}, Size: {sys.getsizeof(s)} bytes")

"""
Memory grows as length increases.

But there is fixed object overhead.
"""

