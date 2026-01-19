# np.isinf(array) returns a boolean array indicating where the elements are infinite.

#1/0

import numpy as np
arr = np.array([1, 2, np.inf, 4, -np.inf, 6])

print(np.isinf(arr))  # Output: [False False  True False  True False]