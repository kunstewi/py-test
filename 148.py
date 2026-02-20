# - [ ] 147. **[Practice]** Find the most frequent character.

"""
Input:  "programming"
Output: "g"

the character that is present most number of times, if number is same then some program return both or which occured first
"""

# using dictionary

# Take input
s = input("Enter a string: ")

freq = {}   # Dictionary to store frequency

# Count frequency
for char in s:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

# Find most frequent character
max_char = None
max_count = 0

for char in freq:
    if freq[char] > max_count:
        max_count = freq[char]
        max_char = char

print("Most frequent character:", max_char)
print("Frequency:", max_count)


# using max

"""
freq.get(char, 0) avoids writing if/else

max(freq, key=freq.get) returns key with highest value
"""

s = input("Enter a string: ")

freq = {}

for char in s:
    freq[char] = freq.get(char, 0) + 1

max_char = max(freq, key=freq.get)

print("Most frequent character:", max_char)


# using collections.Counter()

from collections import Counter

s = input("Enter a string: ")

counter = Counter(s)

most_common_char = counter.most_common(1)[0]

print("Most frequent character:", most_common_char[0])
print("Frequency:", most_common_char[1])