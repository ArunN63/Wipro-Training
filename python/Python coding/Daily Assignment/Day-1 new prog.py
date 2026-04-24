#Write a program that asks the user for their age and checks if they are eligible to vote (18 years and older).
# Print a message based on their eligibility.

age=int(input("enter your age"))
if age>=18:
    print("you are eligible to vote")
else:
    print("your not eligible to vote")
#Write a program that takes a year as input and checks if it is a leap year or not.
year=int(input("enter the year"))
if(year%4==0 and year%100!=0) or(year%400==0):
    print("it is a leap year")
else:
    print("it is not a leap year")

# Write a program that takes a number as input and checks if it is divisible by 5.
number=int(input("enter a number"))
if number%5==0:
    print("it is divisible by 5")
else:
    print("it is not divisible by 5")
#Write a program that takes a character as input and checks if it is a vowel or consonant.
char=(input("enter the char"))
if char in 'aeiou':
    print("it is a vowel")
else:
    print("it is not vowel")
#Write a program that takes a password as input and checks if it is strong
password=input("enter the password")
if len(password)>=8:
    print("strong password")
else:
    print("not strong password")

# Write a program that takes a grade (A, B, C, D, F) as input
grade=input("enter the grade(A/B/C/D/E/F)")
match grade:
    case 'A':
        print("excellent")
    case 'B':
        print("good")
    case 'C':
        print("better")
    case 'D':
        print("ok")
    case 'E':
        print("it's ok")
    case 'F':
        print("fail")

#Write a program that takes a traffic light color (Red, Yellow, Green) as input
light=input("enter the light(green/red/yellow)")
match light:
    case 'green':
        print("go")
    case 'red':
        print("stop")
    case 'yellow':
        print("ready")
    case _:
        print("invalid")

#Write a program that takes a number as input and uses a for loop to calculate its factorial
num=int(input("enter the number"))
fact=1
for i in range(1, num+1):
    fact*=i
    print("factorial of number",fact)

#Write a program that uses a for loop to print all even numbers between 1 and 20.
i=1
for i in range(1, 21):
    if i%2==0:
        print(i)

#. Write a program that uses a while loop to create a countdown timer from 10 to 0.
i=11
while i>=0:
    print(i)
    i-=1

# Write a program that uses a for loop to count the number of vowels in a given string
text=input("enter the string")
count=0
for char in text:
    if char in 'aeiou':
        count=count+1
        print("number of vowels",count)

# Write a program that uses a for loop to print numbers from 1 to 10, but skips
#printing the number 5 (use continue) and stops the loop if the number 8 is reached
for i in range(1,11):
    if i==5:
        continue
    if i==9:
        break
    print(i)