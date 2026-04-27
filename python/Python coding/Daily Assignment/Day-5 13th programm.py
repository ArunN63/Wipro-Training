#Write a program that repeatedly asks the user to input an integer. Use a `try-except`
# block to handle `ValueError` in case the user enters a non-integer value. The program
# should keep asking for input until a valid integer is provided, and then print the integer.

while True:
    try:
        num = int(input("Enter integer: "))
        print("Valid:", num)
        break
    except ValueError:
        print("Try again")