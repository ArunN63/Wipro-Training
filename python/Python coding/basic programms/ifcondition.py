"""
Date : 222-04-2026
Description : learning various if statement formats

"""


#bigest of 2 numbers
'''
num1 = int(input('Enter a number'))
num2 = int(input('Enter another number'))

if num1 == num2 :
    print('both are equal')
elif num1 > num2 :
    print(num1, 'is big')
else:
    print(num2, 'is big')
'''

#biggest of 3 numbers
'''num1 = int(input('enter 1st number'))
num2 = int(input('enter 2nd number'))
num3 = int(input('enter 3rd number'))

if num1 == num2 and num2 == num3:
    print('all the values are same')
elif num1 == num2 or num2 == num3 or num1 == num3:
    print('2 values are equal')
if num1 > num2 and num1 > num3:
    print(num1 ,'is biggest')
elif num2 > num1 and num2 > num3:
    print(num2, 'is biggest ')
elif num3 > num1 and num3 > num2:
    print(num3, 'is biggest')
'''

#weekday
choice = int(input('Enter a number between 1- 7 :'))

match (choice):
    case 1:
        print('monday')
    case 2:
        print('tuesday')
    case 3:
        print('wednesday')
    case 4:
        print('thursday')
    case 5:
        print('friday')
    case 6:
        print('saturday')
    case 7:
        print('sunday')
    case _:
        print('invalid choice')

