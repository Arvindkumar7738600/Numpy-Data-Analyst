# np.isnan(array)

#np.isnan() function is used to check for NaN (Not a Number) values in a NumPy array.

import numpy as np

arr = np.array([1, 2, np.nan, 4, np.nan, 6])

print(np.isnan(arr))  # Output: [False False  True False  True False]


#Interview Question Example:

'''print(np.nan == np.nan)''' #Answer: False
