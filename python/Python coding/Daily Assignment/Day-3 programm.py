#Take a list of numbers as input and print the largest and smallest numbers in the list.
#Take a string as input and print the length of the string.
#Take a list of names as input and print the list in alphabetical order.
#Take a list of numbers as input and print the total sum of the elements in the list.
#Takes a string as input and print the string in uppercase.

numbers=list(map(int,input("enter the numbers").split()))
print("largest num:",max(numbers))
print("smallest num:",min(numbers))
print("sum of num:",sum(numbers))
text=input("enter the string")
print("length:",len(text))
print("uppercase:",text.upper())

names=input("enter names:").split()
names.sort()
print("sorted names:",names)

