# import the sys module to access command line arguments
import sys  

# sys.argv is a list:
# sys.argv[0] -> script name
# sys.argv[1:] -> actual arguments passed

print("All CLI arguments:", sys.argv)

# Check if at least one argument is passed
if len(sys.argv) < 2:
    print("Usage: python script.py <name>")
    sys.exit(1)  # exit with error code

# Access first argument
name = sys.argv[1]

print(f"Hello, {name}!")
