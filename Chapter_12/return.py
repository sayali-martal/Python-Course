def sum_of_numbers(num1, num2=4):
    print("Inside the function")
    print(num1, num2)
    result = num1 + num2
    return result
    print("Statement will not get executed after the return statement")


# num1 = 2, num2 = 3
print("Sum of two numbers is: " + str(sum_of_numbers(2, 3)))

# num1 = 3, num2 = 2
print("Sum of two numbers is: " + str(sum_of_numbers(num2=2, num1=3)))

# num1 = 2, num2 = 4
print("Sum of two numbers is: " + str(sum_of_numbers(2)))
