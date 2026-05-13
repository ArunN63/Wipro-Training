'''
Basic Mathematical Functions
Trigonometric Functions
NumPy provides various trigonometric functions such as sine, cosine,
tangent, etc.
'''

import numpy as np

angles = np.array([0, np.pi/2, np.pi])
print(angles)
print("Sine of angles:", np.sin(angles))
print("Cosine of angles:", np.cos(angles))
print("Tangent of angles:", np.tan(angles))

# Inverse trigonometric functions
print("Arcsine of 1:", np.arcsin(1))
print("Arccosine of 0:", np.arccos(0))
print("Arctangent of 1:", np.arctan(1))

'''
Exponential and Logarithmic Functions
Rounding and Modulus Functions
'''

values = np.array([1, 2, 3])

print("Exponential of values:", np.exp(values))
print("Natural log of values:", np.log(values))
print("Base-10 log of values:", np.log10(values))

values = np.array([1.7, 2.3, 3.9])

print("Floor of values:", np.floor(values))
print("Ceil of values:", np.ceil(values))
print("Rounded values:", np.round(values))

print("Modulus of 5 and 2:", np.mod(5.5, -2.0))
print("Remainder of 5 divided by 2:", np.remainder(5.5, -2.0))

'''
Linear Algebra Functions
Dot Product and Matrix Multiplication
Determinants and Inverses
Eigenvalues and Eigenvectors

'''

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("Dot product of A and B:", np.dot(A, B))
print("Matrix multiplication of A and B:", np.matmul(A, B))

print("Determinant of A:", np.linalg.det(A))
print("Inverse of A:\n", np.linalg.inv(A))

eigenvalues, eigenvectors = np.linalg.eig(A)
print("Eigenvalues of A:", eigenvalues)
print("Eigenvectors of A:\n", eigenvectors)