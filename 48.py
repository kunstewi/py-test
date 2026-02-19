"""
checks : 
1 < x AND x < 10

1 < x < 10 is equivalent to 
(1 < x) and (x < 10)

"""

x = 5

if 1 < x < 10:
    print("x is between 1 and 10")

# multiple chains
a = 5
print(1 < a <= 5 < 10) # 1 < a AND a <= 5 AND 5 < 10

# different operators
x = 7

if 5 <= x != 10: # (5 <= x) AND (x != 10)53
    print("Valid")
