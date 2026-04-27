#Write a program that asks the user to enter some text and saves it to a file called
# output.txt. Then, open the file and read its contents, printing them to the console.

text=input("enter some text:")
file= open("output.txt","w")
file.write(text)
file.close()
file= open("output.txt","r")
context=file.read()
print("file content:",context)
file.close()