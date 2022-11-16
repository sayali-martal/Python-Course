char_name = "Beautiful day"

# Print string
print(char_name)

# Concatenation of strings
print("Beautiful" + " " + "day")

# String to lower case
print(char_name.lower())

# String to upper case
print(char_name.upper())

# True only if string is upper case
print(char_name.isupper())

# Length of a string
print(len(char_name))

# Get character at specific index
#                   B e a u t i f u l   d a y
# Normal index:     1 2 3 4 5 6 7 8 9
# Python index:     0 1 2 3 4 5 6 7 8
print(char_name[1])

# Get index of a character
print(char_name.index("a"))

# Get starting index of a word
print(char_name.index("auti"))

# Replace character
print(char_name.replace("B", "D"))

# Replace word
print(char_name.replace("Beautiful", "Amazing"))
