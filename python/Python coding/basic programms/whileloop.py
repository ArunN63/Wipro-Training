#natural numbers printing

'''num = int(input('enter a number'))
value = 1

while value <= num:
    print(value)
    value += 1'''

# armstrong number

num = input('enter a number')
count = len(num)
sum = 0
ni = int(num)
comp = ni
while ni > 0:
    rem = ni % 10
    sum = sum + rem ** count
    ni = ni // 10

if comp == sum:
    print('armstrong number')
else:
    print('not armstrong number')