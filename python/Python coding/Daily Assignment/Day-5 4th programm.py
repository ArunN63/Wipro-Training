#Write a program that appends a line of text to a file called log.txt. After appending the
# text, open the file and print its contents to verify that the text was added.

text=input("enter text:")
file=open("sample.txt","a")
file.write(text+"\n")
file.close()
file=open("sample.txt","r")
print(file.read())
file.close()