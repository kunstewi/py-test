for i in range(1, 11):
    if i == 5:
        continue  # Skip this iteration when i is 5
    print(i)


# while loop 
count = 0

while count < 10:
    count += 1
    if count % 2 == 0:
        continue  # Skip even numbers
    print(count)
