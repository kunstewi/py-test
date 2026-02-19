# Use pass as a placeholder.

"""
Python does not allow empty blocks.
if True:
You must write something inside the block.

if True:
    pass

now it runs without error
"""

# empty function
def my_function():
    pass


# empty class
class MyClass:
    pass


# inside loops
for i in range(5):
    pass


# placeholder in condition
x = 0

if x > 10:
    pass
else:
    print("x is small")
