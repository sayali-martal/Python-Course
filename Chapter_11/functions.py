def sum_of_numbers(num1, num2=4):
    print("Inside the function")
    print(num1, num2)
    result = num1 + num2
    print("Sum of two numbers is: " + str(result))


print("outside the function")

# num1 = 2, num2 = 3
sum_of_numbers(2, 3)

# num1 = 3, num2 = 2
sum_of_numbers(num2=2, num1=3)

# num1 = 2, num2 = 4
sum_of_numbers(2)
