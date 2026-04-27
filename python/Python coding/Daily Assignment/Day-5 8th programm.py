#Write a program that takes a list of numbers and asks the user to input an index to
# access an element from the list. Use a try-except block to handle IndexError if the user
# enters an invalid index. Print the corresponding element if the index is valid; otherwise,
# print an error message.

numbers = [10, 20, 30, 40]
try:
    index = int(input("Enter index: "))
    print(numbers[index])
except IndexError:
    print("Invalid index")