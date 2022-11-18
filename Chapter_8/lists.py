color1 = "blue"
color2 = "red"
color3 = "black"
color4 = "white"

# Mutable and supports all data types
mixed_lts = ["string", 2, True]
numbers = [10, 15, 31, 1, 2, 3, 4, 5]
color = ["blue", "red", "black", "white"]
#           0       1       2       3
#          -4       -3     -2      -1

print(color, numbers)

# Update array
color[1] = "yellow"
print(color)

# Indexing
print(color[0], numbers[0])

# Negative indexing
print(color[-1], numbers[-1])

# Slicing
print(numbers[1:])
print(numbers[:2])
print(color[1:])
print(color[:3])
print(color[:-1])
print(color[1:3])

print(color[0][1])
