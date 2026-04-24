#Create and Use a Custom Package:
# Create a package called my_math with two modules: arithmetic.py and geometry.py.
# In arithmetic.py, define functions for addition, subtraction, multiplication, and division.
# In geometry.py, define functions to calculate the area of a circle and the area of a rectangle.
# Write a program that imports these functions from the my_math package and uses them to perform various calculations.

from my_math.arithmetic import add, sub, mul, div
from my_math.geometry import circle_area,rectangle_area
print(add(2,3))
print(sub(10,4))
print(mul(6,2))
print(div(10,2))
print(circle_area(7))
print(rectangle_area(4,6))