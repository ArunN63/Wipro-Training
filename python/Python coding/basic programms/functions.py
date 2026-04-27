'''
#functions
def add(a,b):
    print('a',a)
    print('b',b)
    return a + b




#driver
num1 = int(input('enter a number :'))
num2= int(input('enter another number :'))

result = add(num1 , num2)      #positional arguments
print('Addition : ',result)
result1 = add(b= num2,a = num1) #keyword arguments
print('Addition :',result1)
'''


'''def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div():
    pass

result1 = sub(num1 , num2)
print('subtraction :',result1)

result2 = mul(num1 , num2)
print('multiplication :',result2)'''

#Arbitary arguments : when you do not now how many arguments are ther
'''def add(nums):
    sum =0
    for n in nums:
        sum += n
    return sum

numbers = list()
count = int(input('how many '))

for _ in range(1, count + 1):
    numbers.append(int(input('numbers : ')))


'''

#optional

def add(n1, n2, n3 =10):
    return n1 + n2 + n3

num1 = int(input('enter a number'))
num2 = int(input('enter another number'))

print(add(num1,num2))
print(add(num1,num2, n3=100))
