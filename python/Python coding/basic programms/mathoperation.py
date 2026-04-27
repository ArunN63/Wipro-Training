# second program for module
from mypack.basicshapes import areaofsquare, perimeterofsquare, areaofrectangle
from mypack.circle import areaofcricle, perimeterofcricle


radius = int(input('Enter radius : '))

print('Area : ',areaofcricle(radius = radius))
print('Perimeter : ',perimeterofcricle(radius = radius))

s = int(input('Enter side of sq :'))
print('Area of Square : ', areaofsquare(side = s))
print('perimeter of square : ', perimeterofsquare(side = s))

l = int(input('Enter length : '))
b = int(input('Enter breadth : '))
print('Area of rec :', areaofrectangle(l,b))