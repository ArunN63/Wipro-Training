#Write a program that tries to open a file specified by the user for reading. Use a try
# except block to handle FileNotFoundError if the file does not exist. If the file is
# successfully opened, print its contents; otherwise, print an error message.

filename=input("enter file name:")
try:
    file=open(filename,"r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("file not found")