# basic
def basicInfiniteLoop():
    while True:
        print("Running... Press Ctrl+C to stop")

# try except with proper keyboard interrup handling
try:
    while True:
        print("Running... Press Ctrl+C to stop")
except KeyboardInterrupt:
    print("\nProgram stopped by user.")
