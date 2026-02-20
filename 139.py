import textwrap

text = "Python is a powerful programming language used for web development, data science, automation, and more."

short_text = textwrap.shorten(text, width=50)

print(short_text)

"""
width=50 → maximum allowed length

If text exceeds width → it gets truncated

Adds "..." automatically at the end

It removes extra whitespace automatically

textwrap.shorten():

Breaks at word boundaries

Does NOT cut words in half

Collapses multiple spaces into one
"""

# manual wrapping + shortning
import textwrap

wrapped = textwrap.fill(text, width=40)
print(wrapped)