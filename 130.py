# check for an anagram

# Two strings are anagrams if they contain the same characters in the same frequency (order doesn't matter).

# using sorted()
def is_anagram(s1, s2):
    # Remove spaces and convert to lowercase
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    
    return sorted(s1) == sorted(s2)


print(is_anagram("listen", "silent"))   # True
print(is_anagram("hello", "world"))     # False

"""
replace(" ", "") → removes spaces

lower() → makes comparison case-insensitive

sorted() → sorts characters alphabetically

If both sorted lists are equal → anagram
"""

# using character counting
def is_anagram(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    
    if len(s1) != len(s2):
        return False
    
    count = {}
    
    for char in s1:
        count[char] = count.get(char, 0) + 1
    
    for char in s2:
        if char not in count:
            return False
        count[char] -= 1
        if count[char] < 0:
            return False
    
    return True


print(is_anagram("triangle", "integral"))  # True

# Collections.counter()
from collections import Counter

def is_anagram(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    
    return Counter(s1) == Counter(s2)


print(is_anagram("evil", "vile"))  # True