'''
Docstring for Reshaping & manuplating.reshape

reshape(rows, columns) - Reshaping a NumPy array to the specified number of rows and columns.
if dimensions do not match, it will raise an error.
dimension must be same as original array.

reshaping does not create copy of original array, it returns a new view of original array.
'''


import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

reshaped_arr = arr.reshape(2, 3)
print(reshaped_arr)  # Output: 2D array with 2 rows and