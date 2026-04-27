#Write a program that defines a function to add two numbers. Use a try-except block to
# handle TypeError in case the function is called with non-numeric arguments (e.g.,
# strings). Print an appropriate error message if the exception is caught.

def add(a, b):
    try:
        return a + b
    except TypeError:
        print("Invalid types")
print(add(5, 10))
print(add("hi", 5))