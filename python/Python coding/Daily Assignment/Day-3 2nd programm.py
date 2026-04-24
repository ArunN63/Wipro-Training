#Write a user-defined function factorial(n) that takes a positive integer n as an argument
#and returns its factorial. Use the function in a program and print the factorial of a given number.
def factorial(n):
    fact=1
    for i in range(1, n+1):
        fact*=i
        return fact
    num = int(input("enter number:"))
    result=factorial(num)
    return result