# Loop through a range of numbers
for i in range(5):
    print(i)

for i in range(3, 5):
    print(i)


# Loop through a string
string_name = "apple"
#              01
for letter in string_name:
    print(letter)

for index in range(len(string_name)):
    print(index, string_name[index])


# Loop through an array
arr = ["apple", "cherry", "banana"]
#         # 0       1           2
for fruit in arr:
    print(fruit)
