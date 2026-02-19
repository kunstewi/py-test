# table from 1 to 10

# Outer loop controls the rows (1 to 10)
for i in range(1, 11):
    
    # Inner loop controls the columns (1 to 10)
    for j in range(1, 11):
        
        # Print product of i and j
        # end="\t" keeps printing in the same row with tab spacing
        print(i * j, end="\t")
    
    # After inner loop ends, move to next line
    print()


# printing single multiplication table
number = 5

for i in range(1, 11):
    for j in range(1, 2):  # runs once, just to demonstrate nesting
        print(f"{number} x {i} = {number * i}")
