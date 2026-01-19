import numpy as np

arr = np.array([1, 2, 3, 4.4, 5.8])
print(arr.dtype)
int_arr = arr.astype(int)

# array converted to integer type
print(int_arr)
print(int_arr.dtype)