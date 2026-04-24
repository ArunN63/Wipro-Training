#Combining Built-in and User-Defined Functions: Find the Average of a List: Write a user-
# defined function average(numbers) that takes a list of numbers as an argument and returns
# the average of the numbers. Call the function with a list of numbers and print the average.
def average(numbers):
    return sum(numbers)/len(numbers)
nums=list(map(int,input("enter the numbers:").split()))
print("average:",average(nums))