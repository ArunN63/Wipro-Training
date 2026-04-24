#Use the Math Module:Write a program that imports the math module and uses it to:
# Find the square root of a number.
# Calculate the sine of an angle .
# Find the greatest common divisor (GCD) of two numbers .

import math
num=int(input("enter number:"))
print("square root:",math.sqrt(num))
angle=int(input("enter angle:"))
print("sine:",math.sin(math.radians(angle)))
a,b=map(int,input("enter two numbers:").split())
print("gcd:",math.gcd(a,b))