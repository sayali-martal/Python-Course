numbers = [10, 15, 31, 1, 2, 3, 4, 5]
color = ["blue", "red", "black", "white"]
#           0       1       2       3
#          -4       -3       -2       -1

# Add items to the list
color.extend(numbers)
color.extend([5, 6, 7])
print(color)

# Add item at the end of the list
color.append("brown")
color.append(5)
print(color)

# Add item at the given position of the list
color.insert(2, "yellow")
print(color)

# Remove item from the list
color.remove("black")
print(color)

# Clear the list
color.clear()
print(color)

# Remove last element from the list and returns the removed element
lastColor = color.pop()
print(lastColor, color)

# Give index of the value
print(color.index("black"))

# Give number of times an element is repeated
print(color.count(5))

# Sort array in ascending order
color.sort()
print(color)

# Reverse an array
color.reverse()
print(color)

# Copy array
new_color = color
new_color_copy = color.copy()
color[0] = "green"
print(new_color, new_color_copy)
