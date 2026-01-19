"""
Docstring for Advanced NumPY.stacking

stack(arrays, axis=0) - Stacking NumPy arrays along a specified axis.
axis=0 [ denoted ] means stacking along rows (vertical stacking)
axis=1  means stacking along columns (horizontal stacking)
This function returns a new array formed by stacking the input arrays along the specified axis.

"""

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

print(np.vstack((arr1, arr2))) # Stacking along rows

print(np.hstack((arr1, arr2))) # Stacking along columns
