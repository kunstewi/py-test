# Center a string using `.center()`.

# The .center(width, fillchar) method centers a string inside a field of a given width.

# width → Total length of the final string

# fillchar → Optional character used for padding (default is space)

text = "Hello"

centered = text.center(11)

print(centered) #    Hello   

"""
"Hello" has length 5.
To make it length 11, Python adds 3 spaces on each side.
"""

# custom fill character
text = "Hello"

print(text.center(11, "*")) # ***Hello***