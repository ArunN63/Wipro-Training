
#lambda

'''num1 = int(input('enter an number'))
num2 = int(input('enter another number'))

add = lambda n1, n2 : n1+n2

print(add(num1,num2))
'''

numbers = [1,2,3,4,5]

square = lambda nums : [num * num for num in nums]
print(square(numbers))