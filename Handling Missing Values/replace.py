# replace means to substitute a specific value in an array with another value.

import numpy as np
arr = np.array([1, 2, np.inf, 4, -np.inf, 6])

print(np.isinf(arr))  

cleared_arr = np.nan_to_num(arr, posinf=1000, neginf=-1000)

print(cleared_arr)  # Output: [    1.     2.  1000.     4. -1000.     6.]