#Write a program that reads the contents of a file called source.txt and writes the
# contents to another file called destination.txt. Ensure that destination.txt is created if it doesn't exist.

source=open("sample.txt","r")
data=source.read()
destination=open("destination.txt","w")
destination.write(data)
source.close()
destination.close()
print("copied from sample.txt")