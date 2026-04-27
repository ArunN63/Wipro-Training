#Write a program that repeatedly asks the user to input two numbers and performs
# division. Use a try-except block inside a loop to handle ZeroDivisionError and
# ValueError. The program should continue until the user provides valid input and a valid
# division result is printed.

while True:
    try:
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        print("Result:", a / b)
        break
    except ZeroDivisionError:
        print("Zero division error")
    except ValueError:
        print("Invalid input")