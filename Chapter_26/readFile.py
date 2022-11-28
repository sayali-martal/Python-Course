# Open file in read mode
open_file = open("file.txt", "r")

# check if file is readable
print(open_file.readable())

# Read entire file
print(open_file.read())

# Read file line by line
print(open_file.readline())
print(open_file.readline())
print(open_file.readline())

# Read lines as an array
print(open_file.readlines())
print(open_file.readlines()[1])
for line in open_file.readlines():
    print(line)

# Close file
open_file.close()
