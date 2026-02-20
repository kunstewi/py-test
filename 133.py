# - [ ] 133. **[Practice]** Remove punctuation from a string.

# using string.punctuation
import string

def remove_punctuation(text):
    result = ""
    
    for char in text:
        if char not in string.punctuation:  # Check if not punctuation
            result += char
    
    return result


# Example
text = "Hello, World! How's everything?"
print(remove_punctuation(text))

"""
string.punctuation → contains all punctuation characters:

!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

We loop through each character.

If it's not punctuation → keep it.
"""


# using str.translate
import string

def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))


text = "Hello, World! How's everything?"
print(remove_punctuation(text))

"""
str.maketrans('', '', string.punctuation)
→ creates a translation table that removes punctuation.

translate() applies it.
"""

# using regular epressions
import re

def remove_punctuation(text):
    return re.sub(r'[^\w\s]', '', text)


text = "Hello, World! How's everything?"
print(remove_punctuation(text))

"""
[^\w\s]

\w → letters & digits

\s → spaces

^ → NOT

So it removes everything that is not word or space.
"""