

import numpy as np

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# Element-wise addition
print("Element-wise addition:", array1 + array2)

# Element-wise subtraction
print("Element-wise subtraction:", array1 - array2)

# Element-wise multiplication
print("Element-wise multiplication:", array1 * array2)

# Element-wise division
print("Element-wise division:", array1 / array2)

'''
Basic Arithmetic Operations
NumPy provides functions for basic arithmetic operations which also operate element-wise.

Aggregate Functions
NumPy provides aggregate functions that operate over the entire array 
or along a specific axis.

'''

# Adding a scalar to an array
print("Adding 10 to each element:", array1 + 10)

# Multiplying each element by a scalar
print("Multiplying each element by 2:", array1 * 2)

# Using numpy functions
print("Square of each element:", np.square(array1))
print("Square root of each element:", np.sqrt(array1))


array = np.array([[1, 2, 3], [4, 5, 6]])

# Sum of all elements
print("Sum of all elements:", np.sum(array))

# Mean of all elements
print("Mean of all elements:", np.mean(array))

# Minimum element
print("Minimum element:", np.min(array))

# Maximum element
print("Maximum element:", np.max(array))

# Sum along each column
print("Sum along each column:", np.sum(array, axis=0))

# Sum along each row
print("Sum along each row:", np.sum(array, axis=1))