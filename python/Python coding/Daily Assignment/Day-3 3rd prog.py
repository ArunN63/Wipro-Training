#Write a user-defined function "find_largest(a, b, c)" that takes three numbers as
#arguments and returns the largest of the three. Use the function in a program to find and
#print the largest of three given numbers.
def larg(a,b,c):
    return max(a,b,c)
a, b, c=map(int,input("enter 3 numbers:").split())
print("largest:",larg(a,b,c))

