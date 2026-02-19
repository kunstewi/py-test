# using for loop
text = "Python"

for char in text:
    print(char)


# using index with range

for i in range(len(text)):
    print(f"Index {i}: {text[i]}")


# while
i = 0

while i < len(text):
    print(text[i])
    i += 1
