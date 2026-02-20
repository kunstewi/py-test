# In Python, .decode('utf-8') converts bytes → string (str).

data = b"Hello"

decoded_text = data.decode("utf-8")

print(decoded_text)
print(type(decoded_text))

"""
Hello
<class 'str'>

b"Hello" is bytes.
After decoding, it becomes a normal Python string.
"""

# example with hindi

data = "नमस्ते".encode("utf-8")  # First encode to bytes

decoded = data.decode("utf-8")

print(decoded) # नमस्ते

