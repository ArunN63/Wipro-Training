#Check Palindrome: Write a user-defined function is_palindrome(s) that takes a string as
# an argument and returns True if the string is a palindrome (reads the same forward and
# backward), and False otherwise. Test the function with different strings and print the results.
def is_palm(s):
    return s==s[::-1]
text=input("enter the string:")
print("palindrome:",is_palm(text))