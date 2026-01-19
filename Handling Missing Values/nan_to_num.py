#nan_to_num( array, nan=0.0, posinf=None, neginf=None)

#it means to replace NaN with zero and positive infinity with a very large number and negative infinity with a very small (or negative) number.

import numpy as np

arr = np.array([1, 2, np.nan, 4, np.nan, 6])

cleared_arr = np.nan_to_num(arr, nan=0.0, posinf=1e10, neginf=-1e10)
print(cleared_arr)  # Output: [ 1.  2.  0.  4.  0.  6.]