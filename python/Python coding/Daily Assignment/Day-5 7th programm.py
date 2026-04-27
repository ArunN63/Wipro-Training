#Write a program that asks the user to input two numbers and performs division. Use a
# try-except block to handle both ZeroDivisionError and ValueError. Print different
# messages for each exception. If no exception occurs, print the result of the division.

try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print("Reasult:", a / b)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")