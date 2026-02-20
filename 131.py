# Find the longest word in a sentence.

# using loop
"""
split() → converts sentence into a list of words.

We initialize longest = "".

Loop through each word.

If current word length > longest word length → update.

Return the longest word.
"""
def longest_word(sentence):
    words = sentence.split()   # Split sentence into words
    
    longest = ""               # Store longest word
    
    for word in words:         # Iterate over each word
        if len(word) > len(longest):  # Compare lengths
            longest = word
    
    return longest


# Example
sentence = "I am learning Python programming language"
print(longest_word(sentence))



# using max
"""
max(words, key=len)
→ Finds the word with maximum length
→ key=len tells Python to compare based on length.
"""
def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)


sentence = "I am learning Python programming language"
print(longest_word(sentence))



# remove punctuation
import re

def longest_word(sentence):
    words = re.findall(r'\b\w+\b', sentence)
    return max(words, key=len)

sentence = "I am learning Python programming, language!"
print(longest_word(sentence))