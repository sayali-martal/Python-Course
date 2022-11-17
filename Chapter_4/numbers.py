# from math import *
import math

# Positive integers
num1 = 7
num2 = 3
# Negative integers
num3 = -45
# Float
num4 = 2.3

print(num1, num2, num3, num4)

# Arithmetic operations
# Sum
print(num1 + num2)
# Subtraction
print(num1 - num2)
# Multiplication
print(num1 * num2)
# Division - Gives float divisor
print(num1 / num2)
# Division - Gives integer divisor
print(num1 // num2)
# Division - Gives remainder
print(num1 % num2)

# Type casting - convert numbers into string for concatenation
print(str(1) + " is less than 2")

# Python inbuilt functions
# Absolute - Outputs positive numbers
print(abs(num2))
# Power - 3^2
print(pow(3, 2))
# Maximum of the two numbers
print(max(3, 2))
# Minimum of the two numbers
print(min(3, 2))

# Rounds float to a nearest integer
# If the digit after decimal is greater than or equal to 5 then round to upper number
# Else lower number
print(round(4.56))      # 5
print(round(4.46))      # 4
print(round(4))         # 4

# Functions from math module
# Round to lower number
print(math.floor(4.99))
print(math.floor(4.46))
# Round to higher number
print(math.ceil(4.99))
print(math.ceil(4.1))
# Square root
print(math.sqrt(9))
