'''
Slicing in NumPy allows you to extract a portion of an array by specifying a range of indices. The syntax for slicing is similar to that of Python lists, using the colon (:) operator.

array[start:end] - Slicing a NumPy array from start index to end index (exclusive).
array[start:end:step] - Slicing a NumPy array with a specified step.
'''

import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])
print(arr[1:4])        # Slicing from index 1 to 3
print(arr[::2])        # Slicing with a step of 2
print(arr[2:])         # Slicing from index 2 to the end
print(arr[:3])         # Slicing from the start to index 2
print(arr[::-1])      # Slicing using reverse indices