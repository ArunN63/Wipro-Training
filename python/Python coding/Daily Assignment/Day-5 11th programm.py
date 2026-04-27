#Write a program that tries to open and read a file. Use a try-except-finally block to
# handle potential exceptions like FileNotFoundError. Ensure that the finally block prints a
# message indicating that the program has completed, whether an exception occurred or not.
try:
    file = open("test.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File not found")
finally:
    print("Done execution")