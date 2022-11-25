# Normal array
arr = [1, 2, 3, 4]
#      0  1  2  3


# 2D array
arr_2D = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [0]]
# column   0  1  2    0  1  2    0  1  2    0
# row         0          1          2       3


# Nested loops
for row in arr_2D:
    # print(row)
    for column in row:
        print(column)
