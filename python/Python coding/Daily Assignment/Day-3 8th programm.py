#Use the Random Module:
# Write a program that imports the random module and uses it to:
# Generate and print a random integer between 1 and 100.
# Create a list of random numbers  and print the list.
# Shuffle a list of numbers and print the shuffled list.
import random
print(random.randint(1,100))
lst=[random.randint(1,100)for i in range(5)]
print(lst)
random.shuffle(lst)
print("shuffled:",lst)
