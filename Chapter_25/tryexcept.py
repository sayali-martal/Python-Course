try:
    value = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as message:
    value = 10 / 1
    print("Divisor is zero")
    print(message)
except ValueError as message:
    print("Invalid input")
    print(message)
except:
    print("Unknown error occurred")

print("PROGRAM IS COMPLETED!")
