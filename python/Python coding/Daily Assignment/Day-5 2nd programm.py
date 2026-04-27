#Write a program that reads a text file called sample.txt and counts the number of lines,
# words, and characters in the file. Print the counts.

file=open("sample.txt","r")
content=file.read()
lines=content.split("\n")
words=content.split()
character=len(content)
print("lines:",len(lines))
print("words:",len(words))
print("characters:",character)
file.close()