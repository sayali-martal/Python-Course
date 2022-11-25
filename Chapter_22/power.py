# 2 ^ 3 = 2 * 2 * 2 = 8

# print(2**3)
# print(pow(2, 3))


def power(base_num, power_num):
    result = 1
    for index in range(power_num):
        # print(result, index)
        result = result * base_num
        # result    1   *   2       = 2
        # result    2   *   2       = 4
        # result    4   *   2       = 8

    return result


print(power(2, 3))
print(power(3, 4))
