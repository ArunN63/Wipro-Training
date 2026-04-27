#Write a program that defines a custom exception class NegativeNumberError. The
# program should ask the user to input a positive number. If the user enters a negative
# number, raise the NegativeNumberError and handle it using a try-except block, printing
# an appropriate error message.

class NegativeNumberError(Exception):
    pass
try:
    num = int(input("Enter number: "))
    if num < 0:
        raise NegativeNumberError("Negative not allowed")
    print("Valid number")
except NegativeNumberError as e:
    print(e)