# basic multiline f string
name = "Kanai"
age = 22
language = "Python"

message = f"""
Hello {name},

You are {age} years old.
You are learning {language}.
"""

print(message)

# Triple-quoted strings preserve spaces. This includes leading spaces.
name = "Kanai"

message = f"""
    Hello {name}
    Welcome!
"""
print(message)

# using textwrap
import textwrap

name = "Kanai"

message = textwrap.dedent(f"""
    Hello {name},
    Welcome to Python practice.
""")

print(message)

# multiline with expression
a = 10
b = 20

result = f"""
Calculation:
a = {a}
b = {b}
Sum = {a + b}
Product = {a * b}
"""

print(result)