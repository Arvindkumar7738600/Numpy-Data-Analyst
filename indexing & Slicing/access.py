'''
Docstring for indexing & Slicing.access

array[index] - Accessing elements in a NumPy array using indexing.
array[row, column] - Accessing elements in a 2D NumPy array using row and column indices.
'''

import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

print(arr[0])    # Accessing the first element
print(arr[2])    # Accessing the third element

print(arr[-1])   # Accessing the last element