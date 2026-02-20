# - [ ] 134. **[Practice]** Capitalize every word in a string manually (without `.title()`).

# using split with loop
def capitalize_words(text):
    words = text.split()  # Split sentence into words
    result = []

    for word in words:
        # Capitalize first letter manually
        capitalized = word[0].upper() + word[1:].lower()
        result.append(capitalized)

    return " ".join(result)


# Example
print(capitalize_words("hello world python programming"))

"""
split() → turns sentence into list of words

word[0].upper() → capitalize first letter

word[1:].lower() → make remaining letters lowercase

" ".join(result) → combine words back into string
"""


# without split()
def capitalize_words(text):
    result = ""
    new_word = True  # Flag to detect start of a word

    for char in text:
        if char == " ":
            result += char
            new_word = True  # Next character starts new word
        else:
            if new_word:
                result += char.upper()
                new_word = False
            else:
                result += char.lower()

    return result


# Example
print(capitalize_words("hello world python programming"))

"""
new_word = True → means next character should be capitalized

When space appears → next character becomes start of new word

No split(), no .title()
"""

# edge case version
def capitalize_words(text):
    if not text:
        return text

    words = text.split()
    return " ".join(
        word[0].upper() + word[1:].lower() if word else ""
        for word in words
    )