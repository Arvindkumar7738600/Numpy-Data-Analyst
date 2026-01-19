# .dtype means data type

# array cheaking for use dtype property

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr.dtype)


# Output: int64 (may vary based on system)
# The .dtype property returns the data type of the elements in the array.

import numpy as np
arr = np.array([1, 2, 3.1, 4.6, 5])
print(arr.dtype)

# Output: float64 (may vary based on system)
