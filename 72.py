# for loop
total = 0

for i in range(1, 101):  # 101 because stop is exclusive
    total += i

print("Sum from 1 to 100 is:", total)


# while loop
i = 1

while i <= 100:
    total += i
    i += 1

print("Sum from 1 to 100 is:", total)


# math formula
n = 100
total = n * (n + 1) // 2
print(total)
