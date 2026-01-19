# ndim = No of dimensions
import numpy as np

arr_1d = np.array([1, 2, 3, 4, 5])
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print(arr_1d.ndim)
print(arr_2d.ndim)
print(arr_3d.ndim)


# Output: 1 means one-dimensional array
# Output: 2 means two-dimensional array
# Output: 3 means three-dimensional array