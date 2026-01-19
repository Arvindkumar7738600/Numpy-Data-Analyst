"""
Docstring for Advanced NumPY.spliting

np.slit(array, indices_or_sections, axis=0) - Splitting a NumPy array into multiple sub-arrays.
array - original array
indices_or_sections - If an integer, N, the array will be divided into N equal arrays
axis - axis along which to split the array

np.hsplit()
np.vsplit()
"""

import numpy as np
arr = np.array([10, 20, 30, 40, 50, 60])

print(np.split(arr, 3))  # Splitting into 3 equal arrays
print(np.split(arr, 2))  # Horizontal split into 3 equal arrays