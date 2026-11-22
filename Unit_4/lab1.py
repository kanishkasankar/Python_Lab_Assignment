# Lab Exercise 1: Log File Reader
filename = input("Enter log file name (example: sample.log): ")

try:
    with open(filename, "r") as file:
        for line in file:
            print(line.rstrip())
except FileNotFoundError:
    print("File not found. Create the file in this program's folder first.")
