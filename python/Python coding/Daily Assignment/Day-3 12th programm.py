#Create a Package for String Utilities:
# Create a package called string_utils with two modules: string_operations.py and string_validations.py.
# In string_operations.py, define functions for reversing a string, converting a string to uppercase, and finding the length of a string.
#In string_validations.py, define functions to check if a string is a palindrome and if it contains only alphabetic characters.
# Write a program that imports and uses these functions from the string_utils package.

from string_utils.string_operatons import reverse_string, to_upper, string_length
from string_utils.string_validation import is_palindrome, is_alpha
text=input("enter a string:")
print("recersed:",reverse_string(text))
print("length:",string_length(text))
print("is palindrome:",is_palindrome(text))
print("only Alphabetes:", is_alpha(text))