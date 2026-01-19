'''
Docstring for Advanced NumPY.insert

insert(array, index, values) - Inserting values into a NumPy array at specified indices.
This function returns a new array with the values inserted at the specified indices.

np.insert(arr, index, values)
array - original array
index - index or indices before which values is inserted
values - values to be inserted into array
Returns a new array with the values inserted.

'''

import numpy as np

arr = np.array([10, 20, 30, 40, 50])
print(arr)
new_arr = np.insert(arr, 2, 1000)  # Inserting 25
print(new_arr)  # Output: [10 20 25 30 40 50]