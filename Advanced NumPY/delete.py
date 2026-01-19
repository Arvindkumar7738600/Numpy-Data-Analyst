"""
Docstring for Advanced NumPY.delete

np.delete(array, index) - Deleting elements from a NumPy array at specified indices.
This function returns a new array with the specified elements removed.
array - original array
"""

import numpy as np 

arr = np.array([10, 20, 30, 40, 50])
new_arr = np.delete(arr, 2)  # Deleting the element at index 2
print(new_arr)  # Output: [10 20 40 50]